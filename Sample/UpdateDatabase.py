'''
    Author: Abdulrahim Alzahrani.
    Course Name: Programming Language Research Project
    Course Number: CST8333
    Lab	Sec #: 350
    Professors Name: Stanley Pieda.
    Date: April 10, 2015
    Purpose of program: Assignment 4
    References:
      1- (2011). Tutorial: Todo-List Application — Bottle 0.13-dev ,
      Retrieved March 22, 2015, from http://bottlepy.org/docs/dev/tutorial_app.html.
      2- (2014). Python/C API Reference Manual — Python 2.7.9 ,
      Retrieved March 22, 2015, from https://docs.python.org/c-api/.
      3- (2013). SQLite Python Tutorial - TutorialsPoint. Retrieved March 22, 2015,
      from http://www.tutorialspoint.com/sqlite/sqlite_python.htm.
      4- (2011). SQLite Python tutorial - ZetCode. Retrieved March 22, 2015,
      from http://zetcode.com/db/sqlitepythontutorial/.
      5- (2009). Python Files I/O - TutorialsPoint. Retrieved March 22, 2015,
      from http://www.tutorialspoint.com/python/python_files_io.htm.
      6- (2009). Python tutorial - TutorialsPoint. Retrieved March 22, 2015,
      from http://www.tutorialspoint.com/python/.

'''

import sqlite3

from Contact import Contact
import os

'''
This class sort the contact list based on the field number.
'''
def sort(sortValue):
    try:
        # instantiate Contact object
        db = Contact()
        # Create a list .
        contactList = list()
        # for loop statement to store the contact info onto the List
        for row in db.viewData():
            contactList.append(row)
        contactsTuble = tuple(contactList)
        # use sorted method with lambda function to sort the contact based on name
        return sorted(contactsTuble, key=lambda contact: contact[int(sortValue)])
    except:
        return '<p>Failed to sort the contacts list</p>' \
               '<button type="button" ONCLICK="window.location.href=\'/view\'">Go back</button>'

'''
this method update the database table to re-generate the Id number for all contact info.
'''
def update():
    try:
        # getting a cursor object to the database
        db = Contact()
        # open the text file to store the data into it. The file will be created at the first time or if it's not exit.
        contactList = list();
        # for loop statement to convert the tuple line of data into String and write them
        # into the output file

        contactList = db.viewData()
        os.remove("contactDB.db")
        # creating database file, c is the connection object used to interact with the database
        c = sqlite3.connect('contactDB.db')
        # creates a table contacts in the contactDB.db
        c.execute('''CREATE TABLE contacts_tbl (id INTEGER PRIMARY KEY, fname char(100) NOT NULL, lname char(100) NOT NULL, phone_number int(10) NOT NULL, ext int(5), address char(150), city char(100), email char(100), note char(100))''')
        for row in contactList:
            stringRow = str(row)
            txt = stringRow.strip().split(',')
            # get the fields that needed only from the line and take of all unwanted characters
            firstName = txt[1].replace("'", "")
            lastName = txt[2].replace("'", "")
            phoneNumber = txt[3].replace("'", "")
            ext = txt[4].replace("'", "")
            address = txt[5].replace("'", "")
            city = txt[6].replace("'", "")
            email = txt[7].replace("'", "")
            note = txt[8].replace("'", "").strip(')')
            # add the contact and state to the database
            c.execute('''INSERT INTO contacts_tbl (fname, lname, phone_number, ext, address, city, email, note)
                        VALUES (?,?,?,?,?,?,?,?)''',
                      (firstName, lastName, phoneNumber, ext, address, city, email, note))

            # performing database transaction and closing the connection
            c.commit()
        c.close()

        return '''<p>Contact list was updated successfully </p>
               <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''
    except:
        return '<p>Failed to update the contacts list</p>' \
               '<button type="button" ONCLICK="window.location.href=\'/view\'">Go back</button>'
