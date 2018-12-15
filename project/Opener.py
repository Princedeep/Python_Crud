###############################################################################################
# File: Opener.py                                                                             #
# Author: Princedeep Singh                                                                    #
# Date Last Modified: 03-18-2018                                                               #
# Description: This class contains a file opener which is called in another class.            #
# It reads  a csv file using csv reader and display file content in listbox.                  #
# It also inserts new data in specified file and update changes.                              #
###############################################################################################



from tkinter import*
import csv
import os
import codecs

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
# Creating a new class opener
class Opener():

   # Method to read file and view content of csv file in scrollable listbox
   def ReadAndView():
    try:
      with codecs.open(askopenfilename(title="Princedeep Singh", filetypes=[("CSV files", "*.csv")]), encoding='utf-8') as f:

    # Creating Open file dialog to choose file

       csv_reader = csv.reader(f,delimiter='\t') # Csv dictionary  reader for reading contents of file
       #reader = sorted(csv_reader, key=operator.itemgetter(1))
       root = Tk() # Creating new root window
       root.title('Princedeep Singh') # Setting title of window
       root.geometry("900x500") # Setting geometry of root window
       list = Listbox(root, width=400,height=500)#yscrollcommand=scrollbar.set) # Creating new listbox and inserting it in root window

     # Loop to read content of file line by line
       for line in csv_reader:
          list.insert(END , str(line))

          list.grid(row =0, column=0)

       #scrollbar.config(command=list.yview) # Configuring scrollbar to view along yaxis

       root.mainloop() # Loading main window

    except:FileNotFoundError , TclError
    print ("file closed")



   def CreateNew():
       os.system("notepad.exe ")














