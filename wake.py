import speech_recognition as sr 


wake_words = [
    "hey jarvis", 
    "jarvis, are you there?", 
    "are you there, jarvis?",
    "jarvis wake up",
    "ok jarvis"
]

recognizer = sr.Recognizer()