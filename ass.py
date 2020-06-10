from commands1 import commander
# from pygame.mixer import *
from pygame import mixer 
from googletrans import Translator
import speech_recognition as sr
# speech recognizer
r=sr.Recognizer()
# pre_init()
mixer.init()
running=True
translator = Translator()
cmd=commander()
def initSpeech():
    print("Listening...")
    # mixer.init()
    # mixer.music.load('C:\Users\Admin\Desktop\Python_Example\Project\coins.mp3')
    
    with sr.Microphone() as source:
        print("Please wait calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)
        # mixer.music.play()
        print("Say Something")
        audio=r.listen(source)
    # mixer.music.load('C:\Users\Admin\Desktop\Python_Example\Project\end.mp3')
    # mixer.music.play()
    try:
        command=r.recognize_google(audio,language="en-US") #ur-PK
    except:
        print("Couldn't understand you")

    print("Your command: ",end="")
    print(command)
    command=translator.translate(command)
    #print(command.text)
    cmd.discover(command.text)
    if command.text in ["quit","bye","Good Bye","goodbye","exit","see you","اللہ حافظ"]:
            global running
            running=False
    print("\n")
    
while running==True:
    initSpeech()    
