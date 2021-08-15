from tkinter import *
from  tkinter import  ttk


#importing connection
import  mariadb as mc
#establishing connection
conn = mc.connect(
   user='root', password='don', host='localhost', database='classWork')
   

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
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = "DELETE FROM student WHERE firstName=%s && secondName=%s && sirName=%s"
       value = (name1, name2, name3,)
        
       
       try:
           #executing the sql command
           cursor.execute(insert_stmt,value)
           #commit changes in database
           conn.commit()
       except:
           conn.rollback()
       message.set("Deleted successfully")
       firstname.set('')
       secondname.set('')
       sirname.set('')

#defining Registrationform function
def Registrationform():
    global del_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Registration Form")
    #setting height and width of screen
    reg_screen.geometry("450x400")
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
    Label(reg_screen,width="300", text="Please Delete Entered details below", bg="orange",fg="white").pack()
    #name Label
    Label(reg_screen, text="firstname * ").place(x=20,y=40)
    #name textbox
    Entry(reg_screen, textvariable=firstname, width=40,border=2).place(x=90,y=42)
    #contact Label
    Label(reg_screen, text="secondname* ").place(x=18,y=80)
    #contact textbox
    Entry(reg_screen, textvariable=secondname, width=40,border=2).place(x=94,y=82)

    # email Label
    Label(reg_screen, text="sirname * ").place(x=20, y=120)
    # email textbox
    Entry(reg_screen, textvariable=sirname, width=40,border=2).place(x=90, y=122)

    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",textvariable=message).place(x=90,y=140)

    #Label for displaying login status[success/failed]
    Button(reg_screen, text="Delete", width=10, height=1, bg="red",command=delete).place(x=90,y=160)

    reg_screen.mainloop()
#calling function Registrationform
Registrationform()