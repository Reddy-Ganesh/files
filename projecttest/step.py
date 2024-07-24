from tkinter import Tk, Button, Entry, Label, Frame

def update_text():
    name_text = "name+" + name_entry.get()
    display1.insert(0, name_text)
    
    cn_text = "\ncontact+" + contact_entry.get()
    display1.insert("end", cn_text)

window = Tk()

frame3 = Frame(window, width=750, height=550, bg="white", border=2)
frame3.pack()

name_label = Label(frame3, text="name")
name_label.place(x=40, y=250)
name_entry = Entry(frame3, width=38, font=('Microsoft Yahei UI Light', 11))
name_entry.place(x=50, y=270)

contact_label = Label(frame3, text="contact no")
contact_label.place(x=40, y=300)
contact_entry = Entry(frame3, width=38, font=('Microsoft Yahei UI Light', 11))
contact_entry.place(x=50, y=320)

update_button = Button(frame3, text="Update Text", command=update_text)
update_button.place(x=20, y=350)

display1 = Entry(frame3, width=38, font=('Microsoft Yahei UI Light', 11))
display1.place(x=50, y=380)

window.mainloop()
