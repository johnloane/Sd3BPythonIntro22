import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something")
    audio = recognizer.listen(source)

    print("Good Speech Recognition thinks you said: ")
    print(recognizer.recognize_google(audio))