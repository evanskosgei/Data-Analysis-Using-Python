from tkinter import *
from  tkinter import  ttk


#importing connection
import  mariadb as mc
#establishing connection
conn = mc.connect(
   user='root', password='don', host='localhost', database='classWork')

#open update page
def update():
    reg_screen.destroy()
    import update
    update.Update_details()
#open delete page
def delete():
    reg_screen.destroy()
    import delete
    delete.Registrationform()
#function to clear entries
def Clear():
    firstname.set('')
    secondname.set('')
    sirname.set('')
    coursetitle.set('')
    coursecode.set('')
    regnumber.set('')
    #reg_screen.quit()    

##defining register function
def register():
    #getting form data
    name1=firstname.get()
    name2=secondname.get()
    name3=sirname.get()
    gen1=gender.get()
    coursetitle1=coursetitle.get()
    coursecode1=coursecode.get()
    regno= regnumber.get()
    #applying empty validation
    if name1=='' or name2==''or name3=='' or gen1==''or coursetitle1=='' or coursecode1==''or regno=='':
        message.set("fill the empty field!!!")
    else:
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO student(firstName, secondName, sirName, gender, course_title, course_code, regNumber)"
           "VALUES (%s, %s, %s, %s, %s, %s,%s)"
       )
       if gen1==1:
        data = (name1, name2,name3,"Male",coursetitle1,coursecode1,regno)
       else:
        data = (name1, name2, name3,"Female", coursetitle1, coursecode1,regno)
       try:
           #executing the sql command
           cursor.execute(insert_stmt,data)
           #commit changes in database
           conn.commit()
       except:
           conn.rollback()
       message.set("Stored successfully")
       firstname.set('')
       secondname.set('')
       sirname.set('')
       coursetitle.set('')
       coursecode.set('')
       regnumber.set('')

#defining Registrationform function
def Registrationform():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Registration Form")
    #setting height and width of screen
    reg_screen.geometry("450x500")
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
    gender=IntVar()
    coursetitle=StringVar()
    coursecode=StringVar()
    regnumber=StringVar()
    message=StringVar()
    #Creating layout of Registration form
    Label(reg_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
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

    # gender Label
    Label(reg_screen, text="Gender * ").place(x=20, y=160)
    # gender radiobutton
    Radiobutton(reg_screen,text="Male",variable=gender,value=1).place(x=90,y=162)
    Radiobutton(reg_screen, text="Female", variable=gender, value=2).place(x=150, y=162)
    
    #courseTitle
    Label(reg_screen, text="courseTitle * ").place(x=20, y=200)
    # coursetitle field
    Entry(reg_screen, textvariable=coursetitle, width=40,border=2).place(x=90, y=202)

    #coursecode
    Label(reg_screen, text="coursecode * ").place(x=20, y=240)
    # coursecode field
    Entry(reg_screen, textvariable=coursecode, width=40,border=2).place(x=92, y=242)

    #regnumber
    Label(reg_screen, text="regnumber * ").place(x=20, y=280)
    # regnumber field
    Entry(reg_screen, textvariable=regnumber, width=40,border=2).place(x=92, y=280)

 

    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",textvariable=message).place(x=95,y=294)
    #Login button
    Button(reg_screen, text="Add", width=10, height=1,fg="white", bg="darkgreen",command=register).place(x=0,y=350)

    Button(reg_screen, text="Update", width=10, height=1, bg="skyblue",command=update).place(x=100,y=350)

    Button(reg_screen, text="Delete", width=10, height=1, bg="pink",command=delete).place(x=200,y=350)
    Button(reg_screen, text="Xcancel", width=10, height=1,fg="white", bg="red",command=Clear).place(x=300,y=350)


    reg_screen.mainloop()
#calling function Registrationform
Registrationform()