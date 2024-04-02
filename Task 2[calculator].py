#importing tkinter library
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window=tk.Tk()
window.title('My Calci')
frame=tk.Frame(master=window,bg="skyblue",padx=10)
frame.pack()
entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=30)
entry.grid(row=0,column=0,columnspan=4,ipady=2,pady=2)

#define myclick function to get the input from the user

def myclick(number):
     entry.insert(tk.END,number)

#define an equal function to evaluate the value
# try-except is use to handle the error

def equal():
 try:
    y = str(eval(entry.get()))
    entry.delete(0,tk.END)
    entry.insert(0,y)
 except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

#define clear function to delete the previous inputs

def clear():
    entry.delete(0,tk.END)

# Buttons for the First Row
# 9, 8, 7, +

button_1=tk.Button(master=frame,text='9',padx=15,pady=5,width=3,command=lambda:myclick(9))
button_1.grid(row=1,column=0,pady=2)

button_2=tk.Button(master=frame,text='8',padx=15,pady=5,width=3,command=lambda:myclick(8))
button_2.grid(row=1,column=1,pady=2)

button_3=tk.Button(master=frame,text='7',padx=15,pady=5,width=3,command=lambda:myclick(7))
button_3.grid(row=1,column=2,pady=2)

#addition button (+)
button_add=tk.Button(master=frame,text="+",padx=15,pady=5,width=3,command=lambda:myclick('+'))
button_add.grid(row=1,column=3,pady=2)


#buttons for the second row
# 6, 5, 4, -

button_4=tk.Button(master=frame,text='6',padx=15,pady=5,width=3,command=lambda:myclick(6))
button_4.grid(row=2,column=0,pady=2)

button_5=tk.Button(master=frame,text='5',padx=15,pady=5,width=3,command=lambda:myclick(5))
button_5.grid(row=2,column=1,pady=2)

button_6=tk.Button(master=frame,text='4',padx=15,pady=5,width=3,command=lambda:myclick(4))
button_6.grid(row=2,column=2,pady=2)

#subtraction button (-)
button_subtract=tk.Button(master=frame,text="-",padx=15,pady=5,width=3,command=lambda:myclick('-'))
button_subtract.grid(row=2,column=3,pady=2)


#buttons for the third row
# 3, 2, 1, and *

button_7=tk.Button(master=frame,text='3',padx=15,pady=5,width=3,command=lambda:myclick(3))
button_7.grid(row=3,column=0,pady=2)

button_8=tk.Button(master=frame,text='2',padx=15,pady=5,width=3,command=lambda:myclick(2))
button_8.grid(row=3,column=1,pady=2)

button_9=tk.Button(master=frame,text='1',padx=15,pady=5,width=3,command=lambda:myclick(1))
button_9.grid(row=3,column=2,pady=2)

#multiply button (*)
button_multiply=tk.Button(master=frame,text="*",padx=15,pady=5,width=3,command=lambda:myclick('*'))
button_multiply.grid(row=3,column=3,pady=2)


#buttons for the fourth row
# clear, 0, equal, and /

#clear button
button_clear=tk.Button(master=frame,text="C",padx=15,pady=5,width=3,command=clear)
button_clear.grid(row=4,column=0,pady=2)

# 0 button
button_0=tk.Button(master=frame,text='0',padx=15,pady=5,width=3,command=lambda:myclick(0))
button_0.grid(row=4,column=1,pady=2)

#equal button
button_equal=tk.Button(master=frame,text="=",padx=15,pady=5,width=3,command=equal)
button_equal.grid(row=4,column=2,pady=2)

#division button (/)
button_div=tk.Button(master=frame,text="/",padx=15,pady=5,width=3,command=lambda:myclick('/'))
button_div.grid(row=4,column=3,pady=2)


window.mainloop()