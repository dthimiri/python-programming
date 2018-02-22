import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():

    # Open a file for writing and create it if does not exist
    with open("textfile.txt", 'w+') as f:
        for i in range(10):
            f.write("This is line no: %d\r\n" %(i+1))

    with open("textfile.txt", 'r') as f:
        contents = f.read()
        #print(contents)

    # print the name of the os
    print("OS name: ", os.name)

    # check for the existence and type
    print("Item exists: ", path.exists("textfile.txt"))
    print("Item is a file: ", path.isfile("textfile.txt"))
    print("Item is a directory: ", path.isdir("textfile.txt"))

    # work with file paths
    print("File full path: ", path.realpath("textfile.txt"))
    print("File's path and name: ", path.split(path.realpath("textfile.txt")))

    # get the modification time of the file
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # calculate the time diff between last modification
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been " + str(td) + " since the file has been modified")
    print("Or, " + str(td.total_seconds()) + " seconds")



if __name__ == '__main__':
    main()