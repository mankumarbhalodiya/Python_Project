import speech_recognition as sr
import webbrowser
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 135)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    query = r.recognize_google(audio, language='en-in')
    return query.lower()

def main():
    speak("Hello, I am your AI. how can I help you")

    voice = listen()

    if "youtube" in voice:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "spotify" in voice:
        speak("Opening Spotify.")
        webbrowser.open("https://open.spotify.com")

    elif "play music" in voice:
        speak("Playing your music.")
        music_file = r"D:\MUSIC\MIX MUSIC\_Sooraj_Dooba_Hain__FULL_VIDEO_SONG___Arijit_singh_Aditi_Singh_Sharma___T-SERIES(48k).mp3"
        os.startfile(music_file)

    elif "notepad" in voice:
        speak("Opening Notepad.")
        os.system("notepad")

    elif "canvas" in voice:
        speak("Opening Canvas App.")
        webbrowser.open(r"https://canvas.instructure.com/login/canvas")

if __name__ == "__main__":
    main()

