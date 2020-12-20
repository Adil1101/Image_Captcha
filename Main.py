def login():
    import login
def signup():
    import signup
import tkinter as tk
from tkinter import *
root=tk.Tk()
root.title("welcome page")
root.geometry("500x500")
w=tk.Label(root,text="WELCOME \n",bg="Red",fg="black")
w.config(width=200)
w.config(font=("Arial Black",56))
w.pack()
w1=tk.Label(root,text="Made By--Mohammad Adil\n Image Base Captcha\n INT213\n\n\n")
w1.config(width=200)
w1.config(font=("Comic sans Ms",20))
w1.pack()
frame=tk.Frame(root)
frame.pack()
def abc():
    rootA=Tk()
    rootA.title('Login')
    b=Label(rootA,text='please Login\n')
    b.grid(sticky=E)
    n1=Label(rootA,text='Username:')
    p2=Label(rootA,text='Password:')
    n1.grid(row=1,column=0)
    p2.grid(row=2,column=0)
    n1=Entry(rootA)
    p2=Entry(rootA,show='*')
    n1.grid(row=1,column=1)
    p2.grid(row=2,column=1)
    B=tk.Button(rootA,text='Login')
    B.grid(rowspan=1,columnspan=2,sticky=N)
    user=Button(rootA,text='Delete User',fg='red')
    user.grid(rowspan=1,columnspan=2,sticky=N)
    rootA.mainloop()
B1=Button(frame,text="Login",command=lambda : abc(),width=20)

B1.pack()
root.mainloop()
