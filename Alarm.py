from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, False)
GPIO.output(11, False)

AlarmCode = "2222"

def getCode(code_entry):
	global userEntered
	userEntered = (code_entry.get())
	print(userEntered)
	code_entry.delete(0, END)
	if (userEntered == AlarmCode):
		tkinter.messagebox.showinfo("Alarm Code","Code Aceepted" )
		alarmActive()
	elif len(userEntered) <4:
		tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
	else:
		tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")

def getOption(sensor_option):
	global sensorChoice
	sensorChoice =(sensor_option.get())
	print(sensorChoice)

def alarmActive():
        period = 0
        while True:
                if period <=15:
                        GPIO.output(15, True)
                        time.sleep(1)
                        GPIO.output(15, False)
                        time.sleep(1)
                        period +=1
                        print(period)
                else:
                        GPIO.output(15, True)
                        
