# Aplicación Flask «Hola mundo»: despliega una aplicación web Python desde GitHub

[English](README.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [Español](README.es.md)

Una aplicación web Flask (Python) de «Hola mundo». Despliégala gratis desde su dirección de GitHub con la función
[desplegar una aplicación web desde GitHub](https://mitsurutech.co.uk/es/apps) de MitsuruTech: sin cuenta y sin instalar
nada. Es lo bastante pequeña para ser una primera prueba de despliegue en `learntools.dev`, y los pasos
están en la [guía del manual para desplegar aplicaciones Python, Node, Go y Java desde GitHub](https://mitsurutech.co.uk/es/help/deploy-app).

    Language        Python
    Build           pip install --target .deps -r requirements.txt
    Start           PYTHONPATH=.deps gunicorn --bind 0.0.0.0:$PORT app:app

Son los valores por defecto de la plataforma; aquí no hace falta cambiar nada.

**Por qué `--target .deps`.** La compilación y la ejecución ocurren en dos contenedores distintos
que solo comparten esta copia del repositorio, así que las dependencias tienen que acabar *aquí* y no en el Python
del contenedor de compilación. Un `pip install` normal informa de que todo ha ido bien y después la aplicación no puede
importar Flask.

## Ejecutarla tú mismo

    python -m venv .venv && .venv/bin/pip install -r requirements.txt
    .venv/bin/python app.py

## Licencia

Esta obra está bajo licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Puedes compartirla y adaptarla para aprender y enseñar, si citas a Mitsuru Technologies Ltd, no la usas comercialmente y compartes lo que hagas con ella bajo la misma licencia. El texto completo está en el archivo `LICENSE`.

## Acerca de

Hecho por [Mitsuru Technologies](https://mitsurutech.co.uk/es) para la
[plataforma de aprendizaje MitsuruTech](https://mitsurutech.co.uk/es/learning): Python, Java, Go, Node, SQL y
Linux en el navegador para escuelas y centros, con laboratorios de contenedores, aplicaciones web desplegadas desde GitHub y
cuestionarios que se califican solos. Prueba código sin cuenta en el
[entorno de pruebas](https://mitsurutech.co.uk/es/playground).

¿Das clase? Mira [el precio](https://mitsurutech.co.uk/es/pricing) o [crea una cuenta de centro](https://mitsurutech.co.uk/es/signup).
