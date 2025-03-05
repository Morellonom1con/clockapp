import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import time
import datetime
import pygame

def check_alarm():
    alarm_time = entry.get()
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Time's up!")
            pygame.mixer.init()
            pygame.mixer.music.load("alarm_sound.mp3") 
            pygame.mixer.music.play()
            break
        time.sleep(1)

def openfile():
    filepath=filedialog.askopenfilename(intitialdir="/home/bhargav/Downloads",title="Choose Alarm Sound",filetypes=(("audio files",".mp3"),("audio files",".m4a")))
    file=open(filepath,'r')
    file.close()

def increment_time(t):
    if t==1:
        hour1=h1.cget("text")
        hour1=int(hour1)
        if hour1<2:
            hour1+=1
        else:
            hour1=0
        h1.config(text=str(hour1))
    elif t==2:
        hour2=h2.cget("text")
        hour1=h1.cget("text")
        hour2=int(hour2)
        hour1=int(hour1)
        if hour1<2:
            if hour2<9:
                hour2+=1
            else:
                hour2=0
        else:
            if hour2<3:
                hour2+=1
            else:
                hour2=0
                hour1=0
        h2.config(text=str(hour2))
        h1.config(text=str(hour1))
    elif t==3:
        min1=m1.cget("text")
        min1=int(min1)
        if min1<6:
            min1+=1
        else:
            min1=0
        m1.config(text=str(min1))
    elif t==4:
        min2=m2.cget("text")
        min1=m1.cget("text")
        min2=int(min2)
        min1=int(min1)
        if min1<6:
            if min2<9:
                min2+=1
            else:
                min2=0
        else:
            if min2<9:
                min2+=1
            else:
                min2=0
                min1=0
        m2.config(text=str(min2))
        m1.config(text=str(min1))
    return

def decrement_time(t):
    if t==1:
        hour1=h1.cget("text")
        hour1=int(hour1)
        if hour1>0:
            hour1-=1
        else:
            hour1=2
        h1.config(text=str(hour1))
    elif t==2:
        hour2=h2.cget("text")
        hour1=h1.cget("text")
        hour2=int(hour2)
        hour1=int(hour1)
        if hour1>0:
            if hour2>0:
                hour2-=1
            else:
                hour2=9
        else:
            if hour2>0:
                hour2-=1
            else:
                hour2=3
                hour1=2
        h2.config(text=str(hour2))
        h1.config(text=str(hour1))
    elif t==3:
        min1=m1.cget("text")
        min1=int(min1)
        if min1<6:
            min1+=1
        else:
            min1=0
        m1.config(text=str(min1))
    elif t==4:
        min2=m2.cget("text")
        min1=m1.cget("text")
        min2=int(min2)
        if min1<6:
            if min2<9:
                min2+=1
            else:
                min2=0
        else:
            if min2<9:
                min2+=1
            else:
                min2=0
                min1=0
        m2.config(text=str(min2))
        m1.config(text=str(min1))
    return
        

new_alarm=tk.Tk()
new_alarm.title("Create new Alarm")
new_alarm.geometry("400x400")

plus_button1 =ttk.Button(new_alarm,text="+",command=lambda: increment_time(1))
plus_button1.grid(row=3, column=2)
plus_button2 =ttk.Button(new_alarm,text="+",command=lambda: increment_time(2))
plus_button2.grid(row=3, column=3)
plus_button3 =ttk.Button(new_alarm,text="+",command=lambda: increment_time(3))
plus_button3.grid(row=3, column=4)
plus_button4 =ttk.Button(new_alarm,text="+",command=lambda: increment_time(4))
plus_button4.grid(row=3, column=5)

h1 = ttk.Label(new_alarm,text="0", font=("Arial", 14))
h1.grid(row=4,column=2)
h2 = ttk.Label(new_alarm,text="0", font=("Arial", 14))
h2.grid(row=4,column=3)
m1 = ttk.Label(new_alarm,text="0", font=("Arial", 14))
m1.grid(row=4,column=4)
m2 = ttk.Label(new_alarm,text="0", font=("Arial", 14))
m2.grid(row=4,column=5)

minus_button1 =ttk.Button(new_alarm,text="-",command=lambda: decrement_time(1))
minus_button1.grid(row=5, column=2)
minus_button2 =ttk.Button(new_alarm,text="-",command=lambda: decrement_time(2))
minus_button2.grid(row=5, column=3)
minus_button3 =ttk.Button(new_alarm,text="-",command=lambda: decrement_time(3))
minus_button3.grid(row=5, column=4)
minus_button4 =ttk.Button(new_alarm,text="-",command=lambda: decrement_time(4))
minus_button4.grid(row=5, column=5)


new_alarm.mainloop()