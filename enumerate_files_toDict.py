import os

logFilepath = r"\folder\folder\Logs"
searchString = "These are not the droids you are looking for"

def enumerate_files():
    my_files = {}                 
    for i, e in enumerate(os.listdir(logFilepath)):
        my_files[i] = e
    print(my_files)

