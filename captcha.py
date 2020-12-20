from tkinter import *
import tkinter.messagebox as tm
import tkinter
import random

top = Tk()

a='BirthDay cake'
b='cars'
c='flower'
d='Road'
listo=[a,b,c,d]
select=random.choice(listo)
def image1():
    if str(select)==a:
        tm.showinfo("Captcha info","Verified")
    else:
        tm.showerror("Captcha info","Not Verified")
    
def image2():
    if str(select)==b:
        tm.showinfo("Captcha info","Verified")
    else:
        tm.showerror("Captcha info","Not Verified")
def image3():
    if str(select)==c:
        tm.showinfo("Captcha info","Verified")
    else:
        tm.showerror("Captcha info","Not Verified")
def image4():
    if str(select)==d:
        tm.showinfo("Captcha info","Verified")
    else:
        tm.showerror("Captcha info","Not Verified")
u=tkinter.Label(top,text=select)
u.grid()
photo = PhotoImage(file = 'screenshot (24).png' )
b = Button(image = photo, command = image1, height = 100, width = 150) 
b.grid( row=1,column=0)


photo1 = PhotoImage(file = 'screenshot (29).png' )
b1 = Button(image = photo1, command = image2, height = 100, width = 150) 
b1.grid( row=1,column=1)


photo2 = PhotoImage(file = 'screenshot (30).png' )
b2 = Button(image = photo2, command = image3, height = 100, width = 150) 
b2.grid( row=2,column=0)



photo4 = PhotoImage(file = 'Roa.png' )
b4 = Button(image = photo4, command = image4, height = 100, width = 150) 
b4.grid( row=2,column=1)


mainloop()    
