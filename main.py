import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests 


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = 'a777f2f3b3664d96adb15c7d12cf982d'


  

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open Youtube" in c.lower(): 
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif 'news' in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        r.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response as JSON
        data = r.json()

        # Check for status in response
        if data.get("status") == "ok":
            # Retrieve and print articles
            articles = data.get("articles", [])
            print(f"Found {len(articles)} articles:\n")
            
            for index, article in enumerate(articles, start=1):
                speak(article['title'])
                print(f"Title: {article['title']}\n")
        else:
            print(f"Failed to fetch news: {data.get('message', 'Unknown error')}")
    else:
        #Let OpenAI handle the rest of the things
        pass



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

