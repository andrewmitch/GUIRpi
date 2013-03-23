#!/usr/bin/env python
# Python 3
from tkinter import *
from tkinter import ttk

def one():
	code_entry.insert(END,"1")
def two():
	code_entry.insert(END,"2")
def three():
	code_entry.insert(END,"3")
def four():
	code_entry.insert(END,"4")
def five():
	code_entry.insert(END,"5")
def six():
	code_entry.insert(END,"6")
def seven():
	code_entry.insert(END,"7")
def eight():
	code_entry.insert(END,"8")
def nine():
	code_entry.insert(END,"9")
def zero():
	code_entry.insert(END,"0")
def clear():
	code_entry.delete(0, END)
def delete():
	start = len(code_entry.get()) -1
	code_entry.delete(start, END)
	

def getCode():
	global userEntered
	userEntered = (code_entry.get())
	print(userEntered)
	if (userEntered == AlarmCode):
		tkinter.messagebox.showinfo("Alarm Code","Code Aceepted" )
	elif len(userEntered) <4:
		tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
	else:
		tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")
    