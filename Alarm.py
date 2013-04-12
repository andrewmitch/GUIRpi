from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import RPi.GPIO as GPIO
import time


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)

AlarmTriggered = False
AlarmStatus = "Off"
AlarmCode = "2222"
#MotionDetected = False
Flash = True

##def flash(root):
##        if AlarmStatus == 'Off':
##                GPIO.output(15, True)
##                state = 'On'
##                root.after(100, flash)
##        else :
##                GPIO.output(11, False)
##                state = 'Off'
##                root.after(900, flash)

def redLED(pin, mode):
        GPIO.output(pin, mode)
        
def greenLED(pin, mode):
        GPIO.output(pin, mode)
        
def enableCode(code_entry, sensor_option, root):
        global sensorChoice
        global AlarmStatus
        global userEntered
        global AlarmTriggered
        userEntered = (code_entry.get())
        print(userEntered)
        code_entry.delete(0, END)
        if (userEntered == AlarmCode) and (AlarmStatus == "Off"):
                tkinter.messagebox.showinfo("Alarm Code","Code Accepted, enabling alarm.")
                AlarmStatus = "On"
                writeStatus(AlarmTriggered, AlarmStatus)
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
                tkinter.messagebox.showinfo("Alarm Code","Code Accepted, Disabling alarm")
                AlarmStatus = "Off"
                writeStatus(AlarmTriggered, AlarmStatus)
                alarmDisable(11, TRUE)
        elif (userEntered == AlarmCode) and (AlarmStatus == "Off"):
                tkinter.messagebox.showwarning("Alarm Code", "Unable to disable alarm. Alarm is not enabled.")
        elif len(userEntered) <4:
                tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
        else: 
                tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")


##def getOption(sensor_option):
##        global sensorChoice
##        sensorChoice =(sensor_option.get())


def alarmActive(root,period=0):
        global Flash
        redLED(11, FALSE)
        if(period <30) and (AlarmStatus is "On"):
                greenLED(15, Flash)
                Flash = not Flash
                period +=1
                print(period)
                root.after(500, lambda: alarmActive(root, period))
        elif (AlarmStatus == "Off"):
                print("Alarm disabled before activation")
                alarmDisable(11, TRUE)
        
        else:
                greenLED(15, TRUE)
                print("Alarm now active")
                alarmLive(root)
                
                
               
def alarmDisable(pin, mode):
        print ("Alarm Disabled")
        AlarmTriggered = False
        writeStatus(AlarmTriggered, AlarmStatus)
        greenLED(15, FALSE)
        redLED(pin, mode)

def alarmLive(root):
        global AlarmTriggered
        frontSensor = GPIO.input(16)
        backSensor = GPIO.input(18)
        while (AlarmStatus is 'On'):
                if (sensorChoice == 'Both') and (frontSensor is True) or (backSensor is True):
                        AlarmTriggered = True
                        break
                elif (sensorChoice == 'Front') and (frontSensor is True):
                        AlarmTriggered = True
                        break
                elif (sensorChoice == 'Back') and (backSensor is True):
                        AlarmTriggered = True
                        break
                else:
                        AlarmTriggered = False
                        break
        writeStatus(AlarmTriggered, AlarmStatus)
               
        if (AlarmTriggered is True):
                motionDetected(root)
        elif (AlarmStatus is 'On'):
                root.after(1000, lambda: alarmLive(root))
        
        elif (AlarmStatus == "Off"):
                alarmDisable(11, TRUE)

def motionDetected(root, period=0):
        global Flash
        if (AlarmStatus is 'On') and (period <15):
                period +=1
                print(period)
                root.after(1000, lambda: motionDetected(root, period))
        if (AlarmStatus is 'On') and (period >=15):
                redLED(11, Flash)
                Flash = not Flash
                period +=1
                print(period, '2')
                root.after(500, lambda: motionDetected(root, period))
        elif (AlarmStatus == "Off"):
                alarmDisable(11, TRUE)
                
                
                        
        
def writeStatus(AlarmTriggered, AlarmStatus):
        triggered = str(AlarmTriggered)
        status = str(AlarmStatus)
        try:
                f = open("alarm.txt", "w")
                try:
                        f.write(status + "\n" + triggered)
                finally:
                        f.close()
        except IOError:
                pass
        
        
        
        
        
        
        
        


                
                
        
