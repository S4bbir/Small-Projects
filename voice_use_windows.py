import pyttsx3

engine = pyttsx3.init()

def get_text():
    return input("Enter text: ")

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(get_text):
    text = get_text()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak(get_text)

print("Available Voices")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} - {voice.id}")