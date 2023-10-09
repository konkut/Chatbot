import pyttsx3
engine = pyttsx3.init() # object creation

def speaking(text):
  rate = engine.getProperty('rate')   # getting details of current speaking rate
  engine.setProperty('rate', 125)     # setting up new voice rate
  volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                  #printing current volume level
  engine.setProperty('volume',0.5)    # setting up volume level  between 0 and 1
  voices = engine.getProperty('voices')       #getting details of current voice
  engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male
  engine.say(text)
  engine.runAndWait()
  engine.stop()

