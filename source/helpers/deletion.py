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

def mapDelete(dir) -> None:
    '''
    Deletes all maps created by the program.

    Parameters
    ----------------------
    dir: string
        the path to the directory that you want to search
    '''
    entries = os.listdir(dir) #Loads file directory, saves it as a list of strings
    i = 0
    while i < len(entries):
        file = entries[i] #Loads a single string/file name
        if file.find("_map") != -1: # .find() outputs -1 if the desired string is not found
            os.remove('source/images/'+file) #Adds file name to the path of the directory and deletes it
        i = i + 1

def graphDelete(dir) -> None:
    '''
    searches for any files with '_pie' or '_bar' in a given directory
    and deletes them

    Parameters
    ----------------------
    dir: string
        the path to the directory that you want to search
    '''
    images = os.listdir(dir)
    for image in images:
        if '_pie' in image or '_bar' in image:
            os.remove(dir + image)