from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import customtkinter
import sqlite3
import datetime

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
login = customtkinter.CTk()
login.title('Login_Page')
app_width = 600
app_height= 650
screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
login.geometry(f'{app_width}X{app_height}+{int(x)}+{int(y)}')

frm = LabelFrame(login, text= "STAFF LOGIN-PORTAL", font=("cambria", 12),labelanchor='n', highlightthickness=2)
frm.pack()

#creating frame to seperate new staff and old staff
staff_login = LabelFrame(frm, text= "STAFF LOGIN", font=("cambria", 8),labelanchor='n', highlightthickness=2, height=300)
staff_login.grid(row=0, column=0)

staff_register = LabelFrame(frm, text= "REGISTER STAFF", font=("cambria", 8),labelanchor='n', highlightthickness=2)
staff_register.grid(row=0, column=2)

# creating login form
lbl_U_name = customtkinter.CTkLabel(staff_login, text='USER NAME', corner_radius=3, font= ('cambria',10), text_color="black",)
lbl_U_name.grid(row=0, column=0, padx=5)
lbl_psswrd = customtkinter.CTkLabel(staff_login, text='PASSWORD', corner_radius=3, font= ('cambria',10), text_color="black",)
lbl_psswrd.grid(row=0, column=1,padx=5)

txt_U_name = customtkinter.CTkEntry(staff_login, fg_color= 'white', text_color='black', font=('cambria', 10),placeholder_text='ENTER USER NAME', width=120, corner_radius=8)
txt_U_name.grid(row=1, column=0)
txt_psswrd = customtkinter.CTkEntry(staff_login, fg_color= 'white', text_color='black', font=('cambria', 10),placeholder_text='ENTER PASSWORD', show='*', width=120, corner_radius=8)
txt_psswrd.grid(row=1, column=1,padx=5,pady=5)

def enter():
    username= "ADMIN"
    password= "12345"
    if txt_U_name.get().upper() == username and txt_psswrd.get() == password:
        #msg= messagebox.showinfo("STAFF ONLY", "LOGIN SUCCESFUL")
        print('welcome')
        
btn_login = customtkinter.CTkButton(staff_login, text="LOGIN", corner_radius=5,hover_color="green", font=('elephant',10), text_color='black', width=100,command=enter)
btn_login.grid(row=2, column=0, pady=5)
btn_exit = customtkinter.CTkButton(staff_login, text="EXIT", corner_radius=5,hover_color="red", font=('elephant',10), text_color='black', width=100,command=quit)
btn_exit.grid(row=2, column=1, pady=5)

# creating register form
lbl_full_name = customtkinter.CTkLabel(staff_register, text='FULL NAME', corner_radius=3, font= ('cambria',10), text_color="black",)
lbl_full_name.grid(row=0, column=0, padx=5)
lbl_User_name = customtkinter.CTkLabel(staff_register, text='USER-NAME', corner_radius=3, font= ('cambria',10), text_color="black",)
lbl_User_name.grid(row=0, column=2, padx=5)

lbl_psswrd = customtkinter.CTkLabel(staff_register, text='PASSWORD', corner_radius=3, font= ('cambria',10), text_color="black",)
lbl_psswrd.grid(row=1, column=0,padx=5)
lbl_c_psswrd = customtkinter.CTkLabel(staff_register, text='CONFIRM PASSWORD', corner_radius=3, font= ('cambria',10), text_color="black",)
lbl_c_psswrd.grid(row=1, column=2,padx=5)

txt_f_name = customtkinter.CTkEntry(staff_register, fg_color= 'white', text_color='black', font=('cambria', 10),placeholder_text='FULL NAME', width=120, corner_radius=8)
txt_f_name.grid(row=0, column=1)
txt_U_name = customtkinter.CTkEntry(staff_register, fg_color= 'white', text_color='black', font=('cambria', 10),placeholder_text='USER NAME', width=120, corner_radius=8)
txt_U_name.grid(row=0, column=3, padx=5, pady=5)
txt_psswrd = customtkinter.CTkEntry(staff_register, fg_color= 'white', text_color='black', font=('cambria', 10),placeholder_text='PASSWORD', width=120, corner_radius=8)
txt_psswrd.grid(row=1, column=1)
txt_c_psswrd = customtkinter.CTkEntry(staff_register, fg_color= 'white', text_color='black', font=('cambria', 10),placeholder_text='CONFIRM PASSWORD', width=120, corner_radius=8)
txt_c_psswrd.grid(row=1, column=3)


def create():
    pass
btn_create = customtkinter.CTkButton(staff_register, text="REGISTER", corner_radius=5,hover_color="green", font=('elephant',10), text_color='black', width=100,command=create)
btn_create.grid(row=3, column=1, pady=5)
btn_clear = customtkinter.CTkButton(staff_register, text="CLEAR", corner_radius=5,hover_color="red", font=('elephant',10), text_color='black', width=100,command=enter)
btn_clear.grid(row=3, column=2, pady=5)
btn_exit = customtkinter.CTkButton(staff_register, text="EXIT", corner_radius=5,hover_color="purple", font=('elephant',10), text_color='black', width=100,command=quit)
btn_exit.grid(row=3, column=3, pady=5, padx=5)


login.mainloop()