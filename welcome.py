def login():
    root.destroy()
    import login
import tkinter as tk
root=tk.Tk()
root.title("welcome page")
root.geometry("500x600")
w=tk.Label(root,text="WELCOME \n",bg="Red",fg="black")
w.config(width=200)
w.config(font=("Arial Black",56))
w.pack()
w1=tk.Label(root,text="Made By--Mohammad Adil \n Image Base Captcha\n INT213\n\n\n")
w1.config(width=200)
w1.config(font=("Comic sans Ms",20))
w1.pack()
frame=tk.Frame(root)
frame.pack()
Button=tk.Button(frame,text="Login",width=20,command=login)
Button.pack()
root.mainloop()
