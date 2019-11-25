# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Research Exception Handling & Pickling in Python
# ChangeLog (Who,When,What):
# Kstevens,11-20-19,Modified code to complete assignment 7
# ------------------------------------------------------------------------ #
# Research topic: Pickle Module
# Code Version: Example code 2.2
# Reference: “Python Pickling” (Tutorialspoint.com, 2019)
# <https://www.tutorialspoint.com/python-pickling> accessed November 24, 2019.
# Description: Python pickle module is used for serializing and de-serializing python
# object structures. The process to converts any kind of python objects (list, dict, etc.)
# into byte streams (0s and 1s) is called pickling or serialization or flattening or marshalling.
# We can converts the byte stream (generated through pickling) back into python objects by a
# process called as unpickling.
# Why Pickle?: In real world sceanario, the use pickling and unpickling are widespread as
# they allow us to easily transfer data from one server/system to another and then store
# it in a file or database.
# Precaution: It is advisable not to unpickle data received from an untrusted source as
# they may pose security threat. However, the pickle module has no way of knowing or raise
# alarm while pickling malicious data.
# Only after importing pickle module we can do pickling and unpickling.

import pickle
#Pickle examples:
# Below is a simple program on how to pickle a list:
# Pickle a simple list: Pickle_list1.py

import pickle
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)
#In the above code, list – “mylist” contains four elements (‘a’, ‘b’, ‘c’, ‘d’). We open
# the file in “wb” mode instead of “w” as all the operations are done using bytes
# in the current working directory. A new file named “datafile.txt” is created, which
# converts the mylist data in the byte stream.
#Unpickle a simple list: unpickle_list1.py
import pickle
pickle_off = open ("datafile.txt", "rb")
emp = pickle.load(pickle_off)
print(emp)
# Output: On running above scripts, you can see your mylist data again as output.
# ['a', 'b', 'c', 'd']
# Pickle a simple dictionary −
import pickle
EmpID = {1:"Zack",2:"53050",3:"IT",4:"38",5:"Flipkart"}
pickling_on = open("EmpID.pickle","wb")
pickle.dump(EmpID, pickling_on)
pickling_on.close()
# Unpickle a dictionary −
import pickle
pickle_off = open("EmpID.pickle", 'rb')
EmpID = pickle.load(pickle_off)
print(EmpID)
