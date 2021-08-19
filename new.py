from tkinter import *
from  tkinter import  ttk
from PIL import ImageTk, Image


#importing connection
import  mariadb as mc
#establishing connection
conn = mc.connect(
   user='root', password='don', host='localhost', database='classWork')

def back():
    reg_screen.destroy()
    import main
    main.Registrationform()

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
    reg_screen.resizable(0, 0)

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
    gender=IntVar()
    coursetitle=StringVar()
    coursecode=StringVar()
    regnumber=StringVar()
    message=StringVar()
    #Creating layout of Registration form
    Label(reg_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()

    #image labels
    img = ImageTk.PhotoImage(Image.open(r"images\f1.png"))
    label1 = Label(reg_screen,image=img, width=100,height=100)
    label1.place(x=150,y=30)

    img1 = ImageTk.PhotoImage(Image.open(r"images\back.jpg"))
    Button(reg_screen,width=50, height=30,bg='#ffffff', image=img1, borderwidth=0, command=back).place(x=0,y=25)

    #name Label
    Label(reg_screen, text="firstname * ").place(x=20,y=140)
    #name textbox
    Entry(reg_screen, textvariable=firstname, width=40,border=2).place(x=90,y=142)
    #contact Label
    Label(reg_screen, text="secondname* ").place(x=18,y=180)
    #contact textbox
    Entry(reg_screen, textvariable=secondname, width=40,border=2).place(x=94,y=182)

    # email Label
    Label(reg_screen, text="sirname * ").place(x=20, y=220)
    # email textbox
    Entry(reg_screen, textvariable=sirname, width=40,border=2).place(x=90, y=222)

    # gender Label
    Label(reg_screen, text="Gender * ").place(x=20, y=260)
    # gender radiobutton
    Radiobutton(reg_screen,text="Male",variable=gender,value=1).place(x=90,y=262)
    Radiobutton(reg_screen, text="Female", variable=gender, value=2).place(x=150, y=262)
    
    #courseTitle
    Label(reg_screen, text="courseTitle * ").place(x=20, y=300)
    # coursetitle field
    Entry(reg_screen, textvariable=coursetitle, width=40,border=2).place(x=90, y=302)

    #coursecode
    Label(reg_screen, text="coursecode * ").place(x=20, y=340)
    # coursecode field
    Entry(reg_screen, textvariable=coursecode, width=40,border=2).place(x=92, y=342)

    #regnumber
    Label(reg_screen, text="regnumber * ").place(x=20, y=380)
    # regnumber field
    Entry(reg_screen, textvariable=regnumber, width=40,border=2).place(x=92, y=380)

 

    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",font='Helvetica 12 bold',textvariable=message).place(x=95,y=420)
    #Login button
    Button(reg_screen, text="Add",font='Helvetica 12 bold', width=10, height=1,fg="white", bg="darkgreen",command=register).place(x=300,y=450)
    Button(reg_screen, text="Xcancel",font='Helvetica 12 bold', width=10, height=1,fg="white", bg="red",command=Clear).place(x=50,y=450)


    reg_screen.mainloop()
#calling function Registrationform
Registrationform()