# library ko import kiya
import pyttsx3
import speech_recognition as sr 
import os 

from open import OpenExe 

# sabhi kaam ki chijo ko nikala 
engine = pyttsx3.init()

# voice ke liye setup kiya 
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

# speech ke liye short cut banaya 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("mai sun raha hu ......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        print("sorry mai sun nahi paya, phir se bolo")
        return "None"
    return query 

# final test 
if __name__ == "__main__":
    speak("hi boss.")
    while True:
        query = takecommand().lower().strip()
        
        if "hello" in query:
            speak("hello boss")

        elif "hi" in query:
            speak("hi boss")

        elif "good morning" in query:
            speak("good morning boss")

        elif "good afternoon" in query:
            speak("good afternoon boss")
            
        elif "who is your boss" in query:
            speak("prince sir, he is the person who made me and he is genius")

        elif "open" in query:           
            OpenExe(query)
        elif "you are genius" in query:
            speak("thankyou but real genius is prince.")
        elif "play romantic" in query:
            speak("ok boss, playing song")
            music_dir = "C:\\Users\\prince\\Desktop\\songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "play motivational" in query:
             speak("ok boss, playing song")
             music_dir = "C:\\Users\\prince\\Desktop\\songs"
             songs = os.listdir(music_dir)
             os.startfile(os.path.join(music_dir,songs[1]))

            
        elif "bye-bye" in query or "quit" in query:
            speak("Goodbye boss!")
            break

