from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import pymongo
global myclient
global mydb
global mycol
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["project1"]
mycol=mydb['test1']
mycol.create_index([("phonenumber", 1)], unique=True)


windows1=Tk()
windows1.geometry('1920x1080')
windows1.title("welcome")
windows1.config(bg="#0BEEF9")
photo=PhotoImage(file="im5.png")
pic=Label(windows1,image=photo,border=0 ,width=650 ,height=406)
pic.place(x=5,y=200)
'''def move_text():
    canv1.move(text_id,5,0)# Move the text object 5 pixels to the right
    canv1.after(90, move_text)
        # Call the move_text function again after 50,60.. milliseconds # edi speed of text decide chastundi'''
#--------------------------------------------------------------------------------------------------------
#destroy frame1(signin)
#store the login details database(MONGODB)
def login():
    frame1.destroy()
    frame2.place(x=950,y=80)

def sigin():
  
    username1=x1.get()
    phonenum1=y1.get()
    pass1=z1.get()
    x2={"username":username1,"phonenumber":phonenum1,"password":pass1}

    mydata=x2
    print(mydata)
    mycol.insert_one(mydata)
    dblist = myclient.list_database_names()#to store the data base name in one list
    if phonenum1 in dblist:# to chect whether phonenum1 database is there are not
        pass
    else:
        mydb1=myclient[phonenum1] # creating new data base with user mobile number
        mycol2=mydb1[username1] # it is the collection is created to create the data base without table the data basee ws not created in mongo db
        x={'username':username1,"phoneno":phonenum1}#we insert 1 row as username and mobile number
        mycol2.insert_one(x) #insert_one is finctio to insert one row
    frame1.destroy()
    t.destroy()
    frame2.place(x=950,y=80)

    


#------------------------------------------------------------------------------
# on click login to go login page from signup page



    
#-------------------------------------------------------------------------------------------------
#destroy frame2(login)
def destroy2():
    global phoneno2, password2
    password2=z5.get()
    phoneno2=y2.get()

    x=mycol.find({'phonenumber':phoneno2})
    for i in x:
        if i["password"]==password2:
            frame2.destroy()
            pic.destroy()
            windows1.config(bg="#AEC8DA")
            frame3.place(x=500,y=20)
            

            break
'''def userdata_represent():
    global phoneno2, password2
    mydb=myclient[phoneno2]
    mycol=mydb.list_collection_names()
    mycol=mydb[mycol[0]]
    mycol = mycol.find_one({}, {'_id': 0, 'username': 1, 'phoneno': 1})
    
    if mycol:
        label5=Label(executionframe,bg="white",text="username  " + mycol['username'],font=('Microsoft Yahei UI Light',12,'bold'))
        label5.place(x=20,y=300)
        label6=Label(home,bg="white",text="phonenumber  " + mycol['phoneno'],font=('Microsoft Yahei UI Light',12,'bold'))
        label6.place(x=20,y=330)'''
    


def closeintrest():
    frame4.destroy()
    frame3.place(x=500,y=20)
    

    
#----------------------------------------------------------------
#store the login details database(MONGODB)
 
    

#frame---------------------------------------------------------------------------------------

frame1=Frame(windows1,bg="#fff",border=1,width=350,height=600)
##---------------------------------------------------------------------------
#welcome
t=Label(windows1,text="welcome",fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',23,'bold'))
t.place(x=5,y=60)
Label(windows1,text="It is the one the small business aplication",fg="black",bg="white",font=('Script MT Bold',16,'bold')).place(x=5,y=650)
Label(windows1,text= "use to  know whom you the give money and how much",fg="black",bg="white",font=('Script MT Bold',16,'bold')).place(x=5,y=690)

frame1.place(x=950,y=80)
#canv1= Canvas(windows1, width=650,height=50,bg="white")
#canv1.place(x=5,y=650)
#text_id=canv1.create_text(5,10, text="It is the one the small business aplication use to  know whom you the give money and how much",  anchor="nw",font=('Microsoft Yahei UI Light',16,'bold'))
#20, 100) specifies that the starting position of the text object is 20 pixels to the right and 100 pixels down from the top-left corner of the canvas
#In Tkinter, the anchor option determines the reference point for an item's position on the canvas. The anchor values are represented by compass directions: "n" for north (top), "s" for south (bottom), "w" for west (left), "e" for east (right), and combinations such as "nw", "se", etc.
Label(frame1,text="Sign In",border=0,bg='black',fg="#57a1f8",font=('Microsoft Yahei UI Light',23,'bold')).place(x=30,y=35)
def on_enter(e):
    x1.delete(0,'end')
def on_leave(e):
    if x1.get()=='':
        x1.insert(0,"username")

x1 =Entry(frame1,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
x1.place(x=30,y=150)
x1.insert(0,'username')
x1.bind("<FocusIn>",on_enter)
x1.bind("<FocusOut>",on_leave)
Frame(frame1,width=295,height=2,bg='black').place(x=25,y=177)
##---------------------------------------------------------------------------------
def on_enter(e):
    y1.delete(0,'end')
def on_leave(e):
    if y1.get()=='':
        y1.insert(0,"mobile-number")

y1 =Entry(frame1,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
y1.place(x=30,y=200)
y1.insert(0,'mobile-number')
y1.bind("<FocusIn>",on_enter)
y1.bind("<FocusOut>",on_leave)
####-----------------------------------------------------------------------------------------------------------
Frame(frame1,width=295,height=2,bg='black').place(x=25,y=225)
def on_enter(e):
    z1.delete(0,'end')
def on_leave(e):
    if z1.get()=='':
        z1.insert(0,"password")


z1 =Entry(frame1,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
z1.place(x=30,y=245)
z1.insert(0,'password')
z1.bind("<FocusIn>",on_enter)
z1.bind("<FocusOut>",on_leave)
Frame(frame1,width=295,height=2,bg='black').place(x=30,y=275)
##--------------------------------------------------------------------------------------------


##--------------------------frame1 sign  up snd login button

Button(frame1,width=32,text='Sign up',bg='#57a1f8',fg='black',border=0,command=sigin,font=('Microsoft Yahei UI Light',12)).place(x=30,y=300)
label=Label(frame1,text='I have an acccount',fg='black',bg='white',font=('Microsoft Yahei UI Light',10))
label.place(x=75,y=350)
signin=Button(frame1,width=6,text='login',border=0,command=login,bg='white',cursor='hand2',fg='#E15B08',font=('Microsoft Yahei UI Light',11))
signin.place(x=200,y=350)

#######---------------------------------------------------------------------------------
#frame2
frame2=Frame(windows1,bg="#fff",border=1,width=350,height=600)
Label(frame2,bg="black",text="Log In",fg="#57a1f8",font=('Microsoft Yahei UI Light',23,'bold')).place(x=30,y=35)

##---------------------------------------------------------------------------------
def on_enter(e):
    y2.delete(0,'end')
def on_leave(e):
    if y2.get()=='':
        y2.insert(0,"Mobile number")

y2 =Entry(frame2,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
y2.place(x=30,y=200)
y2.insert(0,'mobile number')
y2.bind("<FocusIn>",on_enter)
y2.bind("<FocusOut>",on_leave)
####-----------------------------------------------------------------------------------------------------------

####-----------------------------------------------------------------------------------------------------------
Frame(frame2,width=295,height=2,bg='black').place(x=25,y=225)
def on_enter(e):
    z5.delete(0,'end')
def on_leave(e):
    if z5.get()=='':
        z5.insert(0,"password")

z5 =Entry(frame2,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
z5.place(x=30,y=250)
z5.insert(0,'pasword')
z5.bind("<FocusIn>",on_enter)
z5.bind("<FocusOut>",on_leave)
####-----------------------------------------------------------------------------------------------------------

####-----------------------------------------------------------------------------------------------------------
Frame(frame2,width=295,height=2,bg='black').place(x=25,y=275)


Button(frame2,width=32,text='login',bg='#57a1f8',fg='black',command=destroy2,border=0,font=('Microsoft Yahei UI Light',12)).place(x=30,y=300)
label=Label(frame2,text="I don't have  any account",fg='black',bg='white',font=('Microsoft Yahei UI Light',10))
label.place(x=50,y=355)
signin=Button(frame2,width=6,text='Sign In',border=0,cursor='hand2',fg='#E15B08',font=('Microsoft Yahei UI Light',11))
signin.place(x=215,y=350)
#-------------------------------------------------------------------------------------------------
frame3=Frame(windows1,width=1000,height=750,bg="#4FA9E8",border=0)








'''def open_image():
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
b2.place(x=120,y=140)'''



#Button(frame3,text="take loan",cursor='hand2',bg="white",border=0,font=('Microsoft Yahei UI Light',11)).place(x=250,y=150)
#Button(frame3,text="transtions",cursor='hand2',bg="white",border=0,font=('Microsoft Yahei UI Light',11)).place(x=250,y=200)

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------take loan (frame4)
def delect_frames():
    for frames in  executionframe.winfo_children():# what are the child frames in frame6 are are delet other rames only open button click frame
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
    home_frame=Frame(executionframe,width=500,height=750)
    def open_image():
        file_open=filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])
        image_open=Image.open(file_open)
        image_open=image_open.resize((150,150))
        tk_image = ImageTk.PhotoImage(image_open)
        # Update the label with the new image
        profile_image.config(image=tk_image)
        profile_image.image = tk_image
    
    Button(home_frame,text="upload profile", command=open_image,cursor='hand2',border=0,font=('Microsoft Yahei UI Light',11)).place(x=20,y=250)
    profile_image = Label(home_frame)
    profile_image = Label(home_frame)
    profile_image.place(x=20,y=40)
    def userdata_represent():
        global phoneno2, password2
        mydb=myclient[phoneno2]
        mycol=mydb.list_collection_names()
        mycol=mydb[mycol[0]]
        mycol = mycol.find_one({}, {'_id': 0, 'username': 1, 'phoneno': 1})
    
        if mycol:
            label5=Label(executionframe,bg="white",text="username  " + mycol['username'],font=('Microsoft Yahei UI Light',12,'bold'))
            label5.place(x=20,y=300)
            label6=Label(home_frame,bg="white",text="phonenumber  " + mycol['phoneno'],font=('Microsoft Yahei UI Light',12,'bold'))
            label6.place(x=20,y=330)
    
    userdata_represent()
    
    
    
    home_frame.pack(pady=20)



def transtion_framepage():
    transtion_frame=Frame(executionframe,width=500,height=750)
    lb=Label(transtion_frame,text="jgvgvjhvjvjhbjhbnmgbjbjh\n\nhvvggggv",font=("bold",30))
    lb.pack()
    transtion_frame.pack(pady=20)
def Takeloan_framepage():
    Takeloan_frame=Frame(executionframe,width=500,height=750)
    lb=Label(Takeloan_frame,text="tttttttttttttttbjh\n\nhvvggggv",font=("bold",30))
    lb.pack()
    Takeloan_frame.pack(pady=20)
def discription_framepage():
    discription_frame=Frame(executionframe,width=500,height=750)
    lb=Label(discription_frame,text="oky hdeh bjh\n\nhvvggggv",font=("bold",30))
    lb.pack()
    discription_frame.pack(pady=20)



frame4=Frame(frame3,bg="#c3c3c3",border=0,width=100,height=750)
frame4.pack(side=LEFT)
frame4.pack_propagate(False)
home_but=Button(frame4,text="home",font=("Bold",12),fg="#158aff",bg="#c3c3c3",border=0,command=lambda:indicator(home_indicator,home_framepage))

home_but.place(x=10,y=50)
home_indicator=Label(frame4,text=" ",font=("Bold",12),bg="#c3c3c3")

home_indicator.place(x=3,y=50,width=5,height=40)
discription=Button(frame4,text="discription",font=("Bold",12),fg="#158aff",bg="#c3c3c3",border=0,command=lambda:indicator(discription_indicator,discription_framepage))

discription.place(x=10,y=123)
discription_indicator=Label(frame4,text="",font=("Bold",12),bg="#c3c3c3")

discription_indicator.place(x=3,y=110,width=5,height=40)

Takeloan=Button(frame4,text="takeloan",font=("Bold",12),fg="#158aff",bg="#c3c3c3",border=0,command=lambda:indicator(Takeloan_indicator,Takeloan_framepage))

Takeloan.place(x=10,y=180)

Takeloan_indicator=Label(frame4,text=" ",font=("Bold",12),bg="#c3c3c3",border=0)

Takeloan_indicator.place(x=3,y=170,width=5,height=40)


transtion=Button(frame4,text="transtion",font=("Bold",12),fg="#158aff",bg="#c3c3c3",border=0,command=lambda:indicator(transtion_indicator,transtion_framepage))

transtion.place(x=10,y=240)

transtion_indicator=Label(frame4,text=" ",font=("Bold",12),bg="#c3c3c3",border=0)

transtion_indicator.place(x=3,y=230,width=5,height=40)


executionframe=Frame(frame3,highlightbackground="black",highlightthickness=2)
executionframe.pack(side=LEFT)
executionframe.pack_propagate(False)
executionframe.configure(width=500,height=750)
windows1.mainloop()