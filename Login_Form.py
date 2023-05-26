# -*- coding: utf-8 -*-
"""
Created on Tue May  9  2023

@author: Abhishek
"""
from tkinter import*
root=Tk()
root.geometry("400x300")
root.title("Login Form")
Label(root,text="Python Registration Form",font=('Arial',16,'bold')).grid(row=0,column=3)

name=Label(root,text='Name')
phone=Label(root,text='Phone No')
gender=Label(root,text='Gender')
emg=Label(root,text='Emergency')
payment=Label(root,text='Payment Mode')

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emg.grid(row=4,column=2)
payment.grid(row=5,column=2)

nameEntry=Entry(root)
phoneEntry=Entry(root)
genderEntry=Entry(root)
emgEntry=Entry(root)
paymentEntry=Entry(root)
checkbtn=Checkbutton(root,text="Remember me?")

nameEntry.grid(row=1,column=3)
phoneEntry.grid(row=2,column=3)
genderEntry.grid(row=3,column=3)
emgEntry.grid(row=4,column=3)
paymentEntry.grid(row=5,column=3)
checkbtn.grid(row=6,column=3)

btn=Button(root,text="Submit",font=(12))
btn.grid(row=7,column=3)



root.mainloop()