from tkinter import *
from math import *
from random import *
import tkinter as tk


#____________________________________________________

def valgusfoor():
    tahvel=Tk()
    tahvel.title("Tahvel")
    tahv=Canvas(tahvel,width=600,height=600,background="grey")

    tahv.create_rectangle(100,570,  500,580, fill="black")
    tahv.create_rectangle(290,560,  300,320, fill="black")
    red_light=tahv.create_rectangle(250,240,  340,310,outline="Black", fill="grey")
    yellow_light=tahv.create_rectangle(250,160,  340,230,outline="Black", fill="grey")
    green_light=tahv.create_rectangle(250,80,  340,150,outline="Black", fill="grey")
    tahv.grid()

    def switch():
        if var.get() == 1:
            tahv.itemconfig(red_light, fill='red')
            tahv.itemconfig(yellow_light, fill='black')
            tahv.itemconfig(green_light, fill='black')
        elif var.get() == 2:
            tahv.itemconfig(red_light, fill='black')
            tahv.itemconfig(yellow_light, fill='yellow')
            tahv.itemconfig(green_light, fill='black')
        else:
            tahv.itemconfig(red_light, fill='black')
            tahv.itemconfig(yellow_light, fill='black')
            tahv.itemconfig(green_light, fill='green')
    return switch



    #Create Chess Board
def board():
    tahvel=Tk()
    tahvel.tittle("Tahvel")
    tahvel=Canvas(tahvel,width=600,height=600)
    color="white"
    for y in range(8):
        for x in range(8):
            x1=x*70
            y1=y*70
            x2=x1+70
            y2=y1+70 
            tahvel.create_rectangle((x1,y1,x2,y2), fill=color)
            if color=="white":
                color="black"
            else:
                color="white"
        if color=="white":
            color="white"
        else:
            color="white"
        tahvel.grid()


#____________________________________________________
            

#Harjutus. Lipp
#Eesti lipp
def eesti ():
    nupp.configure()
    tahvel.tittle("Tahvel")
    tahvel=Canvas(tahvel,width=600,height=600)
    tahvel.create_rectangle(300,100, 30,30, fill="blue")
    tahvel.create_rectangle(300,100, 30,60, fill="black")
    tahvel.create_rectangle(300,100, 30,130, fill="white")
    tahvel.grid()
def Bahama ():
    nupp.configure()
    tahvel.tittle("Tahvel")
    tahvel=Canvas(tahvel,width=600,height=600)
    tahvel.create_rectangle(310,100, 550,30,fill="#0fb8a1" )  
    tahvel.create_rectangle(310,100, 550,60,fill="#c9c310" )  
    tahvel.create_rectangle(310,100, 550,130,fill="#0fb8a1" ) 
    tahvel.create_polygon(310,30, 310,130, 400,80, fill="black" ) 
    tahvel.grid()
def Litva ():
    nupp.configure()
    tahvel.tittle("Tahvel")
    tahvel=Canvas(tahvel,width=600,height=600)
    tahvel.create_rectangle(600,100, 800,30, fill="yellow")
    tahvel.create_rectangle(600,100, 800,60, fill="#026b12")
    tahvel.create_rectangle(600,100, 800,130, fill="red")
    tahvel.grid()
    

#____________________________________________________


tekst="Aken"
aken=Tk()
aken.geometry("300x200")  #разрешение экрана
aken.title(tekst)          #заголовок


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
#____________________________________________________
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


#____________________________________________________

# Создаем окно
tahvel=Tk()
tahvel.tittle("Tahvel")
tahvel=Canvas(tahvel, width=600,height=600, background="white")


# Создаем canvas для отображения светофора
canvas = tk.Canvas(width=100, height=250)
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
#____________________________________________________

tahvel=Tk()
tahvel.tittle("Tahvel")
nupp=Button(tahvel,
            text="Eesti lipp",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="green",
            activeforeground="red",
            height=3,    
            width=20,
            command=eesti)

nupp2=Button(tahvel,
            text="Bahama lipp",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="blue",
            activeforeground="red",
            height=3,    
            width=20,
            command=Bahama)

nupp3=Button(tahvel,
            text="Litva lipp",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="blue",
            activeforeground="red",
            height=3,    
            width=20,
            command=Litva)
raam=Canvas(tahvel,
            width=800,
            height=621,
            bg="white",)
   



nupp=Radiobutton(tahvel,text="Eesti lipp",command=eesti)
nupp2=Radiobutton(tahvel,text="Bahama lipp",command=Bahama)
nupp3=Radiobutton(tahvel,text="Litva lipp",command=Litva)
nupp4=Radiobutton(tahvel,text="Tahvel",command=board)
nupp5=Radiobutton(tahvel,text="Ringid",command=oval)

nupp4.grid(row=1,column=1)
nupp3.grid(row=2,column=1)
nupp2.grid(row=3,column=1)
nupp.grid(row=4,column=1)
raam.grid(row=5,column=1)
nupp5.grid(row=6,column=1)



tahvel.mainloop()




