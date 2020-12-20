from tkinter import *
import tkinter
import random
top=tkinter.Tk()
top.title('Image')
a='Cars'
b='BirthDay Cake'
c='Road'
d='Bus'
listo=[a,b,c,d]
select=random.choice(listo)
u=tkinter.Label(top,text=select)
u.pack()
CheckVar1=IntVar()
CheckVar2=IntVar()
CheckVar3=IntVar()
CheckVar4=IntVar()
if select==a:
    def checkbox1():
        print("Verified and you are exited from the program")
        exit(0)
def module():
        button["image"]=background2
canvas=Canvas(top, width=150,height=100)
canvas.pack(anchor=W,padx=0,pady=0)
background=PhotoImage(file='C:\\Users\\Adil\\Desktop\\adil.gif')
background2=PhotoImage(file='C:\\Users\\Adil\\Desktop\\IMG-20170731-WA0009.gif')

button=Button(image=background,height=50,command=module)
button.pack()
canvas.create_image(0,0,anchor=NW,image=background)

canvas=Canvas(top, width=150,height=100)
canvas.pack(anchor=W,padx=0,pady=0)
b=PhotoImage(file='F:\\3rd sem\\python\\projects\\IMG-20170731-WA0009.gif')
canvas.create_image(0,0,anchor=NW,image=b)
C2 = Checkbutton(top, text =b, variable = CheckVar2,onvalue =1, offvalue = 0, height=5,width =0)
C2.pack(anchor=W,padx=0,pady=0)
canvas=Canvas(top, width=150,height=100)
canvas.pack(anchor=W,padx=0,pady=0)
c=PhotoImage(file='F:\\3rd sem\\python\\projects\\IMG-20170731-WA0009.gif')

canvas.create_image(10,10,anchor=NW,image=b)
C3 = Checkbutton(top, text =c, variable = CheckVar3,onvalue =1, offvalue = 0, height=5,width =0)
C3.pack(anchor=W,padx=0,pady=0)
canvas=Canvas(top, width=150,height=100)
canvas.pack(anchor=W,padx=0,pady=0)
d=PhotoImage(file='F:\\3rd sem\\python\\projects\\IMG-20170731-WA0009.gif')
canvas.create_image(10,10,anchor=NW,image=b)
C4 = Checkbutton(top, text =d, variable = CheckVar4,onvalue =1, offvalue = 0, height=-5,width =0)
C4.pack(anchor=W,padx=0,pady=0)

top.mainloop()

