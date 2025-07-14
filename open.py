import os
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def OpenExe(query):
   
    speak("Okay sir, opening...")
    
    if "notepad" in query:
        path = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(path)

    elif "ppt" in query or "powerpoint" in query:
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(path)
        

        
    else:
        speak("Sorry,dont know how to open it.")