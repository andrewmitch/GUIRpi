from tkinter import *
from tkinter import ttk
from Entry import ConstrainedEntry
import tkinter.messagebox


AlarmCode = "1234"

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
code_entry.grid(columnspan = 2, column=2, row=5, sticky=(W, E))

#Add buttons to frame using grid layout
ttk.Button(mainframe, text="1", command =one).grid(column=1, row=1, sticky=NW)
ttk.Button(mainframe, text="2").grid(column=2, row=1, sticky=NW)
ttk.Button(mainframe, text="3").grid(column=3, row=1, sticky=NW)
ttk.Button(mainframe, text="4").grid(column=1, row=2, sticky=NW)
ttk.Button(mainframe, text="5").grid(column=2, row=2, sticky=NW)
ttk.Button(mainframe, text="6").grid(column=3, row=2, sticky=NW)
ttk.Button(mainframe, text="7").grid(column=1, row=3, sticky=NW)
ttk.Button(mainframe, text="8").grid(column=2, row=3, sticky=NW)
ttk.Button(mainframe, text="9").grid(column=3, row=3, sticky=NW)
ttk.Button(mainframe, text="Clear").grid(column=1, row=4, sticky=NW)
ttk.Button(mainframe, text="0").grid(column=2, row=4, sticky=NW)
ttk.Button(mainframe, text="Delete").grid(column=3, row=4, sticky=NW)

ttk.Button(mainframe, text="OK", command =getCode).grid(column=5, row=5, sticky=SE)
ttk.Button(mainframe, text="Cancel").grid(column=6, row=5, sticky=SE)

ttk.Label(mainframe, text="Enter Code:").grid(column=1, row=5, sticky=W)




for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()

