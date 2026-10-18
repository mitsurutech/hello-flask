# Application Flask « Hello World » : déployer une application web Python depuis GitHub

[English](README.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [Español](README.es.md)

Une application web Flask (Python) « Hello World ». Déployez-la gratuitement depuis son adresse GitHub avec la
fonction [déployer une application web depuis GitHub](https://mitsurutech.co.uk/fr/apps) de MitsuruTech : sans compte, rien à
installer. Elle est assez petite pour servir de premier test de déploiement sur `learntools.dev`, et les étapes
sont dans le [guide du manuel pour déployer des applications Python, Node, Go et Java depuis GitHub](https://mitsurutech.co.uk/fr/help/deploy-app).

    Language        Python
    Build           pip install --target .deps -r requirements.txt
    Start           PYTHONPATH=.deps gunicorn --bind 0.0.0.0:$PORT app:app

Ce sont les valeurs par défaut de la plateforme ; rien ici n’a besoin d’être modifié.

**Pourquoi `--target .deps`.** La compilation et l’exécution se font dans deux conteneurs différents
qui ne partagent que cette copie du dépôt : les dépendances doivent donc atterrir *ici* plutôt que dans le Python
du conteneur de compilation. Un simple `pip install` annonce un succès, puis l’application ne peut pas
importer Flask.

## L’exécuter vous-même

    python -m venv .venv && .venv/bin/pip install -r requirements.txt
    .venv/bin/python app.py

## Licence

Cette œuvre est sous licence [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Vous pouvez la partager et l’adapter pour apprendre et enseigner, à condition de citer Mitsuru Technologies Ltd, de ne pas l’utiliser commercialement et de partager tout ce que vous en tirez sous la même licence. Le texte complet est dans le fichier `LICENSE`.

## À propos

Réalisé par [Mitsuru Technologies](https://mitsurutech.co.uk/fr) pour la
[plateforme d’apprentissage MitsuruTech](https://mitsurutech.co.uk/fr/learning) : Python, Java, Go, Node, SQL et
Linux dans le navigateur pour les écoles et les établissements, avec des labs de conteneurs, des applications web déployées depuis GitHub et
des quiz corrigés automatiquement. Essayez du code sans compte dans le
[bac à sable](https://mitsurutech.co.uk/fr/playground).

Vous enseignez à une classe ? Consultez [le prix](https://mitsurutech.co.uk/fr/pricing) ou [créez un compte d’établissement](https://mitsurutech.co.uk/fr/signup).
