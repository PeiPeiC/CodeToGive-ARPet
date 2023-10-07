import speech_recognition as sr
import openai

r = sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=10)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)

openai.api_key = "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"

x = text

response = openai.Image.create(
  prompt=x,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
