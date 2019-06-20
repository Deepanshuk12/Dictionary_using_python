import sqlite3 as sql
import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
root.title("Student Management System")

Head = tk.Label(root, text="Student Management System",
                font=("Verdana 18 bold underline"),
                justify=CENTER, padx=50).pack()

Name = tk.Label(root, text="Enter Student Name", font=("Verdana 10 bold"), pady=10).pack()
nameEntry = tk.Entry(root)
nameEntry.pack()

Roll = tk.Label(root, text="Enter Student Roll Number", font=("Verdana 10 bold"), pady=10).pack()
rollEntry = tk.Entry(root)

rollEntry.pack()

Branch = tk.Label(root, text="Enter Branch", font=("Verdana 10 bold"), pady=10).pack()

branchEntry = tk.Entry(root)
branchEntry.grid(row=2,column=2)

Address = tk.Label(root, text="Enter Student Address", font=("Verdana 10 bold"), pady=10).pack()
addressEntry = tk.Entry(root)
addressEntry.pack()



buttonShow1 = tk.Button(root, text="Reset Field",
                       command=lambda: Reset()).pack(side=LEFT,padx=100,pady=5)

buttonNew2 = tk.Button(root, text="New Student",
                      command=lambda: New()).pack(side=LEFT,padx=100,pady=5)




Show_value = tk.Label(root, text="Enter Roll Number to fetch detail", font=("Verdana 10 bold"), pady=10).pack()
roll_show=tk.Entry(root)
roll_show.pack()

buttonShow3 = tk.Button(root, text="Show Details",
                       command=lambda: Show()).pack(pady =30,)


Show_value1 = tk.Label(root, text="", font=("Verdana 10 bold"), pady=10)
Show_value1.pack()



TABLE_NAME = 'student_table'
STUDENT_Id = 'student_id'
STUDENT_NAME = 'student_name'
STUDENT_BRANCH = 'student_branch'
STUDENT_ROLL= 'student_roll'
STUDENT_ADDRESS = 'student_address'


def Create():
    connection = sql.connect("student.db")
    messagebox.showinfo("Information","Table is created")
    connection.execute(
        "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + "(" + STUDENT_Id + "  INTEGER PRIMARY KEY AUTOINCREMENT , "
        + STUDENT_NAME + " TEXT , " + STUDENT_BRANCH + " TEXT  , " + STUDENT_ROLL +
        " INTEGER, " + STUDENT_ADDRESS + " TEXT);")


def New():

    if nameEntry.index("end") == 0 or branchEntry.index("end") == 0 or rollEntry.index("end")==0 or addressEntry.index("end")==0:
        messagebox.showerror("Error","Field cant be empty.Fill all the fields")

    else:
        Create()
        nameEntry1=str(nameEntry.get())
        branchEntry1=str(branchEntry.get())
        addressEntry1=str(addressEntry.get())
        rollEntry1=str(rollEntry.get())

        connection = sql.connect("Student.db")
        connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_BRANCH + ", " + STUDENT_ADDRESS +
            ", " + STUDENT_ROLL + " ) VALUES ('" + nameEntry1 + "' ,'" + branchEntry1 + "' , '" + addressEntry1 + "' , " + rollEntry1 + " );")

        messagebox.showinfo("Information", "Data Inserted")
        connection.commit()


def Show():
    connection=sql.connect("Student.db")
    roll_show1=str(roll_show.get())
    result = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE  " + STUDENT_ROLL + " = " +roll_show1)
    for row in result:
        ID=str(row[0])
        name=str(row[1])
        branch=str(row[2])
        roll=str(row[3])
        address=str(row[4])

    Show_value1.config(text="Student ID :" +ID+ "\nName : "  +name + " \n Branch : "+branch+ "\nRoll Number : "+str(roll)+ "\nAddress : "+address ,justify=LEFT)


def Reset():
        nameEntry.delete(0, END)
        nameEntry.insert(0, "")

        branchEntry.delete(0, END)
        branchEntry.insert(0, "")

        addressEntry.delete(0, END)
        addressEntry.insert(0, "")

        rollEntry.delete(0, END)
        rollEntry.insert(0, "")

        messagebox.showinfo("Information", "All field area empty now")





root.mainloop()
