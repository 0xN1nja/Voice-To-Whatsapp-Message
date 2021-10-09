import pyttsx3
import speech_recognition as sr
import pywhatkit as pwk

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(string: str):
    engine.say(string)
    engine.runAndWait()


def listen(listening="Listening..."):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(listening)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You Said {query}")
        except Exception:
            print("Can't Hear You!")
            return "None"
        return query


def send_msg(number: str, message: str, hour: int, minute: int):
    pwk.sendwhatmsg(number, message, hour, minute)


if __name__ == '__main__':
    while True:
        query = listen()
        if "hello" in query:
            speak("hi")
        if "send message" in query:
            speak("Enter Number")
            number = input("Enter Number : ")
            speak("Speak Message")
            message = listen("Speak Your Message...")
            speak("Tell Hour")
            hour = listen("Speak Hour...")
            speak("Tell Minute")
            minute = listen("Speak Minute...")
            send_msg(number, message, int(hour), int(minute))
            speak("Message Sent")
            print("Message Was Sent Successfully!")
