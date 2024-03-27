import speech_recognition as sr
import pyttsx3
import googletrans
from googletrans import Translator



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
translator=Translator()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)



    if 'hello' in command:
        talk('Hi!')
    elif 'how are you doing' in command:
        talk('I am doing good! Thanks for asking!')
    elif 'bye' in command:
        quit
    elif 'translate' in command:
        talk("in which language you want to translate press press 1 for hindi,2 for gujarati,3 for spanish , 4 for french")
        language=int(input("language you want to translate to:"))
        if language==1:
            talk("what is the sentence:")
            hin=input("Enter sentence:")
            out1=translator.translate(hin, dest="hi")
            talk("the translation is")
            talk(out1.text)
            print(out1.text)
        elif language==2:
            talk("what is the sentence:")
            guj=input("Enter sentence:")
            out2=translator.translate(guj, dest="gu")
            talk("the translation is")
            talk(out2.text)
            print(out2.text)
        elif language==3:
            talk("what is the sentence:")
            spa=input("Enter sentence:")
            out3=translator.translate(spa, dest="es")
            talk("the translation is")
            talk(out3.text)
            print(out3.text)
        elif language==4:
            talk("what is the sentence:")
            fre=input("Enter sentence:")
            out4=translator.translate(fre, dest="fr")
            talk("the translation is")
            talk(out4.text)
            print(out4.text)
    else:
        talk('Please say the command again.')



while True:
    run_alexa()