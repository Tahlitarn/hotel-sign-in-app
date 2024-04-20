from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import customtkinter
import sqlite3
import datetime
from login_page import login

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
home_page = customtkinter.CTk()
home_page.title('HomePage')
app_width = 600
app_height= 650
screen_width = home_page.winfo_screenwidth()
screen_height = home_page.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
home_page.geometry(f'{app_width}X{app_height}+{int(x)}+{int(y)}')

frm = LabelFrame(home_page, text= "STAFF LOGIN-PORTAL", font=("cambria", 12),labelanchor='n', highlightthickness=2)
frm.pack()

login()

home_page.mainloop()
