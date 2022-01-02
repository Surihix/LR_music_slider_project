import tkinter
from tkinter \
    import Scale, Button, Label, Tk, ttk, HORIZONTAL, \
    PhotoImage, BOTTOM, \
    W, X, SUNKEN
from tkinter.font import Font
import subprocess
import os
from os.path import dirname
import sys

BASEPATH = dirname(__file__)


# Section defining the sys/temp directory for the exe to look for the image files.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Section defining the window size, color, icon and display image
LR_vol_root = Tk()
LR_vol_root.title("LIGHTNING RETURNS : FINAL FANTASY XIII - Music Volume Slider  v1.3")
LR_vol_root.configure(background="#494a4c")
LR_vol_root.iconbitmap(resource_path("image_files/app_icon_title-bar.ico"))
LR_vol_root.geometry("620x830")
LR_vol_root.resizable(width=False, height=False)

display_img = PhotoImage(file=resource_path('image_files/app_display_img.png'))
window_canvas = Label(image=display_img, background="#494a4c")
window_canvas.pack(pady=8)

# Section defining the text sizes with the Font widget
text_size_large = Font(size=11)
text_size_small = Font(size=10)
credit_text_size_heading = Font(size=12)
credit_text_size = Font(size=11)

# Section defining the tab's theme
style = ttk.Style()

style.theme_create("modified", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {"configure": {"padding": [20, 8], "background": "#494a4c",
                                    "foreground": "white", "font": text_size_large},
                      "expand": [("selected", [1, 1, 1, 0])]}})

style.theme_use("modified")


# Section defining the tab position and attributes when on the app
tabs = ttk.Notebook(LR_vol_root)

tab_a = ttk.Frame(tabs)
tab_b = ttk.Frame(tabs)

tabs.add(tab_a, text="Main")
tabs.add(tab_b, text="Credits")
tabs.pack(expand=2, fill="both", padx=0)
ttk.Style().configure(LR_vol_root, background="#494a4c")
tab_b.focus()

# Section defining the placement of the text displayed above the slider with the frame widget
frame0 = tkinter.Frame(tab_a)
frame0.pack(padx=0, pady=30)
text_above_slider = Label(frame0, text="Set your desired volume by clicking and dragging the slider to a value.",
                          font=text_size_large, fg="white", background="#494a4c")
text_above_slider.pack()
text_above_slider2 = Label(frame0, text="Once you have set a value, click on the Set Volume button.",
                           font=text_size_large, fg="white", background="#494a4c")
text_above_slider2.pack(fill="both")


# Section defining the slider
frame1 = tkinter.Frame(tab_a, background="#494a4c")
frame1.pack(padx=30, pady=10)
slider = Scale(frame1, tickinterval=0.5, fg="white", bg="#494a4c", from_=0, to=5,
               length=250, orient=HORIZONTAL)
LR_vol_root.bind("<Left>", lambda e: slider.set(slider.get() - 1))
LR_vol_root.bind("<Right>", lambda e: slider.set(slider.get() + 1))
slider.set(5)
slider.pack()

text_below_slider = Label(frame1, text="You can also use the Left and Right arrow keys to control the slider!",
                          font=text_size_small, fg="white", background="#494a4c")
text_below_slider.pack(pady=15)

text_below_slider2 = Label(frame1, text="If the arrow keys do not work for the slider, then press the TAB key",
                           font=text_size_small, fg="white", background="#494a4c")
text_below_slider2.pack(pady=10)


# Section defining the function that allows the bat scripts to open
def open_bat():
    batch_file_open = slider.get()
    if batch_file_open == 0:
        subprocess.call([BASEPATH + r'.\batch_scripts\level-0.bat'], cwd=BASEPATH + r'\batch_scripts')
        status_bar['text'] = 'Music is muted'
        return
    if batch_file_open == 1:
        subprocess.call([BASEPATH + r'.\batch_scripts\level-1.bat'], cwd=BASEPATH + r'\batch_scripts')
        status_bar['text'] = 'Music Volume set to 1'
        return
    if batch_file_open == 2:
        subprocess.call([BASEPATH + r'.\batch_scripts\level-2.bat'], cwd=BASEPATH + r'\batch_scripts')
        status_bar['text'] = 'Music Volume set to 2'
        return
    if batch_file_open == 3:
        subprocess.call([BASEPATH + r'.\batch_scripts\level-3.bat'], cwd=BASEPATH + r'\batch_scripts')
        status_bar['text'] = 'Music Volume set to 3'
        return
    if batch_file_open == 4:
        subprocess.call([BASEPATH + r'.\batch_scripts\level-4.bat'], cwd=BASEPATH + r'\batch_scripts')
        status_bar['text'] = 'Music Volume set to 4'
        return
    if batch_file_open == 5:
        subprocess.call([BASEPATH + r'.\batch_scripts\level-5.bat'], cwd=BASEPATH + r'\batch_scripts')
        status_bar['text'] = 'Music Volume set to 5. this is the default volume'
        return


def set_volume_hover(e):
    set_volume["bg"] = "#0bae73"


def set_volume_hover_leave(e):
    set_volume["bg"] = "#059561"


# Section defining the button functions and its attributes with the frame widget
frame2 = tkinter.Frame(tab_a, background="#494a4c")
frame2.pack(ipadx=30, ipady=30, pady=10)
set_volume = Button(frame2, text="Set Volume", background="#059561", fg="white",
                    font=text_size_large, height=2, width=15, command=open_bat)
set_volume.bind("<Enter>", set_volume_hover)
set_volume.bind("<Leave>", set_volume_hover_leave)
set_volume.pack()


# Section defining the status bar and its attributes
status_bar = Label(tabs, text="Welcome to LR Music Volume Slider v1.3 ", background="#494a4c", takefocus=0,
                   font=text_size_large, fg="white", relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)


# Section for tab 2 and credits
frame_cr = tkinter.Frame(tab_b)
frame_cr.pack(padx=0, pady=20)
credit_text = Label(frame_cr, text="Credits", font=credit_text_size_heading,
                    fg="white", background="#494a4c")
credit_text.pack()

frame_cr_sub = tkinter.Frame(tab_b)
frame_cr_sub.pack(padx=0, pady=20, fill="both")
credit_text1 = Label(frame_cr_sub, text="Surihix  -  Programmer and creator of this app", font=credit_text_size,
                     fg="white", background="#494a4c")
credit_text1.pack(fill="both")
credit_text2 = Label(frame_cr_sub, text="Kirsan Thyme  -  for Nova Chrysalia's WDB repack function",
                     font=credit_text_size, fg="white", background="#494a4c")
credit_text2.pack(fill="both")
credit_text3 = Label(frame_cr_sub, text="GreenThumbs2  -  for the FFXIIIGetPathTool and the WPDPack tool",
                     font=credit_text_size, fg="white", background="#494a4c")
credit_text3.pack(fill="both")

credit_text4 = Label(frame_cr_sub, text="FluffyQuack  -  for the ff13tool", font=credit_text_size,
                     fg="white", background="#494a4c")
credit_text4.pack(fill="both")
credit_text5 = Label(frame_cr_sub, text="Echelo  -  for the ffxiiicrypt tool", font=credit_text_size,
                     fg="white", background="#494a4c")
credit_text5.pack(fill="both")

LR_vol_root.mainloop()
