import tkinter
from tkinter.font import BOLD
import customtkinter as ctk
from PIL import ImageTk, Image  


class MainFrame:
    def __init__(self, root) -> None:

        self.main_frame = ctk.CTkFrame(root)

        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.place(relx=0.1, rely=0.08, anchor=tkinter.CENTER)

        # Welcome Label
        self.wel_label = ctk.CTkLabel(self.header_frame, text="Welcome, ", font=ctk.CTkFont(family="Segoe UI",size=32))
        self.wel_label.grid(row=0, column=0)

        # User Label
        self.user_label = ctk.CTkLabel(self.header_frame, text="Karan!", font=ctk.CTkFont(family="Segoe UI",size=32, weight='bold'))
        self.user_label.grid(row=0, column=1)


        self.center_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.center_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.get_started_label = ctk.CTkLabel(self.center_frame, text="Let's Get Started", font=ctk.CTkFont(family='Segoe UI', size=24, weight='bold'))
        self.get_started_label.grid(row=0, columnspan=3, pady=64)

        # Touch Image
        self.image1 = ctk.CTkImage(Image.open("images/Touch.png"), size=(96, 96))

        self.img_label1 = ctk.CTkLabel(self.center_frame, text="", image=self.image1)
        self.img_label1.grid(row=1, column=0, padx=64, pady=12)

        # Double Click Image
        self.image2 = ctk.CTkImage(Image.open("images/Peace_Sign.png"), size=(96, 96))

        self.img_label2 = ctk.CTkLabel(self.center_frame, text="", image=self.image2)
        self.img_label2.grid(row=1, column=1, padx=64, pady=12)

        # Grab Image
        self.image3 = ctk.CTkImage(Image.open("images/Take.png"), size=(96, 96))

        self.img_label3 = ctk.CTkLabel(self.center_frame, text="", image=self.image3)
        self.img_label3.grid(row=1, column=2, padx=64, pady=12)

        # Move Label
        self.move_label1 = ctk.CTkLabel(self.center_frame, text="Move Finger", font=ctk.CTkFont(family="Segoe UI",size=18, weight='bold'))
        self.move_label1.grid(row=2, column=0, pady=0)

        self.move_label2 = ctk.CTkLabel(self.center_frame, text="to move the cursor", font=("Segoe UI", 14))
        self.move_label2.grid(row=3, column=0, pady=0)

        # Touch Label
        self.touch_label1 = ctk.CTkLabel(self.center_frame, text="Touch Two Fingers", font=ctk.CTkFont(family="Segoe UI",size=18, weight='bold'))
        self.touch_label1.grid(row=2, column=1, pady=0)

        self.touch_label2 = ctk.CTkLabel(self.center_frame, text="to perform right click", font=("Segoe UI", 14))
        self.touch_label2.grid(row=3, column=1, pady=0)

        # Fold Label
        self.fold_label1 = ctk.CTkLabel(self.center_frame, text="Fold your hand", font=ctk.CTkFont(family="Segoe UI",size=18, weight='bold'))
        self.fold_label1.grid(row=2, column=2, pady=0)

        self.fold_label2 = ctk.CTkLabel(self.center_frame, text="to perform drag and drop", font=("Segoe UI", 14))
        self.fold_label2.grid(row=3, column=2, pady=0)

        self.btn_start_wc = ctk.CTkButton(self.center_frame, 
                                    text="Start Webcam", 
                                    font=("Segoe UI", 18),
                                    width=166, height=40,
                                    fg_color='#9443dd',
                                    corner_radius=20)


        self.btn_start_wc.grid(row=4, columnspan=3, pady=64)
        
        # settings_icon
        self.img_setting = ctk.CTkImage(Image.open("images/settings.png"), size=(36,36))

        self.btn_settings = ctk.CTkButton(self.main_frame, text="", fg_color="transparent", image=self.img_setting, width=48, height=48, corner_radius=16)
        self.btn_settings.place(relx=0.95, rely=0.92)

