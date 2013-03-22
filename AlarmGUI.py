from tkinter import *
from tkinter import ttk
from Entry import ConstrainedEntry
import tkinter.messagebox


AlarmCode = "1234"

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
	if len(code_entry == 1):
		code_entry.delete(1)
	elif len(code_entry == 2):
		code_entry.delete(2)

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
    
root = Tk()
root.title("Alarm Interface")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

code_entered = IntVar()

#Add Entry field for  code data, calls class Constrained Entry for validation
code_entry= ConstrainedEntry(mainframe, width=7, textvariable=code_entered)
code_entry.delete(0, END)
code_entry.grid(columnspan = 2, column=2, row=5, sticky=(W, E))

#Add buttons to frame using grid layout
ttk.Button(mainframe, text="1", command=one).grid(column=1, row=1, sticky=NW)
ttk.Button(mainframe, text="2", command=two).grid(column=2, row=1, sticky=NW)
ttk.Button(mainframe, text="3", command=three).grid(column=3, row=1, sticky=NW)
ttk.Button(mainframe, text="4", command=four).grid(column=1, row=2, sticky=NW)
ttk.Button(mainframe, text="5", command=five).grid(column=2, row=2, sticky=NW)
ttk.Button(mainframe, text="6", command=six).grid(column=3, row=2, sticky=NW)
ttk.Button(mainframe, text="7", command=seven).grid(column=1, row=3, sticky=NW)
ttk.Button(mainframe, text="8", command=eight).grid(column=2, row=3, sticky=NW)
ttk.Button(mainframe, text="9", command=nine).grid(column=3, row=3, sticky=NW)
ttk.Button(mainframe, text="Clear", command = clear).grid(column=1, row=4, sticky=NW)
ttk.Button(mainframe, text="0", command=zero).grid(column=2, row=4, sticky=NW)
ttk.Button(mainframe, text="Delete", command=delete).grid(column=3, row=4, sticky=NW)

ttk.Button(mainframe, text="Disable Alarm", command =getCode).grid(column=5, row=4, sticky=E)
ttk.Button(mainframe, text="Enable Alarm").grid(column=5, row=5, sticky=SE)

ttk.Label(mainframe, text="Alarm Code:").grid(column=1, row=5, sticky=W)




for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()

