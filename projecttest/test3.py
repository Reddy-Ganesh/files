"""from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

top = Tk()
top.geometry('1920x1080')
top.config(bg="white")


def sam():
    global p
    p = x.get()
    frame1.destroy()
    frame2.place(x=800,y=50)
    use()
def use():
    global p
    label = Label(frame2, text="Value of p: " + str(p),bg="white",fg='black')
    label.place(x=90,y=250)




frame1 = Frame(top, width=500, height=750,bg="black")
frame1.place(x=800, y=50)
x = Entry(frame1, width=10, border=1, bg="pink")
x.place(x=20, y=100)
y = Entry(frame1, width=10, border=1, bg="pink")
y.place(x=20, y=175)
b = Button(frame1, text="okay", command=sam, cursor='hand2', fg='#E15B08', font=('Microsoft Yahei UI Light', 11), border=0)
b.place(x=75, y=250)

frame2 = Frame(top, width=500, height=750, bg="red")

x1 = Entry(frame2, width=20, border=1)
x1.place(x=20, y=100)
y1 = Entry(frame2, width=20, border=1)
y1.place(x=20, y=175)
button = Button(frame2, text="ss")

button.place(x=75, y=250)



top.mainloop()"""
''''def open_image():
    file_open=filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])
    image_open=Image.open(file_open)
    image_open=image_open.resize((150,150))
    tk_image = ImageTk.PhotoImage(image_open)
    
    # Update the label with the new image
    profile_image.config(image=tk_image)
    profile_image.image = tk_image
Button(frame3,text="upload profile", command=open_image,cursor='hand2',border=0,font=('Microsoft Yahei UI Light',11)).place(x=20,y=250)
profile_image = Label(frame3)
profile_image.place(x=20,y=40)
b2=Button(frame3,text="intrest",bg="white",fg="black",cursor="hand2",border=0,command=intrest,font=('Microsoft Yahei UI Light',11))
b2.place(x=120,y=140)


Label(frame4,bg="black",text="GIVE LOAN WITH WHAT INTEREST",fg="#57a1f8",font=('Microsoft Yahei UI Light',12,'bold')).place(x=30,y=35)

def on_enter(e):
    interestpercentage.delete(0,'end')
def on_leave(e):
    if interestpercentage.get()=='':
        interestpercentage.insert(0,"interestpercentage")

interestpercentage =Entry(frame4,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
interestpercentage.place(x=30,y=200)
interestpercentage.insert(0,'mobile number')
interestpercentage.bind("<FocusIn>",on_enter)
interestpercentage.bind("<FocusOut>",on_leave)
Frame(frame4,width=295,height=2,bg='black').place(x=25,y=225)
def on_enter(e):
    descrption.delete(0,'end')
def on_leave(e):
    if descrption.get()=='':
        descrption.insert(0,"descrption about u")

descrption =Entry(frame4,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
descrption.place(x=30,y=250)
descrption.insert(0,'descrption')
descrption.bind("<FocusIn>",on_enter)
descrption.bind("<FocusOut>",on_leave)
Frame(frame4,width=295,height=2,bg='black').place(x=25,y=275)
b1=Button(frame4,text="X",bg="white",fg="black",command=closeintrest,cursor="hand2",font=('Microsoft Yahei UI Light',11))
b1.place(x=320,y=3)



Frame(frame4,width=350,height=2,bg='black').place(x=30,y=155)'''
text = "Hello, world!"

# Convert text to bytes using UTF-8 encoding
bytes_data = text.encode('utf-8')

# Print the bytes data
print(bytes_data)
if  len(bytes_data)>0:
    print('yes')

