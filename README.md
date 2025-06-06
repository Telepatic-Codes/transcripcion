# Transcripción de Audio

Este proyecto contiene un pequeño script en Python para transcribir archivos de audio a texto utilizando la librería `speech_recognition`.

## Requisitos

- Python 3.7 o superior
- Dependencias listadas en `requirements.txt`

Instálalas con:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el script indicando la ruta de un archivo de audio (formatos compatibles: WAV, AIFF, FLAC):

```bash
python transcribe.py ruta/al/archivo.wav
```

El texto transcrito se imprimirá por pantalla.

## Notas

El script utiliza el servicio de reconocimiento de voz de Google por defecto, por lo que se necesita conexión a Internet para realizar la transcripción.
