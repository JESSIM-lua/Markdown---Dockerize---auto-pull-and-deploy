import os
import time
import subprocess
import requests
from git import Repo

# URL du dépôt GitHub
repo_url = "https://github.com/JESSIM-lua/Markdown---Dockerize---auto-pull-and-deploy"
# Chemin vers le répertoire local du dépôt
local_repo_path = "/workspaces/Markdown---Dockerize---auto-pull-and-deploy"
# Intervalle de vérification en secondes (par exemple, toutes les 60 secondes)
check_interval = 5

def get_latest_commit_sha(repo_url):
    # URL de l'API GitHub pour récupérer les informations du dernier commit
    api_url = f"https://api.github.com/repos/{'/'.join(repo_url.split('/')[-2:])}/commits"
    response = requests.get(api_url)
    if response.status_code == 200:
        commits = response.json()
        if commits:
            return commits[0]['sha']
    return None

def pull_changes(local_repo_path):
    repo = Repo(local_repo_path)
    origin = repo.remotes.origin
    origin.pull()

def main():
    if not os.path.exists(local_repo_path):
        # Cloner le dépôt si le répertoire local n'existe pas
        Repo.clone_from(repo_url, local_repo_path)

    last_commit_sha = get_latest_commit_sha(repo_url)

    while True:
        time.sleep(check_interval)
        latest_commit_sha = get_latest_commit_sha(repo_url)
        if latest_commit_sha and latest_commit_sha != last_commit_sha:
            print("Nouvelles modifications détectées. Pull des dernières modifications...")
            pull_changes(local_repo_path)
            last_commit_sha = latest_commit_sha
            print("Pull réussi.")
        else:
            print("Aucune modification détectée.")

if __name__ == "__main__":
    main()
