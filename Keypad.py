from tkinter import *
import pdb

root = Tk()

user_input = Entry(root, width=30, borderwidth=5)
user_input.grid(row=0,columnspan=4,padx=5,pady=5)


def insertion(n):
    user_input.insert(0,str(n))

Button(root,padx=12,pady=12,text="C").grid(column=0,row=1)
Button(root,padx=85,pady=12,text="=").grid(column=1,row=1,columnspan=3)

col = 2
ro = 5
num = 9
nums = list(range(0,10))
#Number pad
'''
Need to find a way to make it so each number button is assigned its own unique value
'''

for i in nums:
    #pdb.set_trace()
    if i == 0:
        col = 1
        Button(root, padx=12, pady=12, text=str(0),command=lambda: insertion(0)).grid(column=col,row=ro)
        ro-=1
        col=0
    else:
        Button(root, padx=12, pady=12, text=str(nums[i]),command=lambda: insertion(nums.pop())).grid(column=col,row=ro)
        col += 1
        if col == 3:
            col = 0
            ro-=1

#Operations
ro2=2

for sign in ["+","-","÷","x"]:
    Button(root, padx=12, pady=12, text=sign).grid(column=3,row=ro2)
    ro2+=1


root.mainloop()