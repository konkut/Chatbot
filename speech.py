import threading
import speech_recognition
import pyttsx3 as tts
from neuralintents.assistants import BasicAssistant

class Assistant:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty('rate', 150)
        self.assistant = BasicAssistant('intents.json')
        self.assistant.fit_model(epochs=50)
        self.assistant.save_model()

        threading.Thread(target=self.run_assistant).start()
        self.root.mainloop()

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    audio = self.recognizer.listen(mic)
                    text = text.lower()

                    if text and "hey jake" in text:
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()

                        if text == "stop":
                            self.speaker.say("Goodbye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.quit()
                            break

                        else:
                            response = self.assistant.request(text)
                            if response:
                                self.speaker.say(response)
                                self.speaker.runAndWait()
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    Assistant()