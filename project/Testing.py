###############################################################################################
# File: Testing.py                                                                             #
# Author: PRINCEDEEP SINGH                                                                     #
# Description: This class creates a testcase to test method of database class                  #
# Date Last Modified: 03-24-2018                                                                #
###############################################################################################
import Database
import unittest

print("AUTHOR: PRINCEDEEP SINGH\n")

# Class to perform unit testing
class Test_Methods(unittest.TestCase):

    def test_row(self):  # Method to test number of rows present in database

        result = Database.row()
        self.assertNotEqual(result, 2)  # checking expected value with output

    def test_db_connection(self):

        result = Database.displayData()
        self.assertEqual(result, True)  # checking expected value with output


# Running main loop
if __name__ == '__main__':
    unittest.main()
