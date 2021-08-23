from tkinter import *
from  tkinter import  ttk
from PIL import ImageTk, Image
from db import *


#importing connection
#import  mysql.connector as mc
#establishing connection
#conn = mc.connect(
#   user='root', password='', host='localhost', database='classWork')

def back_button():
    del_screen.destroy()
    import main
    main.Registrationform()

#defining register function
def delete():
    #getting form data
    name1=firstname.get()
    name2=secondname.get()
    name3=sirname.get()

    #applying empty validation
    if name1=='' or name2==''or name3=='':
        message.set("fill the empty field!!!")
    else:
       #Creating a cursor object using the cursor() method
       cursor = mydb.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = "DELETE FROM student WHERE firstName=%s && secondName=%s && sirName=%s"
       value = (name1, name2, name3,)
        
       
       try:
           #executing the sql command
           cursor.execute(insert_stmt,value)
           #commit changes in database
           mydb.commit()
       except:
           mydb.rollback()
       message.set("Deleted successfully")
       firstname.set('')
       secondname.set('')
       sirname.set('')

#defining Registrationform function
def Registrationform():
    global del_screen
    del_screen = Tk()
    #Setting title of screen
    del_screen.title("Registration Form")
    #setting height and width of screen
    del_screen.geometry("450x400")

    del_screen.resizable(0, 0)

    image = PhotoImage('images')
    #declaring variable
    global  message;
    global firstname
    global secondname
    global sirname
    global gender
    global coursetitle
    global coursecode
    global regnumber
    firstname = StringVar()
    secondname = StringVar()
    sirname = StringVar()
    message=StringVar()
    #Creating layout of Registration form
    Label(del_screen,width="300", text="Please Delete Entered details below", bg="orange",fg="white").pack()
    #name Label
    Label(del_screen, text="firstname * ").place(x=20,y=40)
    #name textbox
    Entry(del_screen, textvariable=firstname, width=40,border=2).place(x=90,y=42)
    #contact Label
    Label(del_screen, text="secondname* ").place(x=18,y=80)
    #contact textbox
    Entry(del_screen, textvariable=secondname, width=40,border=2).place(x=94,y=82)

    # email Label
    Label(del_screen, text="sirname * ").place(x=20, y=120)
    # email textbox
    Entry(del_screen, textvariable=sirname, width=40,border=2).place(x=90, y=122)

    #Label for displaying login status[success/failed]
    Label(del_screen, text="",textvariable=message).place(x=90,y=140)

    #Label for displaying login status[success/failed]
    img = ImageTk.PhotoImage(Image.open(r"images\del.jpg"))
    Button(del_screen,image=img, width=100, height=50,borderwidth=0,command=delete).place(x=300,y=160)

    img1 = ImageTk.PhotoImage(Image.open(r"images\back.jpg"))
    Button(del_screen,image=img1, width=100, height=50,borderwidth=0,command=back_button).place(x=10,y=160)

    del_screen.mainloop()
#calling function Registrationform
Registrationform()