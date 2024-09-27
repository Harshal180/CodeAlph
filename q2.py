import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for a voice command and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Network error.")
            return None

def respond(command):
    """Respond to specific voice commands."""
    if 'your name' in command:
        speak("I am your personal assistant.")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif 'play music' in command:
        music_dir = "C:/Path/To/Your/Music/Folder"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music")
    elif 'stop' in command or 'exit' in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I didn't understand that command.")
    return True

def start_assistant():
    """Main loop to run the voice assistant."""
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if command:
            if not respond(command):
                break

if __name__ == "__main__":
    start_assistant()
