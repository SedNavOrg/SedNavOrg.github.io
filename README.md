# Documentation du projet SedNav
Le projet SedNav est un système complet de navigation pour bateau à voile, entièrement Open Source et Open Hardware.

## Fonctionnement
La documentation est sous la forme de fichiers Markdown, et est transformée en site web à l'aide de [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Le site web est hébergé sur GitHub Pages. Une action GitHub génère et publie automatiquement le site à chaques nouveaux changements sur la branche `main` de ce repo.
### Version anglaise
Certaines pages sont traduite. Pour ce faire, il suffit de créer une copie de la page française, en la faisant terminer par l'extension `.en.md`.

## Contribuer
### En ligne
Pour éditer une page de cette documentation, il vous suffit de cliquer sur l'icône "éditer cette page" qui se situe en haut à droite de la page web.
Vous pouvez également éditer ou créer une page en anglais de la même manière.

### En local
Pour modifier la documentation en local, commencez par cloner le repo git. Il vous faut ensuite créer un nouvel environnement virtuel Python, et y installer les modules définis dans le fichier `requirements.txt`.  
Pour Ubuntu:
```console
git clone https://github.com/SedNavOrg/SedNavOrg.github.io.git
cd SedNavOrg.github.io
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Il vous faut également la dépendance `pngquant` d'installé.
```console
sudo apt install -y pngquant
```
Vous pouvez ensuite utiliser la commande `mkdocs serve` pour lancer un serveur web en local et voir le rendu du site.
```console
mkdocs serve
```
