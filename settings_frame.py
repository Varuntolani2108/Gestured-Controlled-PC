from email import header
import tkinter
from tkinter import messagebox
from tkinter.font import BOLD
import customtkinter as ctk
from PIL import Image
import json


class SettingsFrame():
    def __init__(self, root, settings=None) -> None:
        self.setting_frame = ctk.CTkScrollableFrame(root, fg_color="transparent")

        self.img_left_arrow = ctk.CTkImage(Image.open("images/left-arrow.png"), size=(32, 32))

        # Settings Label
        self.setting_button = ctk.CTkButton(self.setting_frame, anchor='w', fg_color="transparent",
                                            compound=tkinter.LEFT, text=" Settings", image=self.img_left_arrow,
                                            font=ctk.CTkFont(family="Segoe UI", size=36, weight='bold'))
        self.setting_button.grid(row=0, column=0, pady=32, sticky=tkinter.W)

        # Map gestures heading
        self.map_ges1 = ctk.CTkLabel(self.setting_frame, text="Map Gestures",
                                     font=ctk.CTkFont(family="Segoe UI", size=18, weight='bold'))
        self.map_ges1.grid(row=1, column=0, sticky=tkinter.W)

        self.map_ges2 = ctk.CTkLabel(self.setting_frame, text="Map Gestures to appropriate actions.",
                                     font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_ges2.grid(row=2, column=0, sticky=tkinter.W)

        # sep 1
        ctk.CTkFrame(
            master=self.setting_frame,
            height=2,
            fg_color='#333333'
        ).grid(row=3, column=0, pady=8, sticky="ew", columnspan=4)

        # map_option 1
        self.map_move_label1 = ctk.CTkLabel(self.setting_frame, text="Two Finger Move Gesture",
                                            font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_move_label1.grid(row=4, column=0, sticky=tkinter.W)

        self.map_move_label2 = ctk.CTkLabel(self.setting_frame, text="Which action for two finger move gesture.",
                                            font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_move_label2.grid(row=5, column=0, sticky=tkinter.W)

        self.map_move_cb = ctk.CTkComboBox(self.setting_frame, values=["Cursor movement", "Multiple item selection"],
                                           width=200, font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_move_cb.set("Cursor movement")
        self.map_move_cb.grid(row=4, column=1, rowspan=2, padx=(80, 120))

        # map_option 2
        self.map_touch_label1 = ctk.CTkLabel(self.setting_frame, text="Two Finger Close Gesture",
                                             font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_touch_label1.grid(row=6, column=0, sticky=tkinter.W, pady=(16, 4))

        self.map_touch_label2 = ctk.CTkLabel(self.setting_frame, text="Which action for two finger close gesture.",
                                             font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_touch_label2.grid(row=7, column=0, sticky=tkinter.W)

        self.map_touch_cb = ctk.CTkComboBox(self.setting_frame, values=["Double Click", "Left Click", "Right Click"],
                                            width=200, font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_touch_cb.set("Double Click")
        self.map_touch_cb.grid(row=6, column=1, rowspan=2, padx=(80, 120))

        # map_option 3
        self.map_dgdp_label1 = ctk.CTkLabel(self.setting_frame, text="Hand Fold & Release Gesture",
                                            font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_dgdp_label1.grid(row=8, column=0, sticky=tkinter.W, pady=(16, 4))

        self.map_dgdp_label2 = ctk.CTkLabel(self.setting_frame, text="Which action for hand fold & release gesture.",
                                            font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_dgdp_label2.grid(row=9, column=0, sticky=tkinter.W)

        self.map_dgdp_cb = ctk.CTkComboBox(self.setting_frame, values=["Drag & Drop"], width=200,
                                           font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_dgdp_cb.set("Drag & Drop")
        self.map_dgdp_cb.grid(row=8, column=1, rowspan=2, padx=(80, 120))

        # map_option 4
        self.map_midf_label1 = ctk.CTkLabel(self.setting_frame, text="Middle Finger Gesture",
                                            font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_midf_label1.grid(row=10, column=0, sticky=tkinter.W, pady=(16, 4))
        self.map_midf_label2 = ctk.CTkLabel(self.setting_frame, text="Which action for middle finger gesture.",
                                            font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_midf_label2.grid(row=11, column=0, sticky=tkinter.W)
        self.map_midf_cb = ctk.CTkComboBox(self.setting_frame,
                                           values=["Left click", "Right Click", "Double Click"],
                                           width=200, font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_midf_cb.set("Left Click")
        self.map_midf_cb.grid(row=10, column=1, rowspan=2, padx=(80, 120))

        # map_option 5
        self.map_indf_label1 = ctk.CTkLabel(self.setting_frame, text="Index Finger Gesture",
                                            font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_indf_label1.grid(row=12, column=0, sticky=tkinter.W, pady=(16, 4))
        self.map_indf_label2 = ctk.CTkLabel(self.setting_frame, text="Which action for index finger gesture.",
                                            font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_indf_label2.grid(row=13, column=0, sticky=tkinter.W)
        self.map_indf_cb = ctk.CTkComboBox(self.setting_frame, values=["Right click", "Left Click", "Double Click"],
                                           width=200, font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_indf_cb.set("Right Click")
        self.map_indf_cb.grid(row=12, column=1, rowspan=2, padx=(80, 120))

        # map_option 6
        self.map_lpnv_label1 = ctk.CTkLabel(self.setting_frame, text="Left Hand Pinch Vertically Gesture",
                                            font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_lpnv_label1.grid(row=4, column=2, sticky=tkinter.W, pady=(16, 4))
        self.map_lpnv_label2 = ctk.CTkLabel(self.setting_frame,
                                            text="Which action for left hand pinch vertically gesture.",
                                            font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_lpnv_label2.grid(row=5, column=2, sticky=tkinter.W)
        self.map_lpnv_cb = ctk.CTkComboBox(self.setting_frame,
                                           values=["Volume Control", "Brightness Control", "Scroll Horizantally",
                                                   "Scroll Vertically"], width=200,
                                           font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_lpnv_cb.set("Scroll Vertically")
        self.map_lpnv_cb.grid(row=4, column=3, rowspan=2, padx=(80, 120))

        # map_option 7
        self.map_lpnh_label1 = ctk.CTkLabel(self.setting_frame, text="Left Hand Pinch Horizantally Gesture",
                                            font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_lpnh_label1.grid(row=6, column=2, sticky=tkinter.W, pady=(16, 4))
        self.map_lpnh_label2 = ctk.CTkLabel(self.setting_frame,
                                            text="Which action for left hand pinch horizantally gesture.",
                                            font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_lpnh_label2.grid(row=7, column=2, sticky=tkinter.W)
        self.map_lpnh_cb = ctk.CTkComboBox(self.setting_frame,
                                           values=["Brightness Control", "Volume Control", "Scroll Horizantally",
                                                   "Scroll Vertically"], width=200,
                                           font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_lpnh_cb.set("Scroll Horizantally")
        self.map_lpnh_cb.grid(row=6, column=3, rowspan=2, padx=(80, 120))

        # map_option 8
        self.map_rpnh_label1 = ctk.CTkLabel(self.setting_frame, text="Right Hand Pinch Horizantally",
                                            font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_rpnh_label1.grid(row=8, column=2, sticky=tkinter.W, pady=(16, 4))
        self.map_rpnh_label2 = ctk.CTkLabel(self.setting_frame,
                                            text="Which action for right hand pinch horizantally gesture.",
                                            font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_rpnh_label2.grid(row=9, column=2, sticky=tkinter.W)
        self.map_rpnh_cb = ctk.CTkComboBox(self.setting_frame,
                                           values=["Scroll Horizantally", "Scroll Vertically", "Volume Control",
                                                   "Brightness Control"], width=200,
                                           font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_rpnh_cb.set("Brightness Control")
        self.map_rpnh_cb.grid(row=8, column=3, rowspan=2, padx=(80, 120))

        # map_option 9
        self.map_rpnh_label1 = ctk.CTkLabel(self.setting_frame, text="Right Hand Pinch Vertically",
                                            font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_rpnh_label1.grid(row=10, column=2, sticky=tkinter.W, pady=(16, 4))
        self.map_rpnh_label2 = ctk.CTkLabel(self.setting_frame,
                                            text="Which action for right hand pinch vertically gesture.",
                                            font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_rpnh_label2.grid(row=11, column=2, sticky=tkinter.W)
        self.map_rpnv_cb = ctk.CTkComboBox(self.setting_frame,
                                           values=["Scroll Vertically", "Scroll Horizantally", "Volume Control",
                                                   "Brightness Control"], width=200,
                                           font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_rpnv_cb.set("Volume Control")
        self.map_rpnv_cb.grid(row=10, column=3, rowspan=2, padx=(80, 120))

        # map_option 10
        self.map_fhm_label1 = ctk.CTkLabel(self.setting_frame, text="Fold Hands and Move",
                                           font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.map_fhm_label1.grid(row=12, column=2, sticky=tkinter.W, pady=(16, 4))
        self.map_fhm_label2 = ctk.CTkLabel(self.setting_frame, text="Which action for fold hands and move gesture.",
                                           font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_fhm_label2.grid(row=13, column=2, sticky=tkinter.W)
        self.map_fhm_cb = ctk.CTkComboBox(self.setting_frame, values=["Multiple item selection", "Cursor movement"],
                                          width=200, font=ctk.CTkFont(family="Segoe UI", size=14))
        self.map_fhm_cb.set("Multiple Item Selection")
        self.map_fhm_cb.grid(row=12, column=3, rowspan=2, padx=(80, 120))

        # sep label 2
        self.sep_label2 = ctk.CTkLabel(self.setting_frame, text="")
        self.sep_label2.grid(row=14, column=0, sticky=tkinter.W, pady=(12))

        # Webcam options
        self.wc_opt1 = ctk.CTkLabel(self.setting_frame, text="Webcam Options",
                                    font=ctk.CTkFont(family="Segoe UI", size=18, weight='bold'))
        self.wc_opt1.grid(row=15, column=0, sticky=tkinter.W)
        self.wc_opt2 = ctk.CTkLabel(self.setting_frame, text="Settings related to webcam",
                                    font=ctk.CTkFont(family="Segoe UI", size=14))
        self.wc_opt2.grid(row=16, column=0, sticky=tkinter.W)

        # sep label 3
        ctk.CTkFrame(
            master=self.setting_frame,
            height=2,
            fg_color='#333333'
        ).grid(row=17, column=0, pady=8, sticky="ew", columnspan=4)

        # lines setting
        self.show_lines_fing = ctk.CTkLabel(self.setting_frame, text="Show lines displaying finger points",
                                            font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.show_lines_fing.grid(row=18, column=0, columnspan=3, sticky=tkinter.W)
        self.show_line_switch = ctk.CTkSwitch(self.setting_frame, text="", progress_color='#9443dd')
        self.show_line_switch.grid(row=18, column=3, sticky=tkinter.E)
        self.show_line_switch.select()

        # action name setting
        self.show_action_name = ctk.CTkLabel(self.setting_frame, text="Show action name performed",
                                             font=ctk.CTkFont(family="Segoe UI", size=14, weight='bold'))
        self.show_action_name.grid(row=19, column=0, columnspan=3, sticky=tkinter.W, pady=12)
        self.show_acn_switch = ctk.CTkSwitch(self.setting_frame, text="", progress_color='#9443dd')
        self.show_acn_switch.grid(row=19, column=3, sticky=tkinter.E)

        self.btn_save_changes = ctk.CTkButton(self.setting_frame,
                                              text="Save Changes",
                                              font=("Segoe UI", 16),
                                              fg_color='#9443dd',
                                              corner_radius=20)

        self.btn_save_changes.grid(row=20, column=3, pady=32, sticky="E")
        self.btn_save_changes.configure(command=self.save_changes_btn_clicked)

        if settings is not None:
            self.show_line_switch.select() if settings['lines_drawn'] == 'true' else self.show_line_switch.deselect()
            self.show_acn_switch.select() if settings['action_shown'] == 'true' else self.show_acn_switch.deselect()
            self.map_move_cb.set(settings['two_finger_move'])
            self.map_touch_cb.set(settings['two_finger_close'])
            self.map_dgdp_cb.set(settings['hand_fold_release'])
            self.map_midf_cb.set(settings['middle_finger'])
            self.map_indf_cb.set(settings['index_finger'])
            self.map_lpnv_cb.set(settings['left_pinch_ver'])
            self.map_lpnh_cb.set(settings['left_pinch_hor'])
            self.map_rpnv_cb.set(settings['right_pinch_ver'])
            self.map_rpnh_cb.set(settings['right_pinch_hor'])
            self.map_fhm_cb.set(settings['fold_hand_move'])

    def save_changes_btn_clicked(self):
        data = {}

        data["two_finger_move"] = self.map_move_cb.get()
        data["two_finger_close"] = self.map_touch_cb.get()
        data["hand_fold_release"] = self.map_dgdp_cb.get()
        data["middle_finger"] = self.map_midf_cb.get()
        data["index_finger"] = self.map_indf_cb.get()
        data["left_pinch_ver"] = self.map_lpnv_cb.get()
        data["left_pinch_hor"] = self.map_lpnh_cb.get()
        data["right_pinch_hor"] = self.map_rpnh_cb.get()
        data["right_pinch_ver"] = self.map_rpnv_cb.get()
        data["fold_hand_move"] = self.map_fhm_cb.get()

        data["lines_drawn"] = "true" if self.show_line_switch.get() == 1 else "false"
        data["action_shown"] = "true" if self.show_acn_switch.get() == 1 else "false"

        with open('settings.json', 'w') as json_file:
            json.dump(data, json_file)

        messagebox.showinfo(title="Info", message="Restart App to see changes")
        self.setting_frame.master.quit()
