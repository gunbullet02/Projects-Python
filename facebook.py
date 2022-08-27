from logging import exception
import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
mydb = mysql.connector.connect(host="localhost", user="root", passwd="arya@123", database="form")
my_cursor = mydb.cursor()

root=Tk()
root.title("Facebook Login")
my_img=ImageTk.PhotoImage(Image.open("fb_login.png"))
my_label=Label(image=my_img)
my_label.pack()

def click():
    
    try:
        if fName.get()=="" or lName.get()=="" or email.get()=="" or password.get()=="" or reEmail.get()=="":
            raise exception
           
        insertSql="INSERT INTO users(fname, lname, email, pass, birthday, gender) VALUES(%s,%s,%s,%s,%s,%s)"
        record=(fName.get(),lName.get(),email.get(),password.get(),(birthdayYear.get()+"-"+birthdayMonth.get()+"-"+birthdayDay.get()),gender.get())
        my_cursor.execute(insertSql,record)
        mydb.commit()
        
        mssg= Label(root, bg="green", fg="white",text="Data inserted successfully...", width=20)
        mssg.place(x=0,y=498)
        
    except:
        
        mssg= Label(root, bg="orangered", fg="white",text="Data field error/s found...", width=20)
        mssg.place(x=0,y=498)
    
fName=Entry(root,width=27)
fName.place(x=725,y=202)
lName=Entry(root, width=27)
lName.place(x=725,y=239)
email=Entry(root, width=27)
email.place(x=725,y=276)
reEmail=Entry(root, width=27)
reEmail.place(x=725,y=313)
password=Entry(root, width=27)
password.place(x=725,y=350)

birthdayDay=Entry(root, width=5)
birthdayDay.place(x=807,y=419)
birthdayDay.insert(0,"1-31")

birthdayMonth=Entry(root, width=7)
birthdayMonth.place(x=725,y=419)
birthdayMonth.insert(0,"1-12")

birthdayYear=Entry(root, width=6)
birthdayYear.place(x=871,y=419)
birthdayYear.insert(0,"1905-2019")

gender = StringVar(root)
gender.set("Select sex")
s=["Male", "Female", "Others"]
drop_menu = OptionMenu(root, gender, *s)
drop_menu.place(x=725,y=387)

submitButton=Button(root,text="Sign Up",command=click, fg="green", padx=27, pady=5)
submitButton.place(x=724,y=474)

root.mainloop()