from binascii import a2b_base64
from re import A
from struct import pack
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks
import turtle 
import tkinter as tk
from math import *
from random import *


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


                       

#Harjutus. Lipud
#Eesti lipp

def eesti ():
    nupp.configure()
    raam.create_rectangle(300,100, 30,30, fill="blue")
    raam.create_rectangle(300,100, 30,60, fill="black")
    raam.create_rectangle(300,100, 30,130, fill="white")
def Bahama ():
    nupp.configure()
    raam.create_rectangle(310,100, 550,30,fill="#0fb8a1" )  
    raam.create_rectangle(310,100, 550,60,fill="#c9c310" )  
    raam.create_rectangle(310,100, 550,130,fill="#0fb8a1" ) 
    raam.create_polygon(310,30, 310,130, 400,80, fill="black" ) 
def Litva ():
    nupp.configure()
    raam.create_rectangle(600,100, 800,30, fill="yellow")
    raam.create_rectangle(600,100, 800,60, fill="#026b12")
    raam.create_rectangle(600,100, 800,130, fill="red")

raam=Tk()
raam.title("Tahvel")
tahvel=Canvas(raam, width=600,height=600, background="white")
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


#Create Chess Board
t= turtle.Turtle()
t.pensize(2)
t.speed(0)
def draw_square():
    for i in range(4):
        t.forward(40)
        t.right(90)
    t.forward(40)
for i in range(8):
    t.penup()
    t.goto(0, 40* i)
    t.pendown()
    for x in range(8):
        if (x+i) % 2==0:
            color="black"
        else:
            color="white"
        t.fillcolor(color)
        t.begin_fill()
        draw_square()
        t.end_fill()
t.hideturtle()
turtle.done()








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

nupp4=draw_square(aken,
            text="valgusfoor",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="green",
            activeforeground="red",
            height=3,    
            width=20,
            command=draw_square)





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


nupp4.pack()
nupp3.pack()
nupp2.pack()
nupp.pack()
raam.pack()
aken.mainloop()
root.mainloop()



