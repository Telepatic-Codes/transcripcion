import argparse
import speech_recognition as sr


def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language='es-ES')
        return text
    except sr.UnknownValueError:
        return "No se pudo entender el audio"
    except sr.RequestError as e:
        return f"Error al realizar la solicitud: {e}"


def main():
    parser = argparse.ArgumentParser(description="Transcribe un archivo de audio")
    parser.add_argument('audio_file', help='Ruta al archivo de audio (wav, aiff, flac)')
    args = parser.parse_args()

    texto = transcribe_audio(args.audio_file)
    print(texto)


if __name__ == '__main__':
    main()
