###############################################################################################
# File: ProducerConsumer.py                                                                   #
# Author: Princedeep Singh                                                                    #
# Date Last Modified: 03-22-2018                                                               #
# Description: Class to show multithreading where one thread is reading from csv and puttting #
# it into list then consumer is taking data from list and inserting it into database          #
#                                                                                             #
###############################################################################################
from threading import Lock


import threading
import mysql.connector
import csv







l= Lock() # Creating a lock object
list_A=[] # creating a list




# Creating producer class to read data from csv file
class producer(threading.Thread):

       def run():

           l.acquire() # puts lock on thread
           global list_A # using global variable
           global cur # using global variable
           conn = mysql.connector.connect(host='localhost', db='postgres', user='root', # Creating connection to database
                                           password='root')  # Creates connection to database
           cur = conn.cursor()
           csv_data = csv.reader(open('a.csv')) # Reading records from csv file
           list_A = list(csv_data)
           l.release() # releases lock on thread

           print("Producer and Consumer are   running")



# Creating consumer class to insert data into datbase
class Consumer(threading.Thread):

       def run():
             l.acquire() #puts lock on thread
             global list_A # using global variable
             global cur # using global variable
             conn = mysql.connector.connect(host='localhost', db='postgres', user='root',
                                          password='root')  # Creates connection to database
             cur = conn.cursor()
             for row in list_A:
                 cur.execute(
                     "INSERT INTO record(refdate,geo,commod,vector,coordinate,val) VALUES(%s, %s, %s, %s, %s, %s)",
                     row) # Query to insert data from csv file into database
                 # close the connection to the database.
             conn.commit()

             print("Producer and Consumer finished")










