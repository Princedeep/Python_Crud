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

from bottle import*

# This Class performs basic functions of the program which are view, add, edit, and delete a contact.
class Contact():


    # this the class Contact constructor
    def __init__(self, phoneNumber="", ext="", address="", city="", email="", note=""):
        super().__init__()

        self.phoneNumber = phoneNumber
        self.ext = ext
        self.address = address
        self.city = city
        self.email = email
        self.note = note



    # this method view all contact list and return all info in the database.
    def viewData(self):
        conn = sqlite3.connect('contactDB.db')
        c = conn.cursor()
        # fetch all the  records from the table
        c.execute("SELECT * FROM contacts_tbl")
        # results is a list of tuple containing data from contacts_tbl table
        results = c.fetchall()
        conn.close()
        return results

    # this method enable the user to inter a new contact to hte list.
    def insertData(self):
        conn = sqlite3.connect('contactDB.db')
        c = conn.cursor()
        firstName = request.GET.get('fName', '').strip()
        lastName = request.GET.get('lName', '').strip()
        phoneNumber = request.GET.get('phoneNumber', '').strip()
        ext = request.GET.get('ext', '').strip()
        address = request.GET.get('address', '').strip()
        city = request.GET.get('city', '').strip()
        email = request.GET.get('email', '').strip()
        note = request.GET.get('note', '').strip()
        # storing new value in the database
        c.execute('''INSERT INTO contacts_tbl (fname, lname, phone_number, ext, address, city, email, note)
                                VALUES (?,?,?,?,?,?,?,?)''',
                  (firstName, lastName, phoneNumber, ext, address, city, email, note))
        # performing database transaction and closing the connection
        conn.commit()
        conn.close()
        return '''<p>The new contact was inserted into the database</p>
                       <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''

    # this method enable the user to update a specific contact using the id number
    def editData(self, idNo):
        conn = sqlite3.connect('contactDB.db')
        c = conn.cursor()
        firstName = request.GET.get('fName', '').strip()
        lastName = request.GET.get('lName', '').strip()
        phoneNumber = request.GET.get('phoneNumber', '').strip()
        ext = request.GET.get('ext', '').strip()
        address = request.GET.get('address', '').strip()
        city = request.GET.get('city', '').strip()
        email = request.GET.get('email', '').strip()
        note = request.GET.get('note', '').strip()
        id_No = int(idNo)
        # storing new value in the database
        c.execute("UPDATE contacts_tbl SET fname=?, lname=?, phone_number=?, ext=?, address=?, city=?, email=?, note=? WHERE id LIKE ?",(firstName, lastName, phoneNumber, ext, address, city, email, note, id_No))
        # performing database transaction and closing the connection
        conn.commit()
        conn.close()
        return '''<p>The item was successfully updated</p>
                       <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''

# this method enable the user to delete a specific contact using the id number
    def deleteData(self, idNo):
        conn = sqlite3.connect('contactDB.db')
        c = conn.cursor()
        c.execute("DELETE FROM contacts_tbl  WHERE id LIKE ?", (idNo))
        conn.commit()
        conn.close()
        return ''' The record was deleted successfully</p>'
                        <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''

    # to string method
    def __str__(self, *args, **kwargs):
        return print("This is Contact class (Parent)")


