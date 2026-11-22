# Hello-World-App mit Flask: eine Python-Web-App aus GitHub bereitstellen

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Eine Hello-World-Web-App mit Flask (Python). Stellen Sie sie kostenlos über ihre GitHub-Adresse mit der
MitsuruTech-Funktion [Web-App aus GitHub bereitstellen](https://mitsurutech.co.uk/de/apps) bereit: ohne Konto,
ohne Installation. Sie ist klein genug für einen ersten Test der Bereitstellung auf `learntools.dev`, und die
Schritte stehen in der [Anleitung des Handbuchs zum Bereitstellen von Python-, Node-, Go- und Java-Apps aus GitHub](https://mitsurutech.co.uk/de/help/deploy-app).

    Language        Python
    Build           pip install --target .deps -r requirements.txt
    Start           PYTHONPATH=.deps gunicorn --bind 0.0.0.0:$PORT app:app

Das sind die Standardwerte der Plattform; hier muss nichts geändert werden.

**Warum `--target .deps`.** Build und Ausführung laufen in zwei verschiedenen Containern, die nur
diesen Checkout gemeinsam haben. Die Abhängigkeiten müssen deshalb *hier* landen und nicht im Python
des Build-Containers. Ein einfaches `pip install` meldet Erfolg, und danach kann die App Flask nicht
importieren.

## Selbst ausführen

    python -m venv .venv && .venv/bin/pip install -r requirements.txt
    .venv/bin/python app.py

## Lizenz

Dieses Werk steht unter der Lizenz [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Sie dürfen es zum Lernen und Unterrichten teilen und bearbeiten, sofern Sie Mitsuru Technologies Ltd nennen, es nicht kommerziell nutzen und alles, was Sie daraus machen, unter derselben Lizenz teilen. Der vollständige Text steht in der Datei `LICENSE`.

## Über dieses Projekt

Erstellt von [Mitsuru Technologies](https://mitsurutech.co.uk/de) für die
[MitsuruTech Learning Platform](https://mitsurutech.co.uk/de/learning): Python, Java, Go, Node, SQL und
Linux im Browser für Schulen und Colleges, mit Container-Labs, aus GitHub bereitgestellten Web-Apps und
Quizzen, die sich selbst bewerten. Probieren Sie Code ohne Konto im
[Playground](https://mitsurutech.co.uk/de/playground) aus.

Sie unterrichten eine Klasse? Sehen Sie sich [den Preis](https://mitsurutech.co.uk/de/pricing) an oder [legen Sie ein Schulkonto an](https://mitsurutech.co.uk/de/signup).
