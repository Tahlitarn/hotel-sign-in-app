from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import customtkinter
import sqlite3
import time

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')
me = customtkinter.CTk()
me.title('CLOCKING APP')
app_width = 600
app_height = 630
screen_width = me.winfo_screenwidth()
screen_height = me.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
me.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
me.resizable(width=False, height=False)

# creating database connection

conn = sqlite3.connect('staff clocking app.db')

# creating frames for both staff login and register staff
global txt_Username

login_frame = LabelFrame (me, text="Staff Login Page", labelanchor=  'n', bg="black", fg='gold')
login_frame.grid(row=1,column=0,padx=150,pady=200)

register_frame = LabelFrame (me, text="Staff Registration Page", labelanchor=  'n', bg="black", fg='gold')
register_frame.grid_forget()

admin_frame =LabelFrame (login_frame, text=" ADMIN OMLY ", labelanchor=  'n', bg="black", fg='gold')
admin_frame.grid_forget()

clocking_page_frame= LabelFrame (me, text="Staff Clocking Page", labelanchor=  'n', bg="black", fg='gold')
clocking_page_frame.grid_forget()

data_frame = LabelFrame (me, text="Attendance Record", labelanchor=  'n', bg="black", fg='gold')
data_frame.grid_forget()

# adding widget to login frame
lbl_username= customtkinter.CTkLabel(login_frame, text= 'USERNAME',text_color='gold', font=('cambria', 10))
lbl_username.grid(row=0, column=0)
lbl_password= customtkinter.CTkLabel(login_frame, text= 'PASSWORD',text_color='gold', font=('cambria', 10))
lbl_password.grid(row=2, column=0)

txt_Username = customtkinter.CTkEntry(login_frame,width= 150, height=10,corner_radius=5,text_color='gold',placeholder_text="Enter Username", placeholder_text_color="gold", font= ('lucida calligraphy',12))
txt_Username.grid(row=1, column=0,padx=5,columnspan=2)
txt_Password = customtkinter.CTkEntry(login_frame,width= 150, height=10,corner_radius=5,text_color='gold',placeholder_text="Enter Password", placeholder_text_color="gold", font= ('lucida calligraphy',12), show='*')
txt_Password.grid(row=3, column=0,padx=5,columnspan=2)

def enter():
    print("button pressed")
    clocking_page_frame.grid(row=1,column=0,padx=150,pady=200)
    register_frame.grid_forget()
    login_frame.grid_forget()

btn_login = customtkinter.CTkButton(login_frame, text='LOGIN',text_color='gold',corner_radius=5,hover_color='green',bg_color="black", fg_color='black', width=50, border_width=0, font=('cambria',12), command=enter )
btn_login.grid(row=4, column=0,padx= 20,columnspan=2)

def new_staff():
    login_frame.grid_forget()
    register_frame.grid(row=1,column=0,padx=150,pady=200)
btn_register = customtkinter.CTkButton(login_frame, text='Click here to register new staff',text_color='green',corner_radius=5,hover_color='green',hover=DISABLED,bg_color="black", fg_color='black', width=300, border_width=0, font=('lucida calligraphy',12), command=new_staff )
btn_register.grid(row=5, column=0, columnspan=2)

def ad():
    admin_frame.grid(row=7,column=0)
btn_admin = customtkinter.CTkButton(login_frame, text='Admin Only',text_color='gold',corner_radius=5,hover_color='green',hover=DISABLED,bg_color="black", fg_color='black', width=100, height=10, border_width=0, font=('lucida calligraphy',8), command=ad )
btn_admin.grid(row=6, column=0)

# adding widget to register frame

lbl_full_name= customtkinter.CTkLabel(register_frame, text= 'Full Name',text_color='gold', font=('cambria', 10))
lbl_full_name.grid(row=0, column=0)
lbl_password= customtkinter.CTkLabel(register_frame, text= 'PASSWORD',text_color='gold', font=('cambria', 10))
lbl_password.grid(row=1, column=0)
lbl_confirm_password= customtkinter.CTkLabel(register_frame, text= ' CONFIRM PASSWORD',text_color='gold', font=('cambria', 10))
lbl_confirm_password.grid(row=2, column=0)

txt_full_name = customtkinter.CTkEntry(register_frame,width= 150, height=10,corner_radius=5,text_color='gold',placeholder_text="Enter Username", placeholder_text_color="gold", font= ('lucida calligraphy',12))
txt_full_name.focus_set()
txt_full_name.grid(row=0, column=1, padx=10)
txt_Password = customtkinter.CTkEntry(register_frame,width= 150, height=10,corner_radius=5,text_color='gold',placeholder_text="Enter Password", placeholder_text_color="gold", font= ('lucida calligraphy',12), show='*')
txt_Password.grid(row=1, column=1, padx=10)
txt_CPassword = customtkinter.CTkEntry(register_frame,width= 150, height=10,corner_radius=5,text_color='gold',placeholder_text="Confirm Password", placeholder_text_color="gold", font= ('lucida calligraphy',12), show='*')
txt_CPassword.grid(row=2, column=1, padx=10)

def reg():
    pass
btn_reg = customtkinter.CTkButton(register_frame, text='REGISTER',text_color='gold',corner_radius=5,hover_color='green',bg_color="black", fg_color='black', width=50, border_width=0, font=('cambria',12), command=reg )
btn_reg.grid(row=3, column=0,padx= 20,columnspan=2)

def bck():
    register_frame.grid_forget()
    login_frame.grid(row=1,column=0,padx=150,pady=200)

btn_back= customtkinter.CTkButton(register_frame, text='Proceed to Login Page',text_color='gold',corner_radius=5,hover_color='green',bg_color="black", fg_color='black', width=50, border_width=0, font=('lucida calligraphy',12),hover=DISABLED, command=bck )
btn_back.grid(row=4, column=0, columnspan=2)

# creating admin login page

txt_admin= customtkinter.CTkEntry(admin_frame,width= 150, height=10,corner_radius=5,text_color='gold',placeholder_text="Enter Password", placeholder_text_color="gold", font= ('lucida calligraphy',12), show='*')
txt_admin.grid(row=0, column=0, padx=10)
txt_admin.focus_set()

def ad_pass():
    psw = "admin1234567890"

    if txt_admin.get() == psw:
        messagebox.showinfo("ADMIN", "PASSWORD CORRECT")
        data_frame.grid(row=1,column=0,padx=100,pady=150)
        login_frame.grid_forget()

    elif txt_admin.get() == "":
        messagebox.showerror("ERROR","field cannot be empty")
        txt_admin.focus_set()
        
    else:
        messagebox.showwarning("WARNING!!!", "INCORRECT PASSWORD")
        txt_admin.delete(0,END)
        txt_admin.focus_set()
        
btn_ad_login = customtkinter.CTkButton(admin_frame, text='ENTER',text_color='gold',corner_radius=5,hover_color='green',bg_color="black", fg_color='black', width=50, border_width=0, font=('cambria',12), command=ad_pass )
btn_ad_login.grid(row=1, column=0,padx= 20,columnspan=2)

# clocking page
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%a")
    month = time.strftime("%b")
    date = time.strftime("%e")
    year = time.strftime("%y")
    am_pm = time.strftime("%p")
    lbl_time.config(text = day + "-" + month + "-" + date + "-" + year + "    " + hour + ":" + minute + ":" + second + am_pm)
    lbl_time.after(1000,clock)

lbl_time = Label(clocking_page_frame,text="" , font=('cambria', 12),bg="black", fg='gold')
lbl_time.grid(row=0, column=0,columnspan=4, padx=5, pady=5)
clock()
def update():
    pass
    # lbl_Uname.configure(text = f'{txt_Username.get()}')
lbl_Uname = customtkinter.CTkLabel(clocking_page_frame,text="" ,text_color='black', font=('cambria', 10),corner_radius=5, width=200,bg_color="gold", fg_color='gold')
lbl_Uname.grid(row=1, column=0,columnspan=4, padx=10)
update()

def clock_in():
    print ("welcome")
btn_clock_in = customtkinter.CTkButton(clocking_page_frame,text='clock-in',text_color='gold',corner_radius=5,hover_color='green',bg_color="black", fg_color='black', width=50, border_width=0, font=('cambria',12), command=clock_in)
btn_clock_in.grid(row=2, column=0)
btn_clock_out = customtkinter.CTkButton(clocking_page_frame,text='clock-out',text_color='gold',corner_radius=5,hover_color='green',bg_color="black", fg_color='black', width=50, border_width=0, font=('cambria',12), command=clock_in)
btn_clock_out.grid(row=2, column=1)
def ex():
    clocking_page_frame.grid_forget()
    login_frame.grid(row=1,column=0,padx=150,pady=200)
btn_clock_exit = customtkinter.CTkButton(clocking_page_frame,text='Exit',text_color='gold',corner_radius=5,hover_color='green',bg_color="black", fg_color='black', width=50, border_width=0, font=('cambria',12), command=ex)
btn_clock_exit.grid(row=2, column=2)

# creating tree inside data frame

my_tree = ttk.Treeview(data_frame)
# define columns
my_tree['columns'] = ("Name", "clock-in", "clock-out")

# format the columns
my_tree.column("#0", width=0, minwidth=0)
my_tree.column("Name",anchor=W, width=130, minwidth=10)
my_tree.column("clock-in",anchor=CENTER, width=150)
my_tree.column("clock-out", anchor=W, width=130)

# creating headings on the tree
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Staff Name", anchor=W)
my_tree.heading("clock-in", text="CLOCK-IN", anchor=CENTER)
my_tree.heading("clock-out", text="CLOCK-OUT", anchor=W)

# add data
my_tree.insert(parent='', index='end', iid=0,text="", values=(""))
my_tree.pack(pady=20)

# button for tree
btn_print = customtkinter.CTkButton(data_frame,text='PRINT',text_color='gold',corner_radius=5,hover_color='green',bg_color="black", fg_color='black', width=50, border_width=0, font=('cambria',12), command=ex)
btn_print.pack()
btn_home = customtkinter.CTkButton(data_frame,text='EXIT',text_color='gold',corner_radius=5,hover_color='red',bg_color="black", fg_color='black', width=50, border_width=0, font=('cambria',12), command=ex)
btn_home.pack()

me.mainloop()