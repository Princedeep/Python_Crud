###############################################################################################
# File: Main.py                                                                                #
# Author: Princedeep Singh                                                                     #
# Description: This class has main window which contains all other small widgets like menubar  #
# and display them.
# Date Last Modified: 03-22-218                                                                            #
###############################################################################################



#Import statement to use tkinter in program
import tkinter as tk
from tkinter import *
from MenuBar import *


# Statement to create main Class of program
class Main(tk.Tk):


    def __init__(self, *args ,**kwargs):      #Creating constructor of class
        tk.Tk.__init__(self,*args,**kwargs)   #Intializing Tkinter
        objects=tk.Frame(self)                #Creating a container which will contain evrything
        objects.grid_rowconfigure(0, weight=1)
        objects.grid_columnconfigure(0, weight=1)

        self.frames= {}                       #Creating an empty dictionary
        frame=MenuBar(objects,self)           #Putting menubar into frame
        self.frames[MenuBar]= frame

        self.show_frame(MenuBar)              #Display menubar into frame

# Method to raise frame to top
    def show_frame(self, obj):
        frame = self.frames[obj] # Passing container object to frame
        frame.tkraise()   # Raise frame



root = Main() # Creating main window
root.title("Princedeep Singh") # setting title of main window
root.geometry("600x500")# Setting dimensions of main window

root.mainloop()  # Loading main loop
