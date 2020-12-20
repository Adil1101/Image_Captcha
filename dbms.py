from tkinter import *
window=Tk()

CheckVar1=IntVar()
def image1():
    if str(select)==a:
        tm.showinfo("Captcha info","Verified")
    else:
        tm.showerror("Captcha info","Not Verified")
        
canvas=Canvas(window,width=150,height=100)
canvas.pack(anchor=W,padx=0,pady=0)
a=PhotoImage(file="adil.gif")
C1=Checkbutton(window,text=a,variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=0)
C1.pack(anchor=W,padx=0,pady=0)
button=Button(image=a,height=50,width=50,command=image1)
button.pack(anchor=W,padx=0,pady=0)
