#!/bin/bash

# Répertoire local du référentiel
repo_dir="C:\Users\jessg\OneDrive - INSTITUTION CHARTREUX\Bureau\lourenco\md\markdown"

# URL du référentiel GitLab
gitlab_url="https://gitlab.com/Virgil21/markdown.git"

# Vérifier s'il y a des mises à jour disponibles
git fetch --quiet

if [[ $(git rev-parse HEAD) != $(git rev-parse @{u}) ]]; then
    # Effectuer le pull
    git pull --quiet

    # Exécuter d'autres commandes ou actions ici si nécessaire

    echo "Pull effectué avec succès."
else
    echo "Aucune nouvelle version disponible."
fi