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
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{repo}: Zugriff verweigert oder Fehler ({response.status_code})")
        return None


def plot_clones(repo_name, clones_data):
    if not clones_data or "clones" not in clones_data:
        print(f"Keine Clonedaten für {repo_name}")
        return

    dates = [datetime.strptime(entry["timestamp"], "%Y-%m-%dT%H:%M:%SZ") for entry in clones_data["clones"]]
    counts = [entry["count"] for entry in clones_data["clones"]]
    uniques = [entry["uniques"] for entry in clones_data["clones"]]

    total_clones = sum(counts)
    total_unique_clones = sum(uniques)

    # === SVG speichern ===
    plt.figure(figsize=(10, 5))
    plt.plot(dates, counts, label="Clones", marker='o')
    plt.plot(dates, uniques, label="Unique Clones", marker='x')
    plt.title(f"Clone Traffic for {repo_name}")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.grid(True)
    textstr = f"Total Clones: {total_clones}\nTotal Unique Clones: {total_unique_clones}"
    plt.gca().text(
        0.02, 0.02, textstr,
        transform=plt.gca().transAxes,
        ha='left', va='bottom',
        fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7, boxstyle='round')
    )
    plt.tight_layout()
    svg_path = f"svg/{repo_name}.clones.svg"
    plt.savefig(svg_path, format="svg")
    plt.close()
    print(f"Diagramm gespeichert: {svg_path}")

    # === TXT-Datei speichern ===
    date_today = datetime.now(UTC).strftime("%Y%m%d")
    txt_path = f"txt/{repo_name}.clones.{date_today}.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("timestamp,count,uniques\n")
        for entry in clones_data["clones"]:
            f.write(f"{entry['timestamp']},{entry['count']},{entry['uniques']}\n")
        f.write(f"\nTotal Clones: {total_clones}\n")
        f.write(f"Total Unique Clones: {total_unique_clones}\n")
    print(f"Textdatei gespeichert: {txt_path}")

def main():
    repos = get_repos(USERNAME)
    print(f"\n📦 Gefundene Repositories für {USERNAME}: {len(repos)}\n")

    for repo in repos:
        name = repo["name"]
        print(f"🔍 Verarbeite Repository: {name}")
        clone_data = get_clone_traffic(USERNAME, name)
        if clone_data:
            plot_clones(name, clone_data)
        time.sleep(1)  # API-Rate-Limit beachten


if __name__ == "__main__":
    main()
