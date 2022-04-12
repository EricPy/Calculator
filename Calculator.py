from tkinter import *
import pdb

root = Tk()
root.title("Simple Calculator")

user_input = Entry(root, width=30, borderwidth=5,)
user_input.grid(row=0,columnspan=4,padx=5,pady=5)

#Button functions

def insertion(n):
    user_input.insert(len(user_input.get()),str(n))

def c():
    user_input.delete(0,END)
    nums = []

def clear():
    user_input.delete(0,END)

def parantheses():
    
    parant_open = []
    parant_close = []

    for item in user_input.get():
        if item == "(":
            parant_open.append(item)
        elif item == ")":
            parant_close.append(item)

    if len(parant_open) > len(parant_close):
        insertion(")")
    else:
        insertion("(")
    
def backspace():

    saved = user_input.get()

    clear()

    insertion(saved[:-1])

def equal():
    equation = ''
    for el in user_input.get():
        if el == "÷":
            equation+= "/"
        elif el == "×":
            equation+="*"
        else:
            equation+=el

    clear()

    result = eval(equation)

    if str(result)[-2::] == ".0":
        result = int(result)

    insertion(result)

'''
LOGIC
- you type in number with the operations
- it turns into a string that eval understands
- inserts eval result

'''

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

button0 = Button(root, padx=12, pady=12, text=str(0),command=lambda: insertion(0)).grid(column=1,row=5)

#Operations
button_clear=Button(root,padx=12,pady=12,text="C",command=c).grid(column=0,row=1)
button_equal=Button(root,padx=50,pady=12,text="=",command=equal).grid(column=2,row=1,columnspan=2)

button_add = Button(root, padx=12, pady=12, text="+",command=lambda: insertion("+")).grid(column=3,row=2)
button_subtract = Button(root, padx=12, pady=12, text="-",command=lambda: insertion("-")).grid(column=3,row=3)
button_div = Button(root, padx=12, pady=12, text="÷",command=lambda: insertion("÷")).grid(column=3,row=4)
button_mult = Button(root, padx=12, pady=12, text="×",command=lambda: insertion("×")).grid(column=3,row=5)

button_dec = Button(root, padx=13, pady=12, text=".",command=lambda: insertion(".")).grid(column=0,row=5)
button_paran = Button(root, padx=9, pady=12, text="( )",command=parantheses).grid(column=2,row=5)
button_back = Button(root, padx=8, pady=12, text="⌫",command=backspace).grid(column=1,row=1)

root.mainloop()