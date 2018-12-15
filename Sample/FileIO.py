'''
    Author: Abdulrahim Alzahrani.
    Course Name: Programming Language Research Project
    Course Number: CST8333
    Lab	Sec #: 350
    Professors Name: Stanley Pieda.
    Date: Mar 22, 2015
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
from Contact import *

import sqlite3
# this class write and read all data stored in the database to a txt file using a Python's built-in open()
# function.
class FileIO():
    # This method write all data extracted from the database into a text file
    db = Contact()
    def backupData(self):
        try:
            # makes a connection to the database
            conn = sqlite3.connect('contactDB.db')
            # getting a cursor object to the database
            c = conn.cursor()
            # fetch all the  records from the table
            c.execute("SELECT * FROM contacts_tbl")
            # results is a list of tuple containing data from contacts_tbl table
            results = c.fetchall()
            conn.close()
            # open the text file to store the data into it. The file will be created at the first time
            # or if it's not exit.
            outfile = open('backup.txt', 'wt')
            type(outfile)
            # for loop statement to convert the tuple line of data into String and write them
            # into the output file
            for row in results:
                stringLine = str(row)
                outfile.write(stringLine + "\n")
            outfile.close()
            return '''<p>Backup was created successfully. Look at "backup.txt" file in the project folder </p>
                       <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''
        except:
            return '<p>Error: The data was not backed up</p>' \
                   '<button type="button" ONCLICK="window.location.href=\'/view\'">Go back</button>'


    # this method retrieves the data from txt file and insert them into database.

    def restoreData(self):
        try:
            # open the text file and retrieve the data
            infile = open('backup.txt', 'rt')
            # getting a cursor object to the database
            conn = sqlite3.connect('contactDB.db')
            c = conn.cursor()
            # loop through the list and separate the data into lines
            for line in infile:
                txt = line.strip().split(',')
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
                conn.commit()
            conn.close()
            return '''<p>The backup data was restored and inserted into the database</p>
                       <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''

        except:
            return '''<p>Error: The backup was not restored</p>
                       <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''