#-----------------------------------------------------------------------------
# Name:        Map Deletion(python.py)
# Purpose:     Deletes all maps created by the program.
#
# References: 	This program uses the NumPy/SciPy style of documentation as found
#				here: https://numpydoc.readthedocs.io/en/latest/format.html with
#				some minor modifications based on Python 3 function annotations
#				(the -> notation).
#
# Author:      Rishabh Tamhane
# Created:     13-Jan-2021
# Updated:     13-Jan-2021
#-----------------------------------------------------------------------------

import os

def map_delete():
    '''
    Deletes all maps created by the program.

    '''
    entries = os.listdir('source/helpers/images') #Loads file directory, saves it as a list of strings
    i = 0
    while i < len(entries):
        file = entries[i] #Loads a single string/file name
        if file.find("_map") != -1: # .find() outputs -1 if the desired string is not found
            os.remove('source/helpers/images/'+file) #Adds file name to the path of the directory and deletes it
        i = i + 1