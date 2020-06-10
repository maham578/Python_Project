import time
from time import ctime
import os
import webbrowser
import pyttsx3
from bs4 import BeautifulSoup
import requests
firefox_path="C:\Program Files\Mozilla Firefox\firefox.exe"
webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(firefox_path))
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait as wait
# from selenium.webdriver.support import expected_conditions as EC
from pygame.mixer import *
engine=pyttsx3.init()
engine.setProperty('rate',180)
class commander:
    def __init__(self):
        pass

    def discover(self,text):
        if "your name" in text:
            self.respond("I am Faheem Uz Zaman's personal assistant")
            self.respond("You can call me python commander")
        elif "functions" in text:
            self.respond("I can tell time, open apps from your computer, show you maps, play songs")
            self.respond("and the best thing is I can fetch information from google") 
        elif text in ["quit","bye","Good Bye","goodbye","exit","see you","اللہ حافظ"]:
            self.respond("Allah Hafiz")
        elif "time" in text:
            self.respond(ctime())
        elif "where is" in text:
            location=text.split(" ",2)
            location=location[2]
            self.respond("Hold on Faheem, I will show you where " + location + " is.")
            url="https://www.google.com/maps/place/"+location            
            webbrowser.get('firefox').open(url)
            time.sleep(10)
        else:
            self.respond("Fetching information from google")
            search=text.replace(" ","+")
            link="https://www.google.com/search?q="+search
            headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
            source=requests.get(link,headers=headers).text
            soup=BeautifulSoup(source,"html.parser")
            
            try:
                answer=soup.find('div',class_="Z0LcW")
                self.respond(answer.text)
            except:
                self.respond("I dont Know")

    def respond(self,response):
        print(response)
        engine.say(response)
        engine.runAndWait()
         
            
