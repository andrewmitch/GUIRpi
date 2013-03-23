from tkinter import *
from tkinter import ttk
import tkinter.messagebox


AlarmCode = "2222"

def getCode(code_entry):
	global userEntered
	userEntered = (code_entry.get())
	print(userEntered)
	code_entry.delete(0, END)
	if (userEntered == AlarmCode):
		tkinter.messagebox.showinfo("Alarm Code","Code Aceepted" )
	elif len(userEntered) <4:
		tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
	else:
		tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")

def getOption(sensor_option):
	global sensorChoice
	sensorChoice =(sensor_option.get())
	print(sensorChoice)
