from googletrans import Translator
from tkinter import *

def funcEnglish():
    lang = "en"
    srcdata=src.get()
    s=t.translate(srcdata,lang)
    destdata=s.text
    dest.set(destdata)

def funcHindi():
    lang = "Hi"
    srcdata = src.get()
    s = t.translate(srcdata, lang)
    destdata = s.text
    dest.set(destdata)

def funcPunjabi():
    lang = "pa"
    srcdata = src.get()
    s = t.translate(srcdata, lang)
    destdata = s.text
    dest.set(destdata)

def funcFrench():
    lang = "fr"
    srcdata = src.get()
    s = t.translate(srcdata, lang)
    destdata = s.text
    dest.set(destdata)

def funcGerman():
    lang = "de"
    srcdata = src.get()
    s = t.translate(srcdata, lang)
    destdata = s.text
    dest.set(destdata)

def funcRussian():
    lang = "ru"
    srcdata = src.get()
    s = t.translate(srcdata, lang)
    destdata = s.text
    dest.set(destdata)

root=Tk()
root.title("Language Translator by Himanshi")
root.geometry("900x700")
root["bg"]="orange"

lbl=Label(root)
lbl["text"]="Enter Text in Any Language"
lbl["font"]=20
lbl["width"]=83
lbl.grid(row=0,column=0,columnspan=4)
lbl.grid(pady=(20,10))

src=StringVar()
entMsg=Entry(root)
entMsg["textvariable"]=src
entMsg["font"]=1
entMsg["width"]=83
entMsg.grid(row=1,column=0,columnspan=4)
entMsg.grid(pady=(10,50))

btnEnglish=Button(root)
btnEnglish["text"]="English"
btnEnglish["font"]=20
btnEnglish["bg"]="yellow"
btnEnglish["width"]=20
btnEnglish["height"]=3
btnEnglish["command"]=funcEnglish
btnEnglish.grid(row=2,column=0)
btnEnglish.grid(padx=(30,15))

btnHindi=Button(root)
btnHindi["text"]="Hindi"
btnHindi["font"]=20
btnHindi["bg"]="yellow"
btnHindi["width"]=20
btnHindi["height"]=3
btnHindi["command"]=funcHindi
btnHindi.grid(row=2,column=1)
btnHindi.grid(padx=(15,15))

btnPunjabi=Button(root)
btnPunjabi["text"]="Punjabi"
btnPunjabi["font"]=20
btnPunjabi["bg"]="yellow"
btnPunjabi["width"]=20
btnPunjabi["height"]=3
btnPunjabi["command"]=funcPunjabi
btnPunjabi.grid(row=2,column=2)
btnPunjabi.grid(padx=(15,30))

btnFrench=Button(root)
btnFrench["text"]="French"
btnFrench["font"]=20
btnFrench["bg"]="yellow"
btnFrench["width"]=20
btnFrench["height"]=3
btnFrench["command"]=funcFrench
btnFrench.grid(row=3,column=0)
btnFrench.grid(pady=(40,20))
btnFrench.grid(padx=(30,15))

btnGerman=Button(root)
btnGerman["text"]="German"
btnGerman["font"]=20
btnGerman["bg"]="yellow"
btnGerman["width"]=20
btnGerman["height"]=3
btnGerman["command"]=funcGerman
btnGerman.grid(row=3,column=1)
btnGerman.grid(pady=(40,20))
btnGerman.grid(padx=(30,15))

btnRussian=Button(root)
btnRussian["text"]="Russian"
btnRussian["font"]=20
btnRussian["bg"]="yellow"
btnRussian["width"]=20
btnRussian["height"]=3
btnRussian["command"]=funcRussian
btnRussian.grid(row=3,column=2)
btnRussian.grid(pady=(40,20))
btnRussian.grid(padx=(30,15))

dest=StringVar()
entconvMsg=Entry(root,textvariable=dest,font=1,width=83)
entconvMsg.grid(row=4,column=0,columnspan=4)
entconvMsg.grid(pady=(50,20))
t = Translator()

root.mainloop()

