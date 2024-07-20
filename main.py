from itertools import tee
import tkinter
import customtkinter as ctk
from main_frame import *
from settings_frame import SettingsFrame
from os import getlogin
from gesture import *
from threading import Thread
import json


webcam_enabled = False

with open('settings.json', 'r') as f:
    settings = json.load(f)

ctk.set_appearance_mode("Dark")

user_name = getlogin().split()[0].capitalize()

win = ctk.CTk()
win.title("PC Control using Hand Gestures")
win.geometry('1920x1080')

setting = SettingsFrame(win, settings)

main = MainFrame(win)
main.user_label.configure(text=user_name+"!")
main.main_frame.pack(fill=tkinter.BOTH, expand=1)

def settings_btn_clicked():
    main.main_frame.pack_forget()
    setting.setting_frame.pack(fill=tkinter.BOTH, expand=1, padx=(64,0), pady=16)

def setting_back_btn_clicked():
    setting.setting_frame.pack_forget()
    main.main_frame.pack(fill=tkinter.BOTH, expand=1)

def webcam_btn_clicked():
    global webcam_enabled
    t1 = None

    if webcam_enabled:
        GestureController.cap.release()
        cv2.destroyWindow('Gesture Controller')
        GestureController.stop_thread = True
        main.btn_start_wc.configure(text="Start Webcam")
        webcam_enabled = False
    else:
        main.btn_start_wc.configure(text="Stop Webcam")
        webcam_enabled = True
        gc = GestureController(settings)
        GestureController.stop_thread = False
        t1 = Thread(target=gc.start)
        t1.start()

main.btn_settings.configure(command=settings_btn_clicked)
setting.setting_button.configure(command=setting_back_btn_clicked)
main.btn_start_wc.configure(command=webcam_btn_clicked)

win.mainloop()