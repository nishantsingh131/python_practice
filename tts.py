import pyttsx3

engine = pyttsx3.init()
for _ in range(5):   # Speak 5 times
    engine.say("Durgesh Nai")
engine.runAndWait()
