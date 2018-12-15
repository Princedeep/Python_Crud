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

from Contact import Contact

class Corporation(Contact):

    global corporationName

    # this the class Corporation constructor over write the contact constructor
    def __init__(self, corporationName, phoneNumber, ext, address, city, email, note):
        super().__init__(phoneNumber, ext, address, city, email, note)
        self.corporationName = corporationName


    # def __str__(self):
    #     print('''This is a Corporation contact:
    #           Corporation Name: {0}
    #           PhoneNumber: {1}
    #           Ext.: {2}
    #           Address: {3}
    #           City: {4}
    #           Email: {5}
    #           Note: {6}'''.format(self.corporationName, self.phoneNumber, self.ext, self.address, self.city, self.email, self.note))

