import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import time
import datetime
import pygame
import json

json_file_path="alarms.json"

def check_alarm():
    alarm_time = ttk.entry.get()
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
    filepath=filedialog.askopenfilename(initialdir="/home/bhargav/Downloads",title="Choose Alarm Sound",filetypes=(("mp3 files","*.mp3"),("all files","*.*")))
    if filepath!="":
        audio_file_label.config(text=filepath)
    return

def increment_time(t):
    if t==1:
        hour1=h1.cget("text")
        hour1=int(hour1)
        hour2=h2.cget("text")
        hour2=int(hour2)
        if hour1<2:
            if hour2<3:
                hour1+=1
            elif hour1==1:
                hour1=2
                hour2=3
            else:
                hour1+=1
        else:
            hour1=0
        h1.config(text=str(hour1))
        h2.config(text=str(hour2))
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
        if min1<5:
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
                min1=0
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
        hour2=h2.cget("text")
        hour2=int(hour2)
        if hour1>0:
            hour1-=1
        else:
            if hour2>3:
                hour1=2
                hour2=3
            else:
                hour1=2
        h1.config(text=str(hour1))
        h2.config(text=str(hour2))
    elif t==2:
        hour2=h2.cget("text")
        hour1=h1.cget("text")
        hour2=int(hour2)
        hour1=int(hour1)
        if hour1<2:
            if hour2>0:
                hour2-=1
            else:
                hour2=9
        else:
            if hour2>0:
                hour2-=1
            else:
                hour2=3                      
        h2.config(text=str(hour2))
        h1.config(text=str(hour1))
    elif t==3:
        min1=m1.cget("text")
        min1=int(min1)
        if min1>0:
            min1-=1
        else:
            min1=5
        m1.config(text=str(min1))
    elif t==4:
        min2=m2.cget("text")
        min1=m1.cget("text")
        min2=int(min2)
        min1=int(min1)
        if min1>0:
            if min2>0:
                min2-=1
            else:
                min2=9
        else:
            if min2>0:
                min2-=1
            else:
                min2=9
                min1=5
        m2.config(text=str(min2))
        m1.config(text=str(min1))
    return
        
def save_alarm():
    hour1=h1.cget("text")
    hour2=h2.cget("text")
    min1=m1.cget("text")
    min2=m2.cget("text")
    name=namebox.get()
    audio_file=audio_file_label.cget("text")
    save_entry={"hour1":hour1,"hour2":hour2,"min1":min1,"min2":min2,"name":name,"audio_file":audio_file}
    with open(json_file_path, "r") as file:
        data = json.load(file)
        if "alarms" not in data:
            data["alarms"] = []
        data["alarms"].append(save_entry)
        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=4)
    successful_save.deiconify()
    return

new_alarm=tk.Tk()
new_alarm.title("Create new Alarm")
new_alarm.geometry("400x300")

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

namebox=ttk.Entry(new_alarm,textvariable="Name", font=("Arial", 14))
namebox.grid(row=6,column=3,columnspan=2)

audio_file_label=ttk.Label(new_alarm,text="Audio File")
audio_file_label.grid(row=7,column=2,columnspan=2)
audio_file_button=ttk.Button(new_alarm,text="Choose Audio File",command=openfile)
audio_file_button.grid(row=7,column=4,columnspan=1)

save_button=ttk.Button(new_alarm,text="Save Alarm", command=save_alarm)
save_button.grid(row=8,column=3,columnspan=2)

successful_save=tk.Toplevel(new_alarm)
successful_save.title("")
successful_save.geometry("200x100")
successful_save_label=ttk.Label(successful_save,text="Alarm Saved Successfully")
successful_save_label.pack()
successful_save_button=ttk.Button(successful_save,text="OK",command=successful_save.destroy)
successful_save_button.pack()
successful_save.withdraw()

new_alarm.mainloop()