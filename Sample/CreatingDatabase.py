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

class CreatingDatabase():


    '''
	builds a sqlite3 database for "contacts List" in the same directory.
	Run it only one time.
	schema of table: contactDB(id, fname, lname, phone_number, ext, address, city, email, note)
	'''

    def __init__(self):
        super().__init__()

    # this method creates a database and inserts some data to it
    def createDatabase(self):
        try:
            # creating database file, c is the connection object used to interact with the database
            c = sqlite3.connect('contactDB.db')
            # creates a table contacts in the contactDB.db
            c.execute('''CREATE TABLE contacts_tbl (id INTEGER PRIMARY KEY, fname char(100) NOT NULL, lname char(100)
                        NOT NULL, phone_number int(10) NOT NULL, ext int(5), address char(150), city char(100),
                        email char(100), note char(100))''')
            # inserting some default values into the table using sql statements
            c.execute('''INSERT INTO contacts_tbl(fname, lname, phone_number, ext, address, city, email, note)
                        VALUES ('Rahim', 'Saleh', 6133147728, 120, '26 Drumso st', 'Ottawa', 'rahim@live.ca' ,
                        'This is a test')''')
            c.execute('''INSERT INTO contacts_tbl(fname, lname, phone_number, ext, address, city, email, note)
                        VALUES ('Rahim1', 'Saleh1', 6133147728, 120, '26 Drumso st', 'Ottawa', 'rahim@live.ca' ,
                         'This is a test1')''')
            c.execute('''INSERT INTO contacts_tbl(fname, lname, phone_number, ext, address, city, email, note)
                        VALUES ('Rahim2', 'Saleh2', 6133147728, 120, '26 Drumso st', 'Ottawa', 'rahim@live.ca' ,
                        'This is a test2')''')
            # commit all the changes and execute the above statements
            c.commit()
            c.close()
        except:
            print("The database is not created properly")