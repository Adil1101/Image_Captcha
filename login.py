def cap():
    rootA.destroy()
    import captcha
    
from tkinter import *
import sqlite3

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
loginB=Button(rootA,text='Login',command=cap)
loginB.grid(rowspan=1,columnspan=2,sticky=N)
n1=str(n1)
p2=str(p2)

conn=sqlite3.connect("project.db") 
conn.execute("Insert into LOGIN(Username,Password)values(?,?)",(n1,p2))
conn.commit()
user=Button(rootA,text='Delete User',fg='red')
user.grid(rowspan=1,columnspan=2,sticky=N)
rootA.mainloop()
