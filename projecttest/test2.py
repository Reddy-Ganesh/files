from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
window5=Tk()
window5.geometry('1080x700')
window5.title("titler")


def delect_frames():
    for frames in  frame6.winfo_children():# what are the child frames in frame6 are are delet other rames only open button click frame
        frames.destroy()


def indicator(lb,page):
    hide_indicators()
    lb.config(bg="#158aff")
    delect_frames()
    page()
def hide_indicators():
    home_indicator.config(bg="#c3c3c3")
    transtion_indicator.config(bg="#c3c3c3")
    Takeloan_indicator.config(bg="#c3c3c3")
    discription_indicator.config(bg="#c3c3c3")
def home_framepage():
    home_frame=Frame(frame6)
    lb=Label(frame6,text="hello",font=("bold",30))
    lb.pack()
    home_frame.pack(pady=20)

def transtion_framepage():
    transtion_frame=Frame(frame6)
    lb=Label(frame6,text="jgvgvjhvjvjhbjhbnmgbjbjh\n\nhvvggggv",font=("bold",30))
    lb.pack()
    transtion_frame.pack(pady=20)
def Takeloan_framepage():
    Takeloan_frame=Frame(frame6)
    lb=Label(frame6,text="tttttttttttttttbjh\n\nhvvggggv",font=("bold",30))
    lb.pack()
    Takeloan_frame.pack(pady=20)
def discription_framepage():
    discription_frame=Frame(frame6)
    lb=Label(frame6,text="oky hdeh bjh\n\nhvvggggv",font=("bold",30))
    lb.pack()
    discription_frame.pack(pady=20)


frame3 =Frame(window5,bg="#c3c3c3")
frame3.pack(side=LEFT)
frame3.pack_propagate(False)#we can resize thev frame if you pass false
frame3.configure(width=100,height=400)
home_but=Button(frame3,text="home",font=("Bold",12),fg="#158aff",bg="#c3c3c3",border=0,command=lambda:indicator(home_indicator,home_framepage))

home_but.place(x=10,y=50)
home_indicator=Label(frame3,text=" ",font=("Bold",12),bg="#c3c3c3")

home_indicator.place(x=3,y=50,width=5,height=40)







discription=Button(frame3,text="discription",font=("Bold",12),fg="#158aff",bg="#c3c3c3",border=0,command=lambda:indicator(discription_indicator,discription_framepage))

discription.place(x=10,y=123)
discription_indicator=Label(frame3,text="",font=("Bold",12),bg="#c3c3c3")

discription_indicator.place(x=3,y=110,width=5,height=40)

Takeloan=Button(frame3,text="takeloan",font=("Bold",12),fg="#158aff",bg="#c3c3c3",border=0,command=lambda:indicator(Takeloan_indicator,Takeloan_framepage))

Takeloan.place(x=10,y=180)

Takeloan_indicator=Label(frame3,text=" ",font=("Bold",12),bg="#c3c3c3",border=0)

Takeloan_indicator.place(x=3,y=170,width=5,height=40)


transtion=Button(frame3,text="transtion",font=("Bold",12),fg="#158aff",bg="#c3c3c3",border=0,command=lambda:indicator(transtion_indicator,transtion_framepage))

transtion.place(x=10,y=240)

transtion_indicator=Label(frame3,text=" ",font=("Bold",12),bg="#c3c3c3",border=0)

transtion_indicator.place(x=3,y=230,width=5,height=40)



frame6=Frame(window5,highlightbackground="black",highlightthickness=2)
frame6.pack(side=LEFT)
frame3.pack_propagate(False)
frame6.configure(width=500,height=400)
window5.mainloop()





