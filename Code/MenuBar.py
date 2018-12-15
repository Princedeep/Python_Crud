###############################################################################################
#File: MenuBar.py                                                                             #
#Author: Princedeep Singh                                                                     #
#Description: This class creates a menubar with sub menus                                     #
#Date Last Modified: 03-18-218                                                                #
###############################################################################################
import threading
from Opener import *
from tkinter import *
from Database import *
from ProducerConsumer import *



import tkinter as tk


from tkinter.filedialog import askopenfilename

class MenuBar(tk.Frame,Database,Opener):

    # Creating constructor of class
    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)

        menubar=Menu()#Intializing menubar
        filemenu = Menu(menubar)# Creating file menu
        Db = Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu) #Adding sub label to be diaplyed for file menu
        menubar.add_cascade(label="Database", menu=Db)  # Adding sub label to be diaplyed for Database menu

        Db.add_command( label = "open",command=lambda:Database()) # Adding database class

        filemenu.add_command(label="New" , command=MenuBar.CreateNew )#Creating sub menu new under file menu
        filemenu.add_command(label="Open" ,command=MenuBar.ReadAndView)#Creating open submenu uner file menu and calling file opener of class opener
        filemenu.add_command(label="Mutithreading", command=lambda:StartThreads())# Creating sub menu save under file menu

        helpmenu = Menu(menubar, tearoff=0)#Creating help menu
        menubar.add_cascade(label="Help", menu=helpmenu)#Adding label to be diaplyed for help menu
        helpmenu.add_command(label="about" )# Creating sub menu about under file menu
        controller.config(menu=menubar)#Configuring menubar



       # menubar.pack(pady=50)


def StartThreads():
    pt = threading.Thread(target=producer.run, args=()) # Calling run method of producer class
    ct = threading.Thread(target=Consumer.run, args=())  # Calling run method of Consumer class
    pt.start() # Starting producer thread
    ct.start() # Starting consumer thread



