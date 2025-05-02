#imports
import random
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#file settings
__author__ = "James Pink-Gyett"
__copyright__ = "Copyright 2025, James Pink-Gyett"
root = tk.Tk()
bgcolour = "#808080"
hlcolour = "#595959"
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg=bgcolour)
root.resizable(False, False) 

#functions

#password generation function
def execute():
    length = lengthVar.get()
    uppercase = uppercaseVar.get()
    lowercase = lowercaseVar.get()
    specialchar = specialcharVar.get()
    list = ""
    password = output.cget("text")
    
    if uppercase == False and lowercase == False and specialchar == False:
        output.config(text="Please select at least one option.")
        return
    else:
        if uppercase == True:
            list += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if lowercase == True:
            list += "abcdefghijklmnopqrstuvwxyz"
        if specialchar == True:
            list += "!?#.-_"
        
        password = "".join([random.choice(list) for _ in range(length)])
        output.config(text=password)
        outputlabel.config(text="Click to copy to clipboard.")

    

def copytoclipb():
    password = output.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    outputlabel.config(text="Password copied to clipboard.")

lengthVar = tk.IntVar()
uppercaseVar = tk.BooleanVar()
lowercaseVar = tk.BooleanVar()
specialcharVar = tk.BooleanVar()

title = tk.Label(root, text="Password Generator", bg=bgcolour, font=("bold", 30))
title.pack(pady=10)

sliderlabel = tk.Label(root, text="How many characters would you like in your password?", bg=bgcolour)
sliderlabel.pack()
lengthslider = tk.Scale(root, bg=bgcolour, highlightthickness="0px", length="200px", from_=8, to=30, orient=tk.HORIZONTAL, variable=lengthVar)
lengthslider.pack(pady=10)

uppercaseCb = tk.Checkbutton(root, text="Include uppercase letters (ABC)?", bg=bgcolour, variable=uppercaseVar)
uppercaseCb.pack()

lowercaseCb = tk.Checkbutton(root, text="Include lowercase letters (abc)?", bg=bgcolour, variable=lowercaseVar)
lowercaseCb.pack()

specialcharCb = tk.Checkbutton(root, text="Include special characters (!?#.-_)?", bg=bgcolour, variable=specialcharVar)
specialcharCb.pack()

submitBtn = tk.Button(root, text="Generate Password", bg=bgcolour, height=2, width=30, font=("bold", 10), command=execute)
submitBtn.pack(pady=10)

output = tk.Button(root, text="...", bg=hlcolour, width=40, command=copytoclipb)
output.pack(pady=20)
outputlabel = tk.Label(root, text="Click to copy to clipboard.", bg=bgcolour)
outputlabel.pack()



root.mainloop()