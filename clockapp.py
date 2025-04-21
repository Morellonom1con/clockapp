import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import time
import datetime
import pygame
import json
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

json_file_path="alarms.json"

def check_alarm():
    current_time = datetime.datetime.now().strftime("%H:%M")
    
    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)
            for alarm in data.get("alarms", []):
                alarm_time = f"{alarm['hour1']}{alarm['hour2']}:{alarm['min1']}{alarm['min2']}"
                alarm_state=alarm["state"]
                if current_time == alarm_time and alarm_state=="enabled":
                    pygame.mixer.init()
                    pygame.mixer.music.load(alarm["audio_file"])
                    pygame.mixer.music.play()
                    alarm["state"]="disabled"
                    with open(json_file_path,"w") as file:
                        json.dump(data,file,indent=4)
                    alarm_activated_window=tk.Toplevel(alarms_window)
                    alarm_activated_window.title("")
                    alarm_activated_window.geometry("200x100")
                    alarm_activated_window_label=ttk.Label(alarm_activated_window,text=f"Time's up for {alarm["name"]}")
                    alarm_activated_window_label.pack()
                    alarm_activated_window_button=ttk.Button(alarm_activated_window,text="OK",command=lambda : (alarm_activated_window.destroy(),pygame.mixer.music.stop(),pygame.mixer.music.unload()))
                    alarm_activated_window_button.pack()
                    alarm_activated_window.withdraw()
                    alarm_activated_window.deiconify()

                    
                        

    except FileNotFoundError:
        pass

    alarms_window.after(1000, check_alarm)

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
    save_entry={"hour1":hour1,"hour2":hour2,"min1":min1,"min2":min2,"name":name,"audio_file":audio_file,"state":"enabled"}
    with open(json_file_path, "r") as file:
        data = json.load(file)
        if "alarms" not in data:
            data["alarms"] = []
        data["alarms"].append(save_entry)
        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=4)
    successful_save.deiconify()
    return

def delete_alarm(alarm_frame):
    alarm_name,alarm_time,alarm_audio,_,state_box=alarm_frame.winfo_children()
    if state_box.state()=="selected":
        state="enabled"
    else:
        state="disabled"
    name=alarm_name.cget("text")
    time=alarm_time.cget("text")
    audio_file=alarm_audio.cget("text")
    hour1=time[0]
    hour2=time[1]
    min1=time[3]
    min2=time[4]
    alarm={"hour1":hour1,"hour2":hour2,"min1":min1,"min2":min2,"name":name,"audio_file":audio_file,"state":state}
    with open(json_file_path,"r") as file:
        data=json.load(file)
        for alarm in data.get("alarms", []):
            if (
                alarm["name"] == name and
                alarm["hour1"] == hour1 and alarm["hour2"] == hour2 and
                alarm["min1"] == min1 and alarm["min2"] == min2 and
                alarm["audio_file"] == audio_file
            ):
                alarm["state"] = "disabled"
                break
        data["alarms"].remove(alarm)
        with open(json_file_path,"w") as file:
            json.dump(data,file,indent=4)
    alarm_frame.destroy()
    return

def load_alarms_on_start():
    with open(json_file_path,"r") as file:
        data=json.load(file)
        for alarm in data['alarms']:
            hour1=alarm['hour1']
            hour2=alarm['hour2']
            min1=alarm['min1']
            min2=alarm['min2']
            name=alarm['name']
            alarm_frame=ttk.Frame(alarms_window)
            alarm_frame.pack()
            audio_file=alarm['audio_file']
            alarm_name=ttk.Label(alarm_frame,text=name)
            alarm_name.pack(side="left")
            alarm_time=ttk.Label(alarm_frame,text=hour1+hour2+":"+min1+min2)
            alarm_time.pack(side="left")
            alarm_audio=ttk.Label(alarm_frame,text=audio_file)
            alarm_audio.pack(side="left")
            var=tk.IntVar(value=1 if alarm["state"] == "enabled" else 0)
            alarm_state_checkbox=ttk.Checkbutton(alarm_frame,text="Enable",variable=var,onvalue=1, offvalue=0,command=lambda f=alarm_frame: change_alarm_state(f,var))
            alarm_state_checkbox.pack(side="left")
            delete_button=ttk.Button(alarm_frame,text="Delete",command=lambda f=alarm_frame: delete_alarm(f))
            delete_button.pack(side="right")
    return

def change_alarm_state(alarm_frame,var):
    if var.get()==1:
        enable_alarm(alarm_frame)
    else:
        disable_alarm(alarm_frame)

def disable_alarm(alarm_frame):
    alarm_name,alarm_time,alarm_audio,_,_=alarm_frame.winfo_children()
    name=alarm_name.cget("text")
    time=alarm_time.cget("text")
    audio_file=alarm_audio.cget("text")
    hour1=time[0]
    hour2=time[1]
    min1=time[3]
    min2=time[4]
    alarm={"hour1":hour1,"hour2":hour2,"min1":min1,"min2":min2,"name":name,"audio_file":audio_file,"state":"enabled"}
    with open(json_file_path,"r") as file:
        data=json.load(file)
        for alarm in data.get("alarms", []):
            if (
                alarm["name"] == name and
                alarm["hour1"] == hour1 and alarm["hour2"] == hour2 and
                alarm["min1"] == min1 and alarm["min2"] == min2 and
                alarm["audio_file"] == audio_file
            ):
                alarm["state"] = "disabled"
                break
        with open(json_file_path,"w") as file:
            json.dump(data,file,indent=4)
    return

def enable_alarm(alarm_frame):
    alarm_name,alarm_time,alarm_audio,_,_=alarm_frame.winfo_children()
    name=alarm_name.cget("text")
    time=alarm_time.cget("text")
    audio_file=alarm_audio.cget("text")
    hour1=time[0]
    hour2=time[1]
    min1=time[3]
    min2=time[4]
    alarm={"hour1":hour1,"hour2":hour2,"min1":min1,"min2":min2,"name":name,"audio_file":audio_file,"state":"disabled"}
    with open(json_file_path,"r") as file:
        data=json.load(file)
        for alarm in data.get("alarms", []):
            if (
                alarm["name"] == name and
                alarm["hour1"] == hour1 and alarm["hour2"] == hour2 and
                alarm["min1"] == min1 and alarm["min2"] == min2 and
                alarm["audio_file"] == audio_file
            ):
                alarm["state"] = "enabled"
                break
        with open(json_file_path,"w") as file:
            json.dump(data,file,indent=4)
    return

def load_alarm_on_save():
    with open(json_file_path,"r") as file:
        data=json.load(file)
        alarm=data["alarms"][-1]
        hour1=alarm['hour1']
        hour2=alarm['hour2']
        min1=alarm['min1']
        min2=alarm['min2']
        name=alarm['name']
        alarm_frame=ttk.Frame(alarms_window)
        alarm_frame.pack()
        audio_file=alarm['audio_file']
        alarm_name=ttk.Label(alarm_frame,text=name)
        alarm_name.pack(side="left")
        alarm_time=ttk.Label(alarm_frame,text=hour1+hour2+":"+min1+min2)
        alarm_time.pack(side="left")
        alarm_audio=ttk.Label(alarm_frame,text=audio_file)
        alarm_audio.pack(side="left")
        var=tk.IntVar(value=1 if alarm["state"] == "enabled" else 0)
        alarm_state_checkbox=ttk.Checkbutton(alarm_frame,text="Enable",variable=var,onvalue=1, offvalue=0,command=lambda f=alarm_frame: change_alarm_state(f,var))
        alarm_state_checkbox.pack(side="left")
        delete_button=ttk.Button(alarm_frame,text="Delete",command=lambda f=alarm_frame: delete_alarm(f))
        delete_button.pack(side="right")


main_window=tk.Tk()
main_window.title("Clock App")
main_window.geometry("400x300")
current_time = datetime.datetime.now().strftime("%H:%M")

alarms_window=tk.Toplevel(main_window)
alarms_window.title("alarms")
alarms_window.withdraw()

main_window_time=tk.Label(main_window,text=datetime.datetime.now().strftime("%H:%M"),font=('Helvetica',40))
main_window_time.pack()

alarms_window_button=ttk.Button(main_window,text="alarms",command=alarms_window.deiconify)
alarms_window_button.pack()

timer_window=tk.Toplevel(main_window)
timer_window.title("timer")
timer_window.withdraw()

timer_time=tk.Label(timer_window,text="timer time goes here")
timer_time.pack()

timer_pause=tk.Button(timer_window,text='Pause',command=lambda: pause_timer())
timer_delete=tk.Button(timer_window,text='delete',command=lambda: delete_timer())
timer_pause.pack()
timer_delete.pack()

timer_window_button=ttk.Button(main_window,text="timer",command=timer_window.deiconify)
timer_window_button.pack()

timer_audio_file_label=ttk.Label(timer_window,text="Audio File")
timer_audio_file_button=ttk.Button(timer_window,text="Choose Audio File",command=openfile)
timer_audio_file_label.pack()
timer_audio_file_button.pack()

##
#Create new alarm window
##

new_alarm=tk.Toplevel(alarms_window)
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
new_alarm.withdraw()

##
#save succesful window
##

successful_save=tk.Toplevel(new_alarm)
successful_save.title("")
successful_save.geometry("200x100")
successful_save_label=ttk.Label(successful_save,text="Alarm Saved Successfully")
successful_save_label.pack()
successful_save_button=ttk.Button(successful_save,text="OK",command=lambda : (successful_save.master.destroy()
                                                                     ,load_alarm_on_save()))
successful_save_button.pack()
successful_save.withdraw()

new_alarm_button=ttk.Button(alarms_window,text="+",command=new_alarm.deiconify)
new_alarm_button.pack()

load_alarms_on_start()

check_alarm()

main_window.mainloop()