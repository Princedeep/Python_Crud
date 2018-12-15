##########################################################################################
# File: Animal.py                                                                        #
# Author: Princedeep Singh                                                               #
# Date Last Modified: 30 March, 2018                                                     #
# Description: This animal file demnostrate concepts of inheroitance and Polymorphisim.  #
# Animal file contains three classes. Animal is main class which is inherited            #
# by other two cat and dog. Cat also inherits from dog which shows multiple inheritance. #
##########################################################################################

class Animal():

    def __init__(self, name, weight):  # Intialization constructor.
        self.name = name
        self.weight = weight

    def setName(self, name):  # Setter for name
        self.name = name

    def getName(self):  # Getter for name
        return self.name

    def setWeight(self, weight):  # Setter for weight
        self.weight = weight

    def getWeight(self):  # Getter for weight
        return self.weight

    def name(self):  # Void function to print name
        print("This is animal")

    def sound(self):  # Void function to print sounds
        print("No Sound")



class cat(Animal):

    def __int__(self):
        super.__init__() # Calling super class constructor

    def size(self):      # Funtion to print size
        print("Size is 60")

    def sound(self): # Funtion to print sound
        print("Meow!! Meow!!")


class Dog(cat, Animal):

    def __int__(self):
        super.__init__() # Calling super class constructor

    def size(self):   # Funtion to print size
        print("Size is 70")

    def name(self): # Funtion to print name
        print("This is dog")

    def sound(self): # Funtion to print sound
        print("Booh!! Wooh!!")

print("Program By Princedeep Singh: ")
object=Animal("Original Class is animal" , "Weight of animal is 100")# Calling Animal class
print(object.getName())
print(object.getWeight())
object.sound()

object=cat("\nThis is CAT", "Weight of cat is 40")  # Calling Cat class
print(object.getName())
print(object.getWeight())
object.size()
object.sound()

object=Dog("\nThis is DOG", "Weight of Dog is  4") # Calling Dog class
print(object.getName())
print(object.getWeight())
object.size()
object.sound()
