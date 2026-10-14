# Hello World Flask app: deploy a Python web app from GitHub

A hello-world Flask (Python) web app. Deploy it free from its GitHub address with the MitsuruTech
[deploy a web app from GitHub](https://mitsurutech.co.uk/apps) feature: no account, nothing to
install. It is small enough to be a first test of deploying to `learntools.dev`, and the steps
are in the manual's [guide to deploying Python, Node, Go and Java apps from GitHub](https://mitsurutech.co.uk/help/deploy-app).

    Language        Python
    Build           pip install --target .deps -r requirements.txt
    Start           PYTHONPATH=.deps gunicorn --bind 0.0.0.0:$PORT app:app

Those are the platform's defaults; nothing here needs changing.

**Why `--target .deps`.** The build and the run happen in two different containers that
share only this checkout, so dependencies have to land *here* rather than in the build
container's own Python. A plain `pip install` reports success and then the app cannot
import Flask.

## Running it yourself

    python -m venv .venv && .venv/bin/pip install -r requirements.txt
    .venv/bin/python app.py

## About

Made by [Mitsuru Technologies](https://mitsurutech.co.uk) for the
[MitsuruTech Learning Platform](https://mitsurutech.co.uk/learning): Python, Java, Go, Node, SQL and
Linux in the browser for schools and colleges, with container labs, web apps deployed from GitHub, and
quizzes that mark themselves. Try code with no account in the
[playground](https://mitsurutech.co.uk/playground).
