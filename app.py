"""A hello-world Flask app for learntools.dev.

The one rule this platform asks: listen on the port it gives you. Locally that is 5000 by
default; when it is deployed, $PORT is set and gunicorn is told it on the command line, so
this file never reads it at all.
"""
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return (
        "<h1>Hello from Flask</h1>"
        f"<p>Serving on port {os.environ.get('PORT', '5000')}.</p>"
        "<p>Written by a student, hosted for an hour.</p>"
    )


@app.route("/healthz")
def healthz():
    return {"ok": True}


if __name__ == "__main__":
    # Only for running it on your own machine. The deployment uses gunicorn.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
