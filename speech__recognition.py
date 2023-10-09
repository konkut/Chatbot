import speech_recognition as sr

# recognize speech using Google Speech Recognition
def get_recognize_google():
  try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
      audio = r.listen(source)
    return r.recognize_google(audio)
  except sr.UnknownValueError:
    return "No puedo entender el audio"
  except sr.RequestError as e:
    return "No se pudieron solicitar resultados del servicio de reconocimiento de voz de Google"   

