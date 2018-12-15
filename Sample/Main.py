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
from Corporation import Corporation
from FileIO import *
from Contact import *
from bottle import *
import sqlite3
from CreatingDatabase import CreatingDatabase
from Person import Person

from UpdateDatabase import sort, update


'''
    this is a Contacts list web application built using bottle micro framework.
    dependencies: bottle - type in terminal "pip install bottle" to install it. , python 3.4
    3 routes(urls) are defined - /view - shows all open contact [beautify.tpl is used for html template]
                           /new - adds a new contact [new.tpl is used for html template]
                           /edit/(no) - edits the contact having id = no [edit.tpl is used for html template]
                           /delete/(no) - deletes the record with id = no

'''


db = Contact()
# this method view all contact list. it runs the main page or interface.
@route('/')
@route('/view')
def view_contacts():
    try:
        # the fetched results are formatted according to the template
        output = template('main', rows= db.viewData())
        return output
    except:
        return '<p>Error: The contacts cannot be shown</p>'

# this method enable the user to inter a new contact to hte list.
@route('/new')
def new_contact():
    try:
        # When save button is clicked
        if request.GET.get('save', '').strip():
            # gets called when user clicks on save button, extracting values of contact from the template
            output = db.insertData()
            return output
        else:
            return template('new.tpl')
    except:
        return '''<p>Error: The contact has not Added</p>
               <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''

# this method enable the user to update a specific contact using the id number
@route('/edit/:contact_ID')
def edit_contact(contact_ID):
    try:
        # When save button is clicked
        if request.GET.get('save', '').strip():

            output = db.editData(contact_ID)
            return output
        else:
            # Display the contact that is going to be modified
            conn = sqlite3.connect('contactDB.db')
            c = conn.cursor()
            c.execute("SELECT * FROM contacts_tbl WHERE id LIKE ?", (str(contact_ID)))
            cur_data = c.fetchone()

            return template('edit', old=cur_data, id=contact_ID)
    except:
        return '''<p>Error: The contact has not edited</p>
               <button type="button" ONCLICK="window.location.href=\'/view\'">Go back</button>'''

# this method enable the user to delete a specific contact using the id number
@route('/delete/:contact_ID')
def delete_contact(contact_ID):
    try:
        # deletes a record at id
        output = db.deleteData(contact_ID)

        return output
    except:
        return '''<p>Error: The contact has not deleted</p>
               <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''

file_io = FileIO()
# This method write all data extracted from the database into a text file
@route('/backup')
def backup_contacts():
    try:
        output = file_io.backupData()
        return output
    except:
        return '<p>Error: The data was not backed up</p>' \
               '<button type="button" ONCLICK="window.location.href=\'/view\'">Go back</button>'


# this method retrieves the data from txt file and insert them into database.
@route('/restore')
def restore_contacts():
    try:
        output = file_io.restoreData()
        return output
    except:
        return '''<p>Error: The backup was not restored</p>
               <button type="button" ONCLICK="window.location.href='/view'">Go back</button>'''

# this method enable the user to sort the contacts based on a specific field
@route('/sort/:sortValue')
def sort_contacts(sortValue):
    try:
        # the fetched results are formatted according to the template
        output = template('main', rows=sort(sortValue))
        return output
    except:
        return '<p>Error: The contacts cannot be shown</p>'

#this method update the database table to re-generate the Id number for all contact info.
@route('/update')
def update_contacts():
    try:
        # the fetched results are formatted according to the template
        output = update()
        return output
    except:
        return '<p>Error: The contacts cannot be shown</p>'


# creates database if doesn't exists
if not (os.path.exists('contactDB.db')):
    try:
        db = CreatingDatabase()
        db.createDatabase()
    except:
        print("Could not create a database.")


# demonstrates the inheritance concept
contacts = (Person("Rahim", "Saleh", "6133147728", "123", "26 Drumso St.", "Ottawa", "rahim@live.ca", "Test"),
            Corporation("Algonquin College", "613265487", "562", "1385 Woodroffe Avenue", "Ottawa", "Algon@live.ca", "Test"))
for contact in contacts:
    contact.__str__()

# run the program
run(host='localhost', port=8080, debug=True, reloader=True)



