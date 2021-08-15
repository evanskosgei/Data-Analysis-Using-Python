from tkinter import *
from  tkinter import  ttk


#importing connection
import  mariadb as mc
#establishing connection
conn = mc.connect(
   user='root', password='don', host='localhost', database='classWork')

def back():
    reg_screen.destroy()
    import new
    new.Registrationform()
#function to clear entries
def search(): 
    search1 = searchitem.get()
    mycursor = conn.cursor()
    query ="SELECT * FROM student WHERE firstName='%s'"%searchitem.get()

    mycursor.execute(query)
    results = mycursor.fetchall()
    print(results)
    for result in results:
        firstname.set(result[1])
        secondname.set(result[2])
        sirname.set(result[3])
        coursetitle.set(result[5])
        coursecode.set(result[6])
        regnumber.set(result[7])
#defining register function
def update_fn():
    ##getting form data
    name1=firstname.get()
    name2=secondname.get()
    name3=sirname.get()
    coursetitle1=coursetitle.get()
    coursecode1=coursecode.get()
    regno= regnumber.get()
    #applying empty validation
    if name1=='' or name2==''or name3=='' or coursetitle1=='' or coursecode1==''or regno=='':
        message.set("fill the empty field!!!")
    else:
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt ="UPDATE student SET(firstName,secondName,sirName, course_title,  course_code, regNumber WHERE  firstName='%s'"%firstname.get()
       "VALUES (%s, %s, %s, %s, %s, %s)"
       value = (name1, name2, name3, coursetitle1, coursecode1,regno)
  
       try:
           #executing the sql command
           cursor.execute(insert_stmt,value)
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
def Update_details():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("UpdateForm")
    #setting height and width of screen
    reg_screen.geometry("450x500")
    #declaring variable
    global  message;
    global searchitem
    global firstname
    global secondname
    global sirname
    global gender
    global coursetitle
    global coursecode
    global regnumber
    firstname = StringVar()
    searchitem = StringVar()
    secondname = StringVar()
    sirname = StringVar()
    gender=IntVar()
    coursetitle=StringVar()
    coursecode=StringVar()
    regnumber=StringVar()
    message=StringVar()
    #Creating layout of Registration form
    Label(reg_screen,width="300", text="Please update details below", bg="orange",fg="white").pack()

    #search textbox
    Label(reg_screen, text="search item * ").place(x=20,y=30)
    #search textbox
    Entry(reg_screen, textvariable= searchitem, width=40,border=2).place(x=92,y=32)

    #firstname Label
    Label(reg_screen, text="firstname * ").place(x=20,y=70)
    #firstname textbox
    Entry(reg_screen, textvariable=firstname, width=40,border=2).place(x=90,y=72)
    #secondname Label
    Label(reg_screen, text="secondname* ").place(x=18,y=110)
    #secondname textbox
    Entry(reg_screen, textvariable=secondname, width=40,border=2).place(x=94,y=112)

    # sirname Label
    Label(reg_screen, text="sirname * ").place(x=20, y=150)
    # sirname textbox
    Entry(reg_screen, textvariable=sirname, width=40,border=2).place(x=90, y=152)

    
    #courseTitle
    Label(reg_screen, text="courseTitle * ").place(x=20, y=190)
    # coursetitle field
    Entry(reg_screen, textvariable=coursetitle, width=40,border=2).place(x=90, y=190)

    #coursecode
    Label(reg_screen, text="coursecode * ").place(x=20, y=230)
    # coursecode field
    Entry(reg_screen, textvariable=coursecode, width=40,border=2).place(x=92, y=232)

    #regnumber
    Label(reg_screen, text="regnumber * ").place(x=20, y=270)
    # regnumber field
    Entry(reg_screen, textvariable=regnumber, width=40,border=2).place(x=92, y=272)

 

    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",textvariable=message).place(x=95,y=294)
    #buttons
    Button(reg_screen, text="Save", width=10, height=1, bg="lightgreen",command=update_fn).place(x=200,y=320)

    #search button
    Button(reg_screen, text="Search", width=10, height=1, bg="lightgreen",command=search).place(x=350,y=30)

    Button(reg_screen, text="<back", width=10, height=1, bg="skyblue",command=back).place(x=0,y=320)

    reg_screen.mainloop()
#calling function Registrationform
Update_details()