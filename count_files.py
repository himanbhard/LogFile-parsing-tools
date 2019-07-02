import os
import time

logFilepath = r"/Users/folder/files"
searchString = "These are not droids you are looking for"



def count_files():
    """This will get the count of files in the directory"""
    i=0
    x=[]
    for file in os.listdir(logFilepath):
            print(file)
            x.append(file)
            i+=1
    print('the total number of files: ' +str(i))