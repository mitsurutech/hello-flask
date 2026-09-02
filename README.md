# hello-flask

A hello-world Flask app, small enough to be a first test of deploying to
`learntools.dev`.

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
