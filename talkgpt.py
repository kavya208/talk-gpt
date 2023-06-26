import openai
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
openai.api_key = "Api key here"
engine = pyttsx3.init()
while True:
  with sr.Microphone() as source:
    print("speak.....")
    voice=listener.listen(source)
    data=listener.recognize_google(voice)
    # model which will provide us with the info through openai
    models = "text-davinci-003"

    if "exit" in data:
      break

  #response from the model
  completion = openai.Completion.create(model = "text-davinci-003",
  prompt = data, #question that will be asked to get input
  max_tokens=1024, #max number of words
  temperature = 0.5, #accuracy of the output
  n=1,
  stop= None)

  response = completion.choices[0].text
  print(response)
  engine.say(response)
  engine.runAndWait()