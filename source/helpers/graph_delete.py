#-------------------------------------------------
# Name:       graph_delete.py
# Purpose:    To delete the images of the graphs
#             upon termination of the program
#
# Author:     Alfred Mikhael
# Date:       11-01-2021
#-------------------------------------------------
import os

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
