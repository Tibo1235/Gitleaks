# GitLeaks Watcher

## Description
GitLeaks Watcher est un outil conçu pour les développeurs et administrateurs afin de sécuriser leurs dépôts GitHub en détectant des informations sensibles telles que des clés API, des identifiants AWS ou des mots de passe exposés.

## Fonctionnalités
- Scanne un dépôt GitHub public via l'API GitHub.
- Détecte les clés API, les tokens d'accès et les mots de passe dans les fichiers.
- Affiche les résultats sous forme de tableau coloré grâce à `rich`.  
  *(Un exemple d'affichage serait utile ici.)*

## Installation
### Prérequis
- Python 3.7+
- Pip

### Installation des dépendances
```bash
pip install requests rich
```

## Utilisation
### Scanner un dépôt Github
Exécutez la commande suivante :

```
python Gitleaks.py https://github.com/user/repository
```
(Remplacez https://github.com/user/repository par l'URL du dépôt que vous souhaitez analyser.)

## Amélioration futures

- Ajout d'un mode de surveillance continue des nouveaux commits.
- Intégration avec slack/Discord pour recevoir des alertes.
- Analyse avancée avec de l'IA pour de l'amélioration de détection.