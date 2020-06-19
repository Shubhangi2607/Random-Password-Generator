import tkinter
from tkinter import *
from tkinter import Tk
import string
import random
window =Tk()
window.geometry('250x250')

label1=Label(window,text="enter length")
label1.place(x=75,y=20)

entry_in=Entry(window,width=20)
entry_in.place(x=75,y=38)

entry_out=Entry(window)
entry_out.place(x=75,y=105)

def retrieve():
        entry_out.delete(0,'end')
        lt=int(entry_in.get())
        s1=string.ascii_letters+string.digits+string.punctuation
        password= "".join(random.choice(s1) for i in range (lt))
        entry_out.insert(0,password)

b=Button(window,text="submit",command=retrieve)
b.place(x=70,y=150)
window.mainloop()