# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Research Exception Handling & Pickling in Python
# ChangeLog (Who,When,What):
# Kstevens,11-20-19,Modified code to complete assignment 7
# ------------------------------------------------------------------------ #
# Research topic: Pickle Module
# Code Version: Example code 2.1
# Reference: 11.3. copy_reg — Register pickle support functions
# https://docs.python.org/2/library/copy_reg.html
# Description: The copy_reg module defines functions which are used by pickling specific
# objects while pickling or copying. This module provides configuration
# information about object constructors(may be factory functions or class
# instances) which are not classes.

import copyreg, copy, pickle
class C(object):
     def __init__(self, a):
         self.a = a

def pickle_c(c):
     print("pickling a C instance...")
     return C, (c.a,)

copyreg.pickle(C, pickle_c)
c = C(1)
d = copy.copy(c)
#pickling a C instance...
p = pickle.dumps(c)
#pickling a C instance...