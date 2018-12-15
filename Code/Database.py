###############################################################################################
# File: Database.py                                                                           #
# Author: Princedeep Singh                                                                    #
# Date Last Modified: 03-24-2018                                                               #
# Description: This file contains different methods to perform different database operations  #
# There is main window which contains entry fields and buttons to perform C.R.U.D operations  #
###############################################################################################

from tkinter import *
import csv

import mysql.connector
from tkinter import messagebox
from tkinter import ttk


#
class Database:
    def __init__(self):
        # Creating varables for all fields in csv file

        refvar = StringVar()  # String variable
        geovar = StringVar()  # String variable
        commodvar = StringVar()  # String variable
        vectorvar = StringVar()  # String variable
        valuevar = StringVar()  # String variable
        coordinatevar = StringVar()  # String variable
        refdate = StringVar()  # String variable
        geo = StringVar()  # String variable
        commod = StringVar()  # String variable
        vector = StringVar()  # String variable
        value = StringVar()  # String variable
        coordinate = StringVar()  # String variable
        delete = StringVar()  # String variable
        deletevar = StringVar()  # String variable

        # Button to open database connection
        self.button = Button(text="Open Database", command=self.createConnection, relief=SOLID)
        self.button.grid(row=9, column=5)

        # Buttons to call create table method
        self.button2 = Button(text="create table", command=self.createTable, relief=SOLID)
        self.button2.grid(row=10, column=9)

        # Button to call close database connection method
        self.button3 = Button(text="Close Database", command=self.closeConnection, relief=SOLID)
        self.button3.grid(row=10, column=5)

        # Button to insert new entries into database
        self.button4 = Button(text='Insert Records', command=self.insertData, relief=SOLID)
        self.button4.grid(row=10, column=6)

        # Button to list records from database
        self.button5 = Button(text='List Records', command=self.displayData, relief=SOLID)
        self.button5.grid(row=9, column=9)

        # Button to delete records from database
        self.button6 = Button(text='Delete Record', command=lambda: self.deleteRow(), relief=SOLID)
        self.button6.grid(row=9, column=6)

        # Button to insert records from csv into database
        self.button6 = Button(text='Count of rows', command=lambda: self.countRows(), relief=SOLID)
        self.button6.grid(row=11, column=6)

        myRow = 0
        # Labels and entry for all refrence date
        self.refdateLabel = Label(text="Enter value for refdate:")
        self.refdateLabel.grid(row=myRow, column=0)
        self.refdate = Entry()
        self.refdate.grid(row=myRow, column=1)
        myRow += 1

        # Label and entry for geography
        self.geolabel = Label(text="Enter value for geo:")
        self.geolabel.grid(row=myRow, column=0)
        self.geo = Entry()
        self.geo.grid(row=myRow, column=1)
        myRow += 1

        # Label and entry for Commod
        self.commodlabel = Label(text="Enter value for commod:")
        self.commodlabel.grid(row=myRow, column=0)
        self.commod = Entry()
        self.commod.grid(row=myRow, column=1)
        myRow += 1

        # Label and entry for vector
        self.Vectorlabel = Label(text="Enter value for vector:")
        self.Vectorlabel.grid(row=myRow, column=0)
        self.vector = Entry()
        self.vector.grid(row=myRow, column=1)
        myRow += 1

        # Label and entry for coordinate
        self.coordinatelabel = Label(text="Enter value for coordinate:")
        self.coordinatelabel.grid(row=myRow, column=0)
        self.coordinate = Entry()
        self.coordinate.grid(row=myRow, column=1)
        myRow += 1

        # Label and entry for value
        self.valueLabel = Label(text="Enter value for value:")
        self.valueLabel.grid(row=myRow, column=0)
        self.value = Entry()
        self.value.grid(row=myRow, column=1)
        myRow += 1

        # Label and entry for delete
        self.deleteLabel = Label(text="Enter value for delete or delete:")
        self.deleteLabel.grid(row=myRow, column=0)
        self.delete = Entry()
        self.delete.grid(row=myRow, column=1)

        myRow += 1

    # Method to create database connection
    def createConnection(self):
        # Trying to connect to database with provided credentials
        try:
            self.con = mysql.connector.connect(host='localhost', db='postgres', user='root', password='root')
            self.cur = self.con.cursor()

            b = messagebox.showinfo("Princedeep Singh", "Successfully created Connection")


        except (mysql.connector.errors.OperationalError, AttributeError):  # Except statement to catch listed exceptions
            a = messagebox.showerror("Princedeep Singh", "Please open database conection")

    # Method to create new table
    def createTable(self):

        try:
            self.cur = self.con.cursor()
            self.cur.execute('''CREATE TABLE record(
                                      id int(11) NOT NULL,
                                      refdate varchar(100) DEFAULT NULL,
                                      geo varchar(110) NOT NULL,
                                      commod varchar(110) NOT NULL,
                                      vector varchar(110) NOT NULL,
                                      coordinate varchar(110) NOT NULL,
                                      val varchar(110) NOT NULL
                                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;''')  # query to create a sample table with 3 fields
            self.cur.execute('ALTER TABLE record ADD PRIMARY KEY (id)');

            self.cur.execute('ALTER TABLE record MODIFY id int(11) NOT NULL AUTO_INCREMENT')
            b = messagebox.showinfo("Princedeep Singh", "Successfully created table")

        except (mysql.connector.errors.OperationalError, AttributeError):  # Except statement to catch listed exceptions
            a = messagebox.showerror("Princedeep Singh", "Please open database conection")

        except mysql.connector.errors.ProgrammingError: # Except statement to catch listed exceptions
          w = messagebox.showerror("Princedeep Singh", "Table already exists ")

    # Method to delete a particular row using primary key

    def deleteRow(self):

        try:
            self.cur = self.con.cursor(buffered=True)
            self.cur = self.con.cursor()
            deletevar = self.delete.get()
            # Query to delete given values in database
            self.cur.execute(
                "DELETE FROM record WHERE id=%s",
                (deletevar,))  # Query to delete a row selected by id value entered in field
            if self.cur.rowcount == 0:
                a = messagebox.showerror("Princedeep Singh", "Id Not Found")
            else:
                a = messagebox.showinfo("Princedeep Singh", "Record deleted ")
            # end of new code`
            self.con.commit()
        except (mysql.connector.errors.OperationalError, AttributeError):  # Except statement to catch listed exceptions
            a = messagebox.showerror("Princedeep Singh", "Please open database conection")

    # Method to close database connection
    def closeConnection(self):

        # Trying to close created connection
        try:
            self.con.close()
            a = messagebox.showinfo("Princedeep Singh", "Closing Connection")

        except (mysql.connector.errors.OperationalError, AttributeError):  # Except statement to catch listed exceptions
            a = messagebox.showerror("Princedeep Singh", "Connection already closed")

    # Method to insert new entries into database
    def insertData(self):

        try:
            # Variables to get value of entered text in fields
            refdatevar = self.refdate.get()
            geovar = self.geo.get()
            commodvar = self.commod.get()
            vectorvar = self.vector.get()
            coordinatevar = self.coordinate.get()
            valuevar = self.value.get()

            self.cur = self.con.cursor()
            self.cur.execute \
                ("insert into  \
                         record (refdate,geo,commod,vector,coordinate,val)  \
                         values (%s, %s, %s,%s, %s, %s)", \
                 (refdatevar, geovar, commodvar, vectorvar, coordinatevar,
                  valuevar))  # Command to send entered data to database
            self.cur.fetchone()
            # end of new code
            self.con.commit()
            b = messagebox.showinfo("Princedeep Singh",
                                    "affected rows = {}".format(self.cur.rowcount))  # Returns value of effected rows
        except (mysql.connector.errors.OperationalError, AttributeError):  # Except statement to catch listed exceptions
            a = messagebox.showerror("Princedeep Singh", "Please open database conection")
        except (mysql.connector.errors.InternalError):
            a = messagebox.showerror("Princedeep Singh", "Please open database conection again")


        # Method to display data from database

    def displayData(self):

        # Try block for selecting records
        try:
            self.cur.execute('SELECT * FROM record')
            # b=self.cur.fetchall()
            a = messagebox.showinfo("Princedeep Singh", "Record are{}".format(self.cur.fetchone()))

        except (mysql.connector.errors.OperationalError, AttributeError):  # Except statement to catch listed exceptions
            a = messagebox.showerror("Princedeep Singh", "Please open database conection")
        except (mysql.connector.errors.InternalError):
            a = messagebox.showerror("Princedeep Singh", "Please open database conection again")

    def countRows(self):
        try:
            rows = "SELECT Count(*) FROM record"  # Checking rows in database
            cur = self.con.cursor()
            self.cur = self.con.cursor(buffered=True)
            self.cur.execute(rows)
            n = self.cur.fetchone()[0]
            a = messagebox.showinfo("Princedeep Singh", "Total records are: {}".format(n))
            return n  # returns number of rows present in database
        except(mysql.connector.errors.InternalError, AttributeError, mysql.connector.errors.OperationalError):
            a = messagebox.showerror("Princedeep Singh", "Please open database conection Again")
        except (mysql.connector.errors.InternalError):
            a = messagebox.showerror("Princedeep Singh", "Please open database conection again")

    # Method to insert csv file into database
    def insertCsv(self):
        csv_data = csv.reader(open('a.csv'))
        for row in csv_data:
            self.cur.execute(
                "INSERT INTO record(refdate,geo,commod,vector,coordinate,val) VALUES(%s, %s, %s, %s, %s, %s)",
                row)

        # close the connection to the database.

        self.con.commit()
        print("Done")


# Method for testing number of rows in database

def row():
    con = mysql.connector.connect(host='localhost', db='postgres', user='root', password='root')
    cur = con.cursor()
    rows = "SELECT Count(*) FROM record"  # Checking rows in database
    cur.execute(rows)
    n = cur.fetchone()[0]
    return n  # returns number of rows present in database


def displayData():

        # Try block for selecting records

            con = mysql.connector.connect(host='localhost', db='postgres', user='root', password='root')
            cur = con.cursor()
            cur.execute('SELECT * FROM record')
            # b=self.cur.fetchall()
            results = cur.fetchone()
            # Check if anything at all is returned
            if results:
                return True
            else:
                return False

