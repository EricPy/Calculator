from tkinter import *
import pdb

root = Tk()

user_input = Entry(root, width=30, borderwidth=5)
user_input.grid(row=0,columnspan=4,padx=5,pady=5)


def insertion(n):
    user_input.insert(-1,str(n))

Button(root,padx=12,pady=12,text="C").grid(column=0,row=1)
Button(root,padx=85,pady=12,text="=").grid(column=1,row=1,columnspan=3)

#Number pad
button7 = Button(root, padx=12, pady=12, text=str(7),command=lambda: insertion(7)).grid(column=0,row=2)
button8 = Button(root, padx=12, pady=12, text=str(8),command=lambda: insertion(8)).grid(column=1,row=2)
button9 = Button(root, padx=12, pady=12, text=str(9),command=lambda: insertion(9)).grid(column=2,row=2)

button4 = Button(root, padx=12, pady=12, text=str(4),command=lambda: insertion(4)).grid(column=0,row=3)
button5 = Button(root, padx=12, pady=12, text=str(5),command=lambda: insertion(5)).grid(column=1,row=3)
button6 = Button(root, padx=12, pady=12, text=str(6),command=lambda: insertion(6)).grid(column=2,row=3)

button1 = Button(root, padx=12, pady=12, text=str(1),command=lambda: insertion(1)).grid(column=0,row=4)
button2 = Button(root, padx=12, pady=12, text=str(2),command=lambda: insertion(2)).grid(column=1,row=4)
button3 = Button(root, padx=12, pady=12, text=str(3),command=lambda: insertion(3)).grid(column=2,row=4)


root.mainloop()