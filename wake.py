import speech_recognition as sr 


wake_words = [
    "hey jarvis", 
    "jarvis, are you there?", 
    "are you there, jarvis?",
    "jarvis wake up",
    "ok jarvis"
]

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Waiting for a wake word...")
        recognizer.pause_threshold = 0.75 #seconds.
        audio = recognizer.listen(source)

        try:
            print("Waking up...")
            wake_word = recognizer.recognize_google(audio)

            if wake_word in wake_words:
                print(f"Wake word {wake_word} detected!")

        except Exception as e:
            print("No wake words detected!")