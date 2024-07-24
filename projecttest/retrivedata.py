import pymongo
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from prettytable import PrettyTable

from io import BytesIO
windows2=Tk()
windows2.geometry('1920x1080')
windows2.title("welcome")
windows2.config(bg="#0BEEF9")
client=pymongo.MongoClient("mongodb://localhost:27017")
mydb=client['1122']
mycol=mydb.list_collection_names()
mycol=mydb[mycol[0]]


'''mdbs=client['7702837610']
mycol=mdbs.list_collection_names()

mycol=mdbs[mycol[0]]
print(mycol)'''
result = mycol.find_one({}, {'_id': 0, 'username': 1, 'phoneno': 1,'image':1})

def open_image():
    global file_open,image_open,image_bytes
    global ten5
    global image_data150
    ten5=1
    file_open=filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])
    if file_open:
        # Read the image file as bytes
        with open(file_open, "rb") as file:
            image_data150 = file.read()
    image_open1=Image.open(file_open)
    image_open=image_open1.resize((150,150))
    tk_image = PhotoImage(image_open)
    
    # Convert image to Bytes format
    image_bytes = image_open.tobytes()
    

    # Update the label with the new image
    profile_image.config(image=tk_image)
    profile_image.image = tk_image
    mydb15=client['1122']
    mycol7=mydb15.list_collection_names()
    mycol7=mydb15[mycol7[0]]
    result7= mycol7.find_one({}, {'_id': 0, 'username': 1, 'phoneno': 1})
    print(result7)

    # Specify the update criteria (e.g., based on a unique identifier)
    t2=result7['username']

    print(t2)
    print(type(t2))
    filter_criteria = {'username': t2}

    # Define the update operation (e.g., updating a specific field)
    update_operation = {'$set': {'image':image_data150 }}

    # Perform the update operation on a single document
    result5 = mycol7.update_one(filter_criteria, update_operation)

Button(windows2,text="upload profile", command=open_image,cursor='hand2',border=0,font=('Microsoft Yahei UI Light',11)).place(x=20,y=250)
profile_image = Label(windows2)
profile_image.place(x=20,y=40)

def sam():
    global ten5
    if ten5==1:
        file=PhotoImage(file=image_data150)
        p=Label(windows2,image=file,border=0 ,width=650 ,height=406)
        p.place()


#if result:
   # print("username:", result['username'])
  #  print("phonenumber:", result['image'])
#filter_criteria = {'username': result['username']}
##update_operation = {'$set': {'image': 1}}

    # Perform the update operation on a single document
#result5 = mycol.update_one(filter_criteria, update_operation)



   

'''name='7702837610'
s='ganesh'
x=mycol.find({'phonenumber':'7670922693'})
print(x)'''



''''dblist = client.list_database_names()
if '7702837610' in dblist:
    pass
else:
    mydb1=client['7702837610']
    mycol1=mydb1['ganesh']
    x={'phonenumber':'7670922693'}
    t= mycol1.insert_one(x)
dblist=client.list_database_names()
for i in dblist:
    print(i)
mdbs1=client['7702837610']
mycol1=mdbs1['ganesh']
for i in mycol1.find():
    print(mycol1[i])

mydbs=client.list_database_names()
if name in mydbs:
    mydbs1=client[name]
    mycol=mydbs1[s]
'''# Fetch data from the collection
#data = list(mycol.find())
# Fetch data from the collection, excluding the _id field'''
'''data = list(mycol.find({}, {"_id": 0}))

# Create a table instance
table = PrettyTable()

# Add table columns
table.field_names = data[0].keys()
# Create a string representation of the table
table_str = ""


# Add table rows
for document in data:
    table.add_row(document.values())

# Create a string representation of the table
table_str = table.get_string()

windows1 = Tk()

# Create a Text widget to display the table output
table_text = Text(windows1, width=80, height=20)
table_text.pack()

# Set the table output in the Text widget
table_text.insert("1.0", table_str)

#windows1.mainloop()'''

'''import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient



def display_data():
    windows2 = tk.Tk()
    windows2.title("MongoDB Data")

    frame = ttk.Frame(windows2)
    frame.pack(fill="both", expand=True)

    tree = ttk.Treeview(frame)
    tree["columns"] = tuple(mycol.find_one().keys())

    # Add columns to the Treeview
    for column in tree["columns"]:
        tree.heading(column, text=column)
        tree.column(column, width=100)

    # Retrieve data from MongoDB and insert into the Treeview
    for data in mycol.find():
        tree.insert("", "end", values=tuple(data.values()))

    tree.pack(fill="both", expand=True)


display_data()
'''


''''
def userdata_represent():
    global phoneno2, password2
    mydb=myclient[phoneno2]
    mycol=mydb.list_collection_names()
    mycol=mydb[mycol[0]]
    mycol = mycol.find_one({}, {'_id': 0, 'username': 1, 'phoneno': 1})
    
    if mycol:
        label5=Label(executionframe,bg="white",text="username  " + mycol['username'],font=('Microsoft Yahei UI Light',12,'bold'))
        label5.place(x=20,y=300)
        label6=Label(home,bg="white",text="phonenumber  " + mycol['phoneno'],font=('Microsoft Yahei UI Light',12,'bold'))
        label6.place(x=20,y=330)





'''''''''





