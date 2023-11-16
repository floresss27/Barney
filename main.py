import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def send_gpt(message):
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt= message,
        max_tokens=150
    )

    resposta_texto = resposta['choices'][0]['text']

    return resposta_texto

def text_to_speech(text, rate=250):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Fale algo...")

    recognizer.adjust_for_ambient_noise(source)

    try:
        while True:
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio, language="pt-BR")
            print("Texto reconhecido:", text)
            text_to_speech(send_gpt(text))
            print("Fale algo...")
            recognizer.adjust_for_ambient_noise(source)
            if "Barney encerrar conversa" in text:
                print("Conversa encerrada.")
                break

    except sr.UnknownValueError:
        print("Não foi possível entender a fala")
    except sr.RequestError as e:
        print(f"Erro na requisição para a API do Google: {e}")
