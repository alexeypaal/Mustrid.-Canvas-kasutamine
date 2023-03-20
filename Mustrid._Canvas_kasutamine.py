from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks

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


#Bahama lipp



nupp3.pack()
nupp2.pack()
nupp.pack()
raam.pack()
aken.mainloop()



