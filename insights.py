import os
import requests
import time
import matplotlib.pyplot as plt
from datetime import datetime, UTC

# === KONFIGURATION ===
USERNAME = "hjstephan86"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("Umgebungsvariable GITHUB_TOKEN nicht gesetzt!")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
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
        "pulls": [{
            "timestamp": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "count": pull_count,
            "uniques": 0  # Kein Unique-Wert verfügbar
        }]
    }

# === PLOT UND TXT ===

def plot_metric(repo_name, data, kind):
    if not data or kind not in ["clones", "views", "commits", "pulls"]:
        print(f"Keine Daten für {repo_name} ({kind})")
        return

    if kind == "pulls":
        records = data["pulls"]
    elif kind == "commits":
        records = []
        for entry in data:
            dt = datetime.utcfromtimestamp(entry["week"]).strftime("%Y-%m-%dT00:00:00Z")
            records.append({
                "timestamp": dt,
                "count": entry["total"],
                "uniques": 0
            })
    else:
        records = data[kind]

    # Bestehende TXT-Dateien laden
    combined_data = {}
    txt_dir = "txt"

    for fname in os.listdir(txt_dir):
        if fname.startswith(f"{repo_name}.{kind}") and fname.endswith(".txt"):
            with open(os.path.join(txt_dir, fname), "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("timestamp") or line.strip() == "":
                        continue
                    if "," in line and "Total" not in line:
                        try:
                            timestamp, count, uniques = line.strip().split(",")
                            combined_data[timestamp] = {
                                "timestamp": timestamp,
                                "count": int(count),
                                "uniques": int(uniques)
                            }
                        except ValueError:
                            continue

    # Neue API-Daten integrieren (und überschreiben ggf. alte)
    for entry in records:
        combined_data[entry["timestamp"]] = entry

    # Sortieren nach Zeit
    sorted_records = sorted(combined_data.values(), key=lambda x: x["timestamp"])

    dates = [datetime.strptime(e["timestamp"], "%Y-%m-%dT%H:%M:%SZ") for e in sorted_records]
    counts = [e["count"] for e in sorted_records]
    uniques = [e["uniques"] for e in sorted_records]

    total_count = sum(counts)
    total_uniques = sum(uniques)

    # === SVG ===
    plt.figure(figsize=(10, 5))
    plt.plot(dates, counts, label="Count", marker='o')
    plt.plot(dates, uniques, label="Unique", marker='x')
    plt.title(f"{kind.capitalize()} Traffic for {repo_name}")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.grid(True)

    textstr = f"Total {kind.capitalize()}: {total_count}\nTotal Unique {kind.capitalize()}: {total_uniques}"
    plt.gca().text(
        0.02, 0.02, textstr,
        transform=plt.gca().transAxes,
        ha='left', va='bottom',
        fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7, boxstyle='round')
    )

    plt.tight_layout()
    svg_path = f"svg/{repo_name}.{kind}.svg"
    plt.savefig(svg_path, format="svg")
    plt.close()
    print(f"Diagramm gespeichert: {svg_path}")

    # === TXT (nur für heutige Daten) ===
    date_today = datetime.now(UTC).strftime("%Y%m%d")
    txt_path = f"txt/{repo_name}.{kind}.{date_today}.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("timestamp,count,uniques\n")
        for entry in records:
            f.write(f"{entry['timestamp']},{entry['count']},{entry['uniques']}\n")
        f.write(f"\nTotal {kind.capitalize()}: {total_count}\n")
        f.write(f"Total Unique {kind.capitalize()}: {total_uniques}\n")
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
