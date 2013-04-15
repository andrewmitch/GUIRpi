from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import RPi.GPIO as GPIO
import time

# Set up GPIO channels
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)

alarmTriggered = False
alarmStatus = "Off"
alarmCode = "2222"
flash = True

# GPIO red LED function, pass through pin and mode ('True or False')
def redLED(pin, mode):
        GPIO.output(pin, mode)

# GPIO green LED function, pass through pin and mode ('True or False')
def greenLED(pin, mode):
        GPIO.output(pin, mode)
        
# Function called when user hits 'Enable' button on code, which check if code entered matchs the above and display a message regarding the outcome        
def enableCode(code_entry, sensor_option, root):
        global sensorChoice
        global alarmStatus
        global userEntered
        global alarmTriggered
        userEntered = (code_entry.get())
        print(userEntered)
        code_entry.delete(0, END)
        if (userEntered == alarmCode) and (alarmStatus == "Off"):
                tkinter.messagebox.showinfo("Alarm Code","Code Accepted, enabling alarm.")
                alarmStatus = "On"
                writeStatus(alarmTriggered, alarmStatus)
                print(alarmStatus)
                sensorChoice = (sensor_option.get())
                print(sensorChoice)
                alarmActive(root)
        elif (userEntered == alarmCode) and (alarmStatus == "On"):
                tkinter.messagebox.showinfo("Alarm Code","Alarm is already activated")
        elif len(userEntered) <4:
                tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
        else:
                tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")
                
# Function for disbaling the alarm system, called when a user hits the 'Disable' button on the GUI                
def disableCode(code_entry):
        global alarmStatus
        global userEntered
        userEntered = (code_entry.get())
        print(userEntered)
        code_entry.delete(0, END)
        if (userEntered == alarmCode) and (alarmStatus == "On"):
                tkinter.messagebox.showinfo("Alarm Code","Code Accepted, Disabling alarm")
                alarmStatus = "Off"
                writeStatus(alarmTriggered, alarmStatus)
                alarmDisable(11, TRUE)
        elif (userEntered == alarmCode) and (alarmStatus == "Off"):
                tkinter.messagebox.showwarning("Alarm Code", "Unable to disable alarm. Alarm is not enabled.")
        elif len(userEntered) <4:
                tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
        else: 
                tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")



# Called when code entered is correct, flashes the green LED for a set after which point another function is called unless the alarm is disabled before time elapses
def alarmActive(root,period=0):
        global flash
        redLED(11, FALSE)
        if(period <30) and (alarmStatus is "On"):
                greenLED(15, flash)
                flash = not flash
                period +=1
                print(period)
                root.after(500, lambda: alarmActive(root, period))
        elif (alarmStatus == "Off"):
                print("Alarm disabled before activation")
                alarmDisable(11, TRUE)
        
        else:
                greenLED(15, TRUE)
                print("Alarm now active")
                alarmLive(root)
                
                
# Called when alarm is disabled, and turns red LED ON.             
def alarmDisable(pin, mode):
        print ("Alarm Disabled")
        alarmTriggered = False
        writeStatus(alarmTriggered, alarmStatus)
        greenLED(15, FALSE)
        redLED(pin, mode)

# Monitors sensors depedned on thoose selected via the UI, will trigger the alarm should movement be detected.
def alarmLive(root):
        global alarmTriggered
        frontSensor = GPIO.input(16)
        backSensor = GPIO.input(18)
        while (alarmStatus is 'On'):
                if (sensorChoice == 'Both') and (frontSensor is True) or (backSensor is True):
                        alarmTriggered = True
                        break
                elif (sensorChoice == 'Front') and (frontSensor is True):
                        alarmTriggered = True
                        break
                elif (sensorChoice == 'Back') and (backSensor is True):
                        alarmTriggered = True
                        break
                else:
                        alarmTriggered = False
                        break
        writeStatus(alarmTriggered, alarmStatus)
               
        if (alarmTriggered is True):
                motionDetected(root)
        elif (alarmStatus is 'On'):
                root.after(1000, lambda: alarmLive(root))
        
        elif (alarmStatus == "Off"):
                alarmDisable(11, TRUE)


# Called when alarm is triggered, will firstly cause a delay to occur, if the alarm has not been disabled after the delay has expired, will cause the red light to flash to indicate an intruder is present
def motionDetected(root, period=0):
        global flash
        if (alarmStatus is 'On') and (period <15):
                period +=1
                print(period)
                root.after(1000, lambda: motionDetected(root, period))
        if (alarmStatus is 'On') and (period >=15):
                redLED(11, flash)
                flash = not flash
                period +=1
                print(period, '2')
                root.after(500, lambda: motionDetected(root, period))
        elif (alarmStatus == "Off"):
                alarmDisable(11, TRUE)
                
                
                        
# writes the status of the alarm to a test file or creates one if none is not present with the specified path.       
def writeStatus(alarmTriggered, alarmStatus):
        triggered = str(alarmTriggered)
        status = str(alarmStatus)
        try:
                f = open("alarm.txt", "w")
                try:
                        f.write(status + "\n" + triggered)
                finally:
                        f.close()
        except IOError:
                pass
        
        
        
        
        
        
        
        


                
                
        
