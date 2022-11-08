from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import os
from code import dict as ap
from PIL import ImageTk, Image

# click utility for submit button
def click():
    name = str(entryname.get()).upper()
   
    if name in ap:

        total_working_days = 24
        total_present_days = ap[name][0]
        attendance_precentage = ap[name][2]

# ((((IMPORTANT BUTTON XD))))
        # for clear button
        labelname.delete(0, END)
        labelwork.delete(0, END)
        labelpresent.delete(0, END)
        labelpercent.delete(0, END)
        

        labelname.insert(0, name)
        labelwork.insert(0, total_working_days)
        labelpresent.insert(0, total_present_days)
        labelpercent.insert(0, attendance_precentage)

    elif name != "":
      labelname.delete(0, END)
      labelwork.delete(0, END)
      labelpresent.delete(0, END)
      labelpercent.delete(0, END)

      labelname.insert(0, "Wrong Person")
      labelwork.insert(0, "NA")
      labelpresent.insert(0, "NA")
      labelpercent.insert(0, "NA")


# erase utility for erase button
def erase():
    entryname.delete(0, END)
    labelname.delete(0, END)
    labelwork.delete(0, END)
    labelpresent.delete(0, END)
    labelpercent.delete(0, END)



root = Tk()

root.geometry("500x300")
root.title("ATTENDENCE REPORT")

# HEADING PART
# 1.creating the heading bar for our gui
heading = Frame(root, bg="pink", relief="sunken", border=1)
heading.pack(side="top", fill="x")

canvas = Canvas(root, width = 1000, height = 200)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("msd.jpg"))
canvas.create_image(5,5, anchor=NW, image = img)


# 1.1 putting label in frame(heading)
sidelabel = Label(heading, text="Let's See The Attendance Record of Persons",
                  font="Heather", border=12, padx=50, bg="pink", fg="black")
sidelabel.pack(side="top")

# INPUT DETAILS PART
# 2.1 configuing column and dividing in the ratio of 1 : 2
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
# 2.2 creating Frame to for user input name
nameframe = Frame(root, bg="purple", border=5,
                  relief="sunken", width=20, padx=20, pady=80)
nameframe.pack(side="left", anchor="sw", fill="y")

nameframe.columnconfigure(0, weight=1)
nameframe.columnconfigure(1, weight=3)

# 2.3 create label for name
name = Label(nameframe, text="Tpye_name", font="sans 18 bold",
             border=3, bg="white", fg="black")
name.grid(column=0, row=0, sticky=W, padx=14, pady=35)

# take user input using entry option
entryname = Entry(nameframe, border=3, relief="sunken",
                  width=30, font="Tahoma 15", fg="dark red")
entryname.grid(column=1, row=0, sticky=E, padx=14, pady=35)

#2.6 create label for year
# year = Label(nameframe, text="Current Year", font="sans 18 bold",
#              border=3, bg="white", fg="black")
# year.grid(column=0, row=3, sticky=W, padx=14, pady=20)

# take user input for year
# entryyear = Entry(nameframe, border=3, relief="sunken",
#                   width=30, font="Tahoma 15", fg="dark red")
# entryyear.grid(column=1, row=3, sticky=E, padx=14, pady=35)

#2.7 clear button
# clear_button = Button(nameframe, text="Clear", font="serif 12 bold",
#                       border=5, relief="raised", width=10, command=erase)
# clear_button.grid(column=0, row=6, sticky=W, padx=14, pady=5)

#2.8 login button
login_button = Button(nameframe, text="Are you Sure!", font="serif 12 bold",
                      border=5, relief="raised", width=10, command=click)
login_button.grid(column=1, row=6, sticky=E, padx=14, pady=5)

# 3 DISPLAY FRAME
# 3.1 creating frame
photoframe = Frame(root, bg="black", relief="ridge", width=500)
photoframe.pack(side="top", anchor="ne", padx=10, pady=10, fill="x")


subheading = Label(photoframe, text="You can see the Output, Its Correct!", padx=50,
                   pady=50, font="couriernew 30 bold", bg="violet", fg="black",)
subheading.pack(side="left", anchor="nw")


deatilsframe = Frame(root, bg="purple", relief="sunken",
                     border=500, borderwidth=50)
deatilsframe.pack(side="left", anchor="ne", fill="both")

deatilsframe.columnconfigure(0, weight=1)
deatilsframe.columnconfigure(1, weight=4)

#3.3.1 Creating label to display names
namelabel = Label(deatilsframe, text="Name",
                  font="Tahoma 15 bold", border=3, padx=10, pady=5, relief="raised")
namelabel.grid(column=0, row=0, sticky=W, padx=14, pady=20)

labelname = Entry(deatilsframe, relief="sunken",
                  width=56, font="Tahoma 15", fg="red")
labelname.grid(column=3, row=0, sticky=E, padx=16, pady=10)

totworking = Label(deatilsframe, text="Total Classes",
                   font="Tahoma 15 bold", border=3, padx=10, pady=5, relief="raised")
totworking.grid(column=0, row=3, sticky=W, padx=14, pady=20)

labelwork = Entry(deatilsframe, border=3, relief="sunken",
                  width=56, font="Tahoma 15", fg="red")
labelwork.grid(column=3, row=3, sticky=E, padx=16, pady=10)

# 3.3.5 Creating label to display days present
totpresent = Label(deatilsframe, text="Present",
                   font="Tahoma 15 bold", border=2, padx=10, pady=5, relief="raised")
totpresent.grid(column=0, row=4, sticky=W, padx=14, pady=20)

labelpresent = Entry(deatilsframe, border=2, relief="sunken",
                     width=56, font="Tahoma 15", fg="red")
labelpresent.grid(column=3, row=4, sticky=E, padx=16, pady=10)

# 3.3.6 Creating label for Attendance percentage
totattendance = Label(deatilsframe, text="Percentage ",
                      font="Tahoma 15 bold", border=3, padx=10, pady=5, relief="raised")
totattendance.grid(column=0, row=5, sticky=W, padx=14, pady=20)

labelpercent = Entry(deatilsframe, border=3, relief="sunken",
                     width=56, font="Tahoma 15", fg="red")
labelpercent.grid(column=3, row=5, sticky=E, padx=16, pady=10)


root.mainloop()
