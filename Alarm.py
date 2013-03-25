from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import RPi.GPIO as GPIO
import time


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
#GPIO.output(15, False)
#GPIO.output(11, False)

AlarmTriggered = False
AlarmStatus = "Off"
AlarmCode = "2222"
MotionDetected = False
Flash = True



def redLED(pin, mode):
        GPIO.output(pin, mode)
def greenLED(pin, mode):
        GPIO.output(pin, mode)
def enableCode(code_entry, sensor_option, root):
        global sensorChoice
        global AlarmStatus
        global userEntered
        userEntered = (code_entry.get())
        print(userEntered)
        code_entry.delete(0, END)
        if (userEntered == AlarmCode) and (AlarmStatus == "Off"):
                tkinter.messagebox.showinfo("Alarm Code","Code Accepted, enabling alarm.")
                AlarmStatus = "On"
                print(AlarmStatus)
                sensorChoice = (sensor_option.get())
                print(sensorChoice)
                alarmActive(root)
        elif (userEntered == AlarmCode) and (AlarmStatus == "On"):
                tkinter.messagebox.showinfo("Alarm Code","Alarm is already activated")
        elif len(userEntered) <4:
                tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
        else:
                tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")
                
def disableCode(code_entry):
        global AlarmStatus
        global userEntered
        userEntered = (code_entry.get())
        print(userEntered)
        code_entry.delete(0, END)
        if (userEntered == AlarmCode) and (AlarmStatus == "On"):
                tkinter.messagebox.showinfo("Alarm Code","Code Aceepted, Disabling alarm")
                AlarmStatus = "Off"
                alarmDisable(11, TRUE)
        elif (userEntered == AlarmCode) and (AlarmStatus == "Off"):
                tkinter.messagebox.showwarning("Alarm Code", "Unable to disable alarm. Alarm is not enabled.")
        elif len(userEntered) <4:
                tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
        else: 
                tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")


def getOption(sensor_option):
        global sensorChoice
        sensorChoice =(sensor_option.get())


def alarmActive(root,period=0):
        redLED(11, FALSE)
        global Flash
        while (period <30) and (AlarmStatus is "On"):
                if (Flash is True):
                        greenLED(15, FALSE)
                        Flash = False
                        break
                elif (Flash is False):
                        greenLED(15, TRUE)
                        Flash = True
                        break
                else:
                        break
        if (period <30) and (AlarmStatus == "On"):
                period +=1
                print(period)
                root.after(500, lambda: alarmActive(root, period))
        elif (AlarmStatus == "Off"):
                print("Alarm has been disabled before activation")
                
        else:
                #cleanGPIO()
                greenLED(15, TRUE)
                print("Alarm now active")
                #sensorListen(root)
                
               
def alarmDisable(pin, mode):
        print ("Alarm Disabled")
        greenLED(15, FALSE)
        redLED(pin, mode)

##def sensorListen(root):
##                if (sensorChoice == "Both"):
##                        MotionDetected = True
##                        print("Motion Detected")
##                        root.after(1000, lambda: sensorListen(root))
##                elif (sensorChoice == "Front"):
##                        MotionDetected = True
##                elif (sensorChoice == "Back"):
##                        MotionDetected = True
##                else:
##                        print("Error alarm")
                        
                        
        

##def flashLED(root, pin, period=0):
##        if (period <15) and (AlarmStatus == "On"):
##                GPIO.output(pin, True)
##                after(500)
##                GPIO.output(pin, False)
##                time.sleep(1)
##                period +=1
##                print(period)
##                root.after(500, lambda: alarmActive(root, period))
##        elif (AlarmStatus == "Off"):
##                print("Alarm has been disabled")
##        else:
##                GPIO.output(pin, True)
##                        
