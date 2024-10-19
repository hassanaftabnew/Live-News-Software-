# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:22:41 2023

@author: hassan
"""

from bs4 import BeautifulSoup
import requests
import time
import keyboard
import tkinter as Tk
from tkinter import*
from tkinter import PhotoImage
from tkinter import Frame
from tkinter import GROOVE
from tkinter import Label
from tkinter import LabelFrame
from tkinter import Text
from tkinter import VERTICAL
from tkinter import END
from tkinter import RIGHT
from tkinter import BOTH
from tkinter import X
from tkinter import Y
from tkinter import Button
import webbrowser
from pathlib import Path
import sys
##################################################################
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

############################################################
web = ["https://www.google.com/search?client=firefox-b-d&sca_esv=596768218&q=tennis&tbm=nws&source=lnms&sa=X&ved=2ahUKEwjtsePsw8-DAxUe9AIHHWEYDrIQ0pQJegQIDhAB&biw=1366&bih=643&dpr=1",
       "https://www.google.com/search?q=golf&client=firefox-b-d&sca_esv=596768218&biw=1366&bih=643&tbm=nws&ei=vNOcZdyPFPO8i-gP9O2NqAg&ved=0ahUKEwjc3dHuw8-DAxVz3gIHHfR2A4UQ4dUDCA0&uact=5&oq=golf&gs_lp=Egxnd3Mtd2l6LW5ld3MiBGdvbGYyChAAGIAEGAoYsQMyChAAGIAEGAoYsQMyChAAGIAEGAoYsQMyChAAGIAEGAoYsQMyChAAGIAEGAoYsQMyChAAGIAEGAoYsQMyBhAAGAMYCjIGEAAYAxgKMhAQABiABBiKBRgKGLEDGIMBMg0QABiABBgKGLEDGIMBSIBzUL0aWI9QcAF4AJABAZgBiw-gAY45qgENMi0yLjUtMi40LjAuMbgBA8gBAPgBAagCAMICEBAAGIAEGIoFGEMYsQMYgwHCAggQABiABBixA8ICCxAAGIAEGLEDGIMBwgIFEAAYgATCAgoQABiABBiKBRhDwgINEAAYgAQYigUYQxixA8ICBBAAGAOIBgE&sclient=gws-wiz-news",
       "https://www.google.com/search?q=basketball&client=firefox-b-d&sca_esv=596768218&biw=1366&bih=643&tbm=nws&ei=INScZdiHPLDui-gPnqSm8Ac&oq=basket&gs_lp=Egxnd3Mtd2l6LW5ld3MiBmJhc2tldCoCCAAyDRAAGIAEGIoFGEMYsQMyDRAAGIAEGIoFGEMYsQMyDRAAGIAEGIoFGEMYsQMyDRAAGIAEGIoFGEMYsQMyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwFI0i9Q9gNYuCVwAXgAkAEAmAH1AqABiROqAQcwLjIuOC4xuAEDyAEA-AEBqAIAwgIKEAAYgAQYChixA8ICBhAAGAMYCsICEBAAGIAEGIoFGAoYsQMYgwHCAgoQABiABBiKBRhDwgIFEAAYgATCAhAQABiABBiKBRhDGLEDGIMBwgINEAAYgAQYChixAxiDAYgGAQ&sclient=gws-wiz-news",
       "https://www.google.com/search?q=cricket+news&client=firefox-b-d&sca_esv=596768218&hl=en&biw=1366&bih=643&tbm=nws&ei=gNmcZarJAu_si-gPr-axuAM&ved=0ahUKEwiqiaiuyc-DAxVv9gIHHS9zDDcQ4dUDCA0&uact=5&oq=cricket+news&gs_lp=Egxnd3Mtd2l6LW5ld3MiDGNyaWNrZXQgbmV3czIOEAAYgAQYigUYkQIYsQMyCxAAGIAEGIoFGJECMg4QABiABBiKBRiRAhixAzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI1hBQggNY9Q1wAHgAkAEAmAHMAaABngmqAQUwLjQuMrgBA8gBAPgBAcICEBAAGIAEGIoFGEMYsQMYgwHCAg0QABiABBiKBRhDGLEDwgIIEAAYgAQYsQPCAgoQABiABBiKBRhDiAYB&sclient=gws-wiz-news",
       "https://www.google.com/search?q=squash&client=firefox-b-d&sca_esv=596768218&biw=1366&bih=643&tbm=nws&ei=ctScZaX2JZaK9u8Poe-0-AE&ved=0ahUKEwil98fFxM-DAxUWhf0HHaE3DR8Q4dUDCA0&uact=5&oq=squash&gs_lp=Egxnd3Mtd2l6LW5ld3MiBnNxdWFzaDINEAAYgAQYigUYQxixAzINEAAYgAQYigUYQxixAzINEAAYgAQYigUYQxixAzILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI6EBQ-gFY5DtwAHgAkAEAmAGJA6ABxhmqAQgwLjEyLjEuMrgBA8gBAPgBAagCAMICCxAAGIAEGIoFGJECwgIOEAAYgAQYigUYsQMYgwHCAgoQABiABBiKBRhDwgIQEAAYgAQYigUYQxixAxiDAYgGAQ&sclient=gws-wiz-news",
       "https://www.google.com/search?q=rugby&client=firefox-b-d&sca_esv=596768218&biw=1366&bih=643&tbm=nws&ei=tdScZbehNI6Ni-gPuqq8sAs&ved=0ahUKEwj3z8_lxM-DAxWOxgIHHToVD7YQ4dUDCA0&uact=5&oq=rugby&gs_lp=Egxnd3Mtd2l6LW5ld3MiBXJ1Z2J5Mg0QABiABBiKBRhDGLEDMgoQABiABBiKBRhDMg0QABiABBiKBRhDGLEDMgoQABiABBiKBRhDMgoQABiABBiKBRhDMggQABiABBixAzILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgUQABiABDIFEAAYgARIgeQDUPsBWJLaA3ABeACQAQCYAccBoAHuEaoBBDAuMTK4AQPIAQD4AQGoAgDCAg4QABiABBiKBRixAxiDAcICCxAAGIAEGIoFGLEDwgIQEAAYgAQYigUYQxixAxiDAYgGAQ&sclient=gws-wiz-news",
       "https://www.google.com/search?q=baseball&client=firefox-b-d&sca_esv=596768218&biw=1366&bih=643&tbm=nws&ei=F9WcZannObD2i-gPocSOmAg&oq=base&gs_lp=Egxnd3Mtd2l6LW5ld3MiBGJhc2UqAggAMg0QABiABBiKBRhDGLEDMgoQABiABBiKBRhDMhAQABiABBiKBRhDGLEDGIMBMg4QABiABBiKBRixAxiDATIIEAAYgAQYsQMyDhAAGIAEGIoFGLEDGIMBMggQABiABBixAzIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDAUj_LVCwAliTG3ABeACQAQCYAZ0CoAHND6oBBTAuOC4yuAEDyAEA-AEBqAIAwgIFEAAYgASIBgE&sclient=gws-wiz-news"]
news_results = []
link = []
a = 0
while a <= 6:
    response = requests.get(web[a], headers=headers)
    text1 = BeautifulSoup(response.content, "html.parser")
    a = a+1
    for el in text1.select("div.SoaBEf"):
        news_results.append(el.select_one("div.MBeuO").get_text())
        news_results.append('\n')
        news_results.append(el.select_one(".LfVVr").get_text())
        link.append(el.find("a")["href"])
################################################################
with open('log News software.txt', "a", encoding="utf-8") as v:
    v.write(str(news_results))
v.close()
type = 'tennis'
apiKey = 'YOUR_API_KEY_HERE'
global o
o=0
q=[]
class NewsApp:
    global apiKey
    global o
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700')
        self.root.title("Live News")
        self.display = []
        Sports = ["Tennis", "Golf", "Basketball",
                    "Cricket", "Squash", "Rugby",  "Baseball"]
        bg_color = "#007FFF"
        text_area_bg = "#000000"
        basic_font_color = "#FFEBCD"
        def exi():
            global o
            o=1;
        def webone():
            webbrowser.open(link[z])
            time.sleep(3)
        def webtwo():
            webbrowser.open(link[z+1])
            time.sleep(3)
        def webthree():
            webbrowser.open(link[z+2])
            time.sleep(3)
        def webfour():
            webbrowser.open(link[z+3]) 
            time.sleep(3)
        def webfive():
            webbrowser.open(link[z+4])
            time.sleep(3)
        def websix():
            webbrowser.open(link[z+5])
            time.sleep(3)
        def webseven():
            webbrowser.open(link[z+6])
            time.sleep(3)
        def webeight():
            webbrowser.open(link[z+7])
            time.sleep(3)
        F2 = Frame(self.root, bd=7, relief=GROOVE)
        F3 = Frame(self.root, bd=7, relief=GROOVE)
        F4 = Frame(self.root, bd=7, relief=GROOVE)
        F5 = Frame(self.root, bd=7, relief=GROOVE)
        F6 = Frame(self.root, bd=7, relief=GROOVE)
        F7 = Frame(self.root, bd=7, relief=GROOVE)
        F8 = Frame(self.root, bd=7, relief=GROOVE)
        F9 = Frame(self.root, bd=7, relief=GROOVE)
        F10 = Frame(self.root, bd=7, relief=GROOVE)
        F2.place(x=100, y=80, relwidth=0.85, relheight=0.07)
        F3.place(x=100, y=130, relwidth=0.85, relheight=0.10)
        F4.place(x=100, y=200, relwidth=0.85, relheight=0.10)
        F5.place(x=100, y=270, relwidth=0.85, relheight=0.10)
        F6.place(x=100, y=340, relwidth=0.85, relheight=0.10)
        F7.place(x=100, y=410, relwidth=0.85, relheight=0.10)
        F8.place(x=100, y=480, relwidth=0.85, relheight=0.10)
        F9.place(x=100, y=550, relwidth=0.85, relheight=0.10)
        F10.place(x=100, y=620, relwidth=0.85, relheight=0.10)
        F11 = Button(self.root, text='Exit', bd=7, relief=GROOVE, command=exi)
        F12 = Button(self.root, text='Link', bd=7, relief=GROOVE, command=webone)
        F13 = Button(self.root, text='Link', bd=7, relief=GROOVE, command=webtwo)
        F14 = Button(self.root, text='Link', bd=7, relief=GROOVE, command=webthree)
        F15 = Button(self.root, text='Link', bd=7, relief=GROOVE, command=webfour)
        F16 = Button(self.root, text='Link', bd=7, relief=GROOVE, command=webfive)
        F17 = Button(self.root, text='Link', bd=7, relief=GROOVE, command=websix)
        F18 = Button(self.root, text='Link', bd=7, relief=GROOVE, command=webseven)
        F19 = Button(self.root, text='Link', bd=7, relief=GROOVE, command=webeight)
        F11.place(x=1140, y=75, relwidth=0.08, relheight=0.07)
        F12.place(x=1140, y=135, relwidth=0.08, relheight=0.07)
        F13.place(x=1140, y=205, relwidth=0.08, relheight=0.07)
        F14.place(x=1140, y=275, relwidth=0.08, relheight=0.07)
        F15.place(x=1140, y=345, relwidth=0.08, relheight=0.07)
        F16.place(x=1140, y=415, relwidth=0.08, relheight=0.07)
        F17.place(x=1140, y=485, relwidth=0.08, relheight=0.07)
        F18.place(x=1140, y=555, relwidth=0.08, relheight=0.07)
        F19.place(x=1140, y=625, relwidth=0.08, relheight=0.07)
        news_title = Label(F2, text=Sports[b], font=("arial", 20, "bold"), bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea2 = Text(F2, font=("times new roman", 16, "bold"), bg=text_area_bg, fg="#FFEBCD")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea2.yview)
        self.txtarea2.pack(fill=BOTH, expand=1)
        self.txtarea3 = Text(F3, font=("times new roman", 16, "bold"), bg=text_area_bg, fg="#FFEBCD")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea3.yview)
        self.txtarea3.pack(fill=BOTH, expand=1)
        self.txtarea4 = Text(F4, font=("times new roman", 16, "bold"), bg=text_area_bg, fg="#FFEBCD")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea4.yview)
        self.txtarea4.pack(fill=BOTH, expand=1)
        self.txtarea5 = Text(F5, font=("times new roman", 16, "bold"), bg=text_area_bg, fg="#FFEBCD")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea5.yview)
        self.txtarea5.pack(fill=BOTH, expand=1)
        self.txtarea6 = Text(F6, font=("times new roman", 16, "bold"), bg=text_area_bg, fg="#FFEBCD")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea6.yview)
        self.txtarea6.pack(fill=BOTH, expand=1)
        self.txtarea7 = Text(F7, font=("times new roman", 16, "bold"), bg=text_area_bg, fg="#FFEBCD")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea7.yview)
        self.txtarea7.pack(fill=BOTH, expand=1)
        self.txtarea8 = Text(F8, font=("times new roman", 16, "bold"), bg=text_area_bg, fg="#FFEBCD")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea8.yview)
        self.txtarea8.pack(fill=BOTH, expand=1)
        self.txtarea9 = Text(F9, font=("times new roman", 16, "bold"), bg=text_area_bg, fg="#FFEBCD")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea9.yview)
        self.txtarea9.pack(fill=BOTH, expand=1)
        self.txtarea10 = Text(F10, font=("times new roman", 16, "bold"), bg=text_area_bg, fg="#FFEBCD")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea10.yview)
        self.txtarea10.pack(fill=BOTH, expand=1)
        title = Label(self.root, text="Live News Software", font=("times new roman", 30, "bold"), pady=2, bd=12, relief=GROOVE, bg=bg_color, fg=basic_font_color).pack(fill=X)
        self.txtarea3.insert("1.0", news_results[c].replace("\n", ""), "1.0", news_results[c+1], "end", news_results[c+2])
        self.txtarea4.insert("1.0", news_results[c+3].replace("\n", ""), "1.0", news_results[c+4], "end", news_results[c+5])
        self.txtarea5.insert("1.0", news_results[c+6].replace("\n", ""), "1.0", news_results[c+7], "end", news_results[c+8])   
        self.txtarea6.insert("1.0", news_results[c+9].replace("\n", ""), "1.0", news_results[c+10], "end", news_results[c+11]) 
        self.txtarea7.insert("1.0", news_results[c+12].replace("\n", ""), "1.0", news_results[c+13], "end", news_results[c+14])
        self.txtarea8.insert("1.0", news_results[c+15].replace("\n", ""), "1.0", news_results[c+16], "end", news_results[c+17])
        self.txtarea9.insert("1.0", news_results[c+18].replace("\n", ""), "1.0", news_results[c+19], "end", news_results[c+20])
        self.txtarea10.insert("1.0", news_results[c+21].replace("\n", ""), "1.0", news_results[c+22], "end", news_results[c+23])
        # h[b].write(news_results)

        # def CallBack():
        #     webbrowser.open(link[1])
        # B = Button(top, text="Hello", command=CallBack)
        # B.place(x=50, y=50)


b = 0
c = 0
z = 0
while b <= 6:
    if o==1:
        break
    if (b == 6):
        b = -1
        c = 0
        z = 0
    b = b+1
    if (b != 0):
        c = c+30
        z = z+10 
    root = Tk()
    obj = NewsApp(root)
    root.after(40000, root.destroy)    
    root.mainloop()
    
