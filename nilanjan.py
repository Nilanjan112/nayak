import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import calendar

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)  
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
def wishMe():
      hour = int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
          speak("Good Morning!")
      
      elif hour>=12 and hour<18:
          speak("Good Afternoon!")

      else:
        speak("Good Evening!")
      speak("hellow Mr. Nilanjan,i am star , how can i help you sir ")


def takecommand():
     r=sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio=r.listen(source)
     try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
     except Exception as e:
        #print(e)
         print("Say that again please...")
         return "None"
     return query

if __name__ == '__main__':
        wishMe()
        #while True:
        if 2:
            query = takecommand().lower()
            #logic for
            if 'wikipedia' in query:
                speak('searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to Wikipedia")
                print(results)
                speak(results)
            elif 'open calendar'in query:
             now = datetime.datetime.now()
             print(calendar.month(int(now.strftime("%Y")), int(now.strftime("%m"))))
             #print(calendar.calendar(int(now.strftime("%Y"))))
            elif 'open youtube' in query:
             webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open facebook' in query:
                webbrowser.open("facebook.com")
            elif 'open whatsapp' in query:
                webbrowser.open("whatsapp.com")
        

