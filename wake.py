import speech_recognition as sr 


wake_words = [
    "hey jarvis", 
    "jarvis, are you there?", 
    "are you there, jarvis?",
    "jarvis wake up",
    "ok jarvis",
    "hello world"
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
            wake_word = wake_word.lower()

            if wake_word in wake_words:
                print(f"Wake word {wake_word} detected!")
                print("Please give me some command :)")
                recognizer.pause_threshold = 0.5 #seconds 
                audio = recognizer.listen(source)

                try:
                    command = recognizer.recognize_google(audio)
                    command = command.lower()

                    print(f"You said: {command}")

                    if command == "goodbye":
                        exit()
                except Exception as e:
                    print("You woke me up, but didn't ask me anything -__-")

        except Exception as e:
            print("No wake words detected!")
            continue