from tkinter import *
from  tkinter import  ttk
from PIL import ImageTk, Image
import tkinter as tk
main_screen = Tk()
#main_screen.iconbitmap('images\add-user.png')

image = PhotoImage('images')


main_screen.geometry("800x550")
main_screen.resizable(0, 0)

#functions for butons
def add_user():
    main_screen.destroy()
    import new
    new.Registrationform()

def delete():
    main_screen.destroy()
    import delete
    delete.Registrationform()

def update():
    main_screen.destroy()
    import update
    update.Registrationform()

def cancel():
    main_screen.destroy()

#frame
frame_1 = tk.Frame(main_screen, bg='#90ee90',width=800,height=550)
frame_1.pack()
frame_1.pack_propagate(0)

#text labels
label1 = Label(main_screen,text="DASHBOARD", width=20,height=3, bg='#90ee90',font='Helvetica 14 bold')
label1.place(x=150,y=0)
#footer
label1 = Label(main_screen,text="© Kamati Group 2021", width=50,height=3, bg='#90ee90',font='Helvetica 12 bold')
label1.place(x=150,y=490)


#add label
#label2 = Label(main_screen,text="Add user", width=30,height=3, bg='#FF0000',font='Helvetica 12 bold')
#label2.place(x=35,y=250)
#add button
img = ImageTk.PhotoImage(Image.open(r"images\follow.png"))
Button(main_screen,width=300, height=200,bg='#ffffff', image=img, borderwidth=0, command=add_user).place(x=30,y=65)

image1 = ImageTk.PhotoImage(Image.open(r"images\delete.png"))
Button(main_screen,width=300, height=200,bg='#ffffff', image=image1, borderwidth=0, command=delete).place(x=400,y=65)

image2 = ImageTk.PhotoImage(Image.open(r"images\exchange.png"))
Button(main_screen,width=300, height=200, image=image2,bg='#ffffff', borderwidth=0, command=update).place(x=30,y=300)

image3 = ImageTk.PhotoImage(Image.open(r"images\x-button.png"))
Button(main_screen,width=300, height=200, image=image3,bg='#ffffff', borderwidth=0, command=cancel).place(x=400,y=300)


main_screen.mainloop()