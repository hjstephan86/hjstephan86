import os
import time
from datetime import UTC, datetime

import matplotlib.pyplot as plt
import requests

# === KONFIGURATION ===
USERNAME = "hjstephan86"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("Umgebungsvariable GITHUB_TOKEN nicht gesetzt!")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

BASE_URL = "https://api.github.com"


# === TRAFFIC-DATEN ===


def get_repos(username):
    repos = []
    page = 1
    while True:
        url = f"{BASE_URL}/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Repos: {response.status_code}")
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos


def get_clone_traffic(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/traffic/clones"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.status_code == 200 else None


def get_view_traffic(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/traffic/views"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.status_code == 200 else None


def get_pull_requests(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/pulls?state=all&per_page=100"
    pull_count = 0
    page = 1

    while True:
        response = requests.get(f"{url}&page={page}", headers=HEADERS)
        if response.status_code != 200:
            break
        data = response.json()
        if not data:
            break
        pull_count += len(data)
        page += 1
    return {
        "pulls": [
            {
                "timestamp": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "count": pull_count,
                "uniques": 0,  # Kein Unique-Wert verfügbar
            }
        ]
    }


# === PLOT UND TXT ===


def load_existing_txt_data(repo_name, kind):
    """Load and merge all existing TXT files for a repository and metric type."""
    combined_data = {}
    txt_dir = "txt"

    if not os.path.exists(txt_dir):
        os.makedirs(txt_dir)
        return combined_data

    # Find all txt files for this repo and metric
    for fname in os.listdir(txt_dir):
        if fname.startswith(f"{repo_name}.{kind}") and fname.endswith(".txt"):
            print(f"Loading existing data from: {fname}")
            try:
                with open(os.path.join(txt_dir, fname), "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        # Skip headers, empty lines, and total lines
                        if (
                            line.startswith("timestamp")
                            or line == ""
                            or "Total" in line
                            or not "," in line
                        ):
                            continue

                        try:
                            parts = line.split(",")
                            if len(parts) >= 3:
                                timestamp, count, uniques = parts[0], parts[1], parts[2]

                                # Handle overlapping timestamps - keep the most recent data
                                # (assuming later files contain more recent/accurate data)
                                combined_data[timestamp] = {
                                    "timestamp": timestamp,
                                    "count": int(count),
                                    "uniques": int(uniques),
                                }
                        except (ValueError, IndexError) as e:
                            print(
                                f"Skipping invalid line in {fname}: {line} (Error: {e})"
                            )
                            continue
            except Exception as e:
                print(f"Error reading file {fname}: {e}")
                continue

    print(f"Loaded {len(combined_data)} existing data points for {repo_name}.{kind}")
    return combined_data


def merge_api_data(combined_data, api_records):
    """Merge API data with existing data, handling overlaps."""
    for entry in api_records:
        timestamp = entry["timestamp"]

        # If timestamp already exists, keep the API data (more recent/accurate)
        if timestamp in combined_data:
            print(f"Updating existing timestamp: {timestamp}")

        combined_data[timestamp] = {
            "timestamp": timestamp,
            "count": entry["count"],
            "uniques": entry["uniques"],
        }

    return combined_data


def fill_gaps_with_zeros(sorted_records):
    """Fill gaps in data with zero values for better visualization."""
    if len(sorted_records) < 2:
        return sorted_records

    filled_records = []

    for i, record in enumerate(sorted_records):
        filled_records.append(record)

        # Check if there's a next record and if there's a gap
        if i < len(sorted_records) - 1:
            current_date = datetime.strptime(record["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            next_date = datetime.strptime(
                sorted_records[i + 1]["timestamp"], "%Y-%m-%dT%H:%M:%SZ"
            )

            # If gap is more than 2 days, add zero entries
            gap_days = (next_date - current_date).days
            if gap_days > 2:
                print(
                    f"Found {gap_days}-day gap between {current_date.date()} and {next_date.date()}"
                )
                # Add a zero entry in the middle of the gap for visualization
                middle_date = current_date + (next_date - current_date) / 2
                filled_records.append(
                    {
                        "timestamp": middle_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "count": 0,
                        "uniques": 0,
                    }
                )

    return sorted(filled_records, key=lambda x: x["timestamp"])


def plot_metric(repo_name, data, kind):
    if not data or kind not in ["clones", "views", "commits", "pulls"]:
        print(f"Keine Daten für {repo_name} ({kind})")
        return

    # Ensure directories exist
    os.makedirs("svg", exist_ok=True)
    os.makedirs("txt", exist_ok=True)

    # Extract API records based on data type
    if kind == "pulls":
        api_records = data["pulls"]
    elif kind == "commits":
        api_records = []
        for entry in data:
            dt = datetime.utcfromtimestamp(entry["week"]).strftime("%Y-%m-%dT00:00:00Z")
            api_records.append({"timestamp": dt, "count": entry["total"], "uniques": 0})
    else:
        api_records = data[kind]

    # Load existing data from all TXT files
    combined_data = load_existing_txt_data(repo_name, kind)

    # Merge with new API data
    combined_data = merge_api_data(combined_data, api_records)

    # Sort by timestamp
    sorted_records = sorted(combined_data.values(), key=lambda x: x["timestamp"])

    if not sorted_records:
        print(f"Keine verwertbaren Daten für {repo_name} ({kind})")
        return

    # Fill gaps for better visualization
    filled_records = fill_gaps_with_zeros(sorted_records)

    # Prepare data for plotting
    dates = []
    counts = []
    uniques = []

    for record in filled_records:
        try:
            date = datetime.strptime(record["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            dates.append(date)
            counts.append(record["count"])
            uniques.append(record["uniques"])
        except ValueError as e:
            print(f"Invalid timestamp format: {record['timestamp']} - {e}")
            continue

    if not dates:
        print(f"Keine gültigen Timestamps für {repo_name} ({kind})")
        return

    total_count = sum(counts)
    total_uniques = sum(uniques)

    # === SVG ===
    plt.figure(figsize=(12, 6))

    if total_count > 0:
        plt.plot(dates, counts, label="Count", marker="o", linewidth=2, markersize=4)
    if total_uniques > 0:
        plt.plot(dates, uniques, label="Unique", marker="x", linewidth=2, markersize=4)

    plt.title(
        f"{kind.capitalize()} Traffic for {repo_name}\n({len(sorted_records)} data points, {len(filled_records)} including gap fills)"
    )
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)

    # Add statistics text box
    date_range = f"{dates[0].strftime('%Y-%m-%d')} to {dates[-1].strftime('%Y-%m-%d')}"
    textstr = (
        f"Total {kind.capitalize()}: {total_count}\n"
        f"Total Unique: {total_uniques}\n"
        f"Date Range: {date_range}"
    )

    plt.gca().text(
        0.02,
        0.98,
        textstr,
        transform=plt.gca().transAxes,
        ha="left",
        va="top",
        fontsize=9,
        bbox=dict(facecolor="white", alpha=0.8, boxstyle="round,pad=0.5"),
    )

    plt.tight_layout()
    svg_path = f"svg/{repo_name}.{kind}.svg"
    plt.savefig(svg_path, format="svg", dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Diagramm gespeichert: {svg_path}")

    # === TXT (save today's data with merged historical data) ===
    date_today = datetime.now(UTC).strftime("%Y%m%d")
    txt_path = f"txt/{repo_name}.{kind}.{date_today}.txt"

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("timestamp,count,uniques\n")
        for record in sorted_records:  # Use original sorted data, not gap-filled
            f.write(f"{record['timestamp']},{record['count']},{record['uniques']}\n")
        f.write(f"\nTotal {kind.capitalize()}: {total_count}\n")
        f.write(f"Total Unique {kind.capitalize()}: {total_uniques}\n")
        f.write(f"Data points: {len(sorted_records)}\n")
        f.write(f"Date range: {date_range}\n")

    print(f"Textdatei gespeichert: {txt_path}")


# === MAIN ===


def main():
    repos = get_repos(USERNAME)
    print(f"\n📦 Gefundene Repositories für {USERNAME}: {len(repos)}\n")

    for repo in repos:
        name = repo["name"]
        print(f"\n🔍 Verarbeite Repository: {name}")

        clone_data = get_clone_traffic(USERNAME, name)
        if clone_data:
            plot_metric(name, clone_data, "clones")

        time.sleep(1)

        view_data = get_view_traffic(USERNAME, name)
        if view_data:
            plot_metric(name, view_data, "views")

        time.sleep(1)

        pull_data = get_pull_requests(USERNAME, name)
        if pull_data:
            plot_metric(name, pull_data, "pulls")

        time.sleep(1)


if __name__ == "__main__":
    main()
