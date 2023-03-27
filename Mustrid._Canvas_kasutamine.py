from binascii import a2b_base64
from re import A
from struct import pack
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks
import turtle 
import tkinter as tk
from math import *
from random import *

#Harjutus. Lipud
#Eesti lipp
def eesti ():
    nupp.configure()
    aken.create_rectangle(300,100, 30,30, fill="blue")
    aken.create_rectangle(300,100, 30,60, fill="black")
    aken.create_rectangle(300,100, 30,130, fill="white")
def Bahama ():
    nupp.configure()
    aken.create_rectangle(310,100, 550,30,fill="#0fb8a1" )  
    aken.create_rectangle(310,100, 550,60,fill="#c9c310" )  
    aken.create_rectangle(310,100, 550,130,fill="#0fb8a1" ) 
    aken.create_polygon(310,30, 310,130, 400,80, fill="black" ) 
def Litva ():
    nupp.configure()
    aken.create_rectangle(600,100, 800,30, fill="yellow")
    aken.create_rectangle(600,100, 800,60, fill="#026b12")
    aken.create_rectangle(600,100, 800,130, fill="red")


    #Create Chess Board
def board():
    for y in range(8):
        for x in range(8):
            x1=x*70
            y1=y*70
            x2=x1+70 
            





aken=Tk()
aken.title("Tahvel")
tahvel=Canvas(aken, width=600,height=600, background="white")
k=7
x0=0
y0=0
x1=600
y1=600
a=300
r=(a**2+a**2)**(1/2)
p=(a-r)
for i in range(7):
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    tahvel.create_rectangle(x0,y0,x1,y1,width=1,outline="blue", fill="red")
    tahvel.create_oval(x0,y0,x1,y1,width=1,outline="blue", fill="yellow")
    p=r-a 
    r=r-p 
    a=((r)*sqrt(2))/2
tahvel.grid()

def oval():
    colors=["black",
        "cyan",
        "magenta",
        "red",
        "blue",
        "gray",
        "yellow",
        "green",
        "lightblue",
        "pink",
        "gold"]
    raam2 = Tk()
    raam2.title("Ringid")
    tahvel2 = Canvas(raam2 , width=600 , height=600 , background="white")
    x0=0
    y0=0
    x1=600
    y1=600
    p=5
    for i in range(55):
        x0+=p 
        y0+=p 
        x1-=p 
        y1-=p 
        tahvel2.create_oval(x0,y0,x1,y1, fill=choice(colors))
    tahvel2.grid()





tekst="Aken"
aken=Tk()
aken.geometry("800x900")
nupp=Button(aken,
            text="Eesti lipp",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="green",
            activeforeground="red",
            height=3,    
            width=20,
            command=eesti)

nupp2=Button(aken,
            text="Bahama lipp",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="blue",
            activeforeground="red",
            height=3,    
            width=20,
            command=Bahama)

nupp3=Button(aken,
            text="Litva lipp",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="blue",
            activeforeground="red",
            height=3,    
            width=20,
            command=Litva)
raam=Canvas(aken,
            width=800,
            height=621,
            bg="white",)
    


nupp4=board(aken,
            text="valgusfoor",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="green",
            activeforeground="red",
            height=3,    
            width=20,
            command=board)
nupp5=oval(aken,
            text="Ringid",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="green",
            activeforeground="red",
            height=3,    
            width=20,
            command=oval)





# Создаем окно
root = tk.Tk()
root.geometry("200x300")

# Создаем canvas для отображения светофора
canvas = tk.Canvas(root, width=100, height=250)
canvas.pack()

# Рисуем красный сигнал светофора
canvas.create_oval(25, 25, 75, 75, fill='gray', outline='')  # Основание
canvas.create_oval(30, 30, 70, 70, fill='red', outline='')  # Сигнал
canvas.create_polygon(48, 75, 52, 75, 50, 80, fill='red')  # Стрелка вниз

# Рисуем желтый сигнал светофора
canvas.create_oval(25, 100, 75, 150, fill='gray', outline='')  # Основание
canvas.create_oval(30, 105, 70, 145, fill='yellow', outline='')  # Сигнал
canvas.create_polygon(48, 150, 52, 150, 50, 155, fill='yellow')  # Стрелка вправо

# Рисуем зеленый сигнал светофора
canvas.create_oval(25, 175, 75, 225, fill='gray', outline='')  # Основание
canvas.create_oval(30, 180, 70, 220, fill='green', outline='')  # Сигнал
canvas.create_polygon(48, 225, 52, 225, 50, 220, fill='green')  # Стрелка вверх



nupp=Radiobutton(aken,text="Eesti lipp",command=eesti)
nupp2=Radiobutton(aken,text="Bahama lipp",command=Bahama)
nupp3=Radiobutton(aken,text="Litva lipp",command=Litva)
nupp4=Radiobutton(aken,text="valgusfoor",command=board)
nupp5=Radiobutton(aken,text="Ringid",command=oval)

nupp4.grid(row=1,column=1)
nupp3.grid(row=2,column=1)
nupp2.grid(row=3,column=1)
nupp.grid(row=4,column=1)
raam.grid(row=5,column=1)
nupp5.grid(row=6,column=1)



aken.mainloop()




