import pyttsx3

engine = pyttsx3.init()
name = input("Enter name: ")
engine.say("Hello, " + name)
engine.runAndWait()