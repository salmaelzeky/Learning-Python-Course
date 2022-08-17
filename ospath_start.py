import imp
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Print the name of the os
    print(os.name)
    # check for item existance and type
    print("Item exists:", str(path.exists("textfile.txt")))
    print("Item is a file:", str(path.isfile("textfile.txt")))
    print("Item is a file:", str(path.isdir("textfile.txt")))
    
    # Work with file paths
    print("Item's path:", str(path.realpath("textfile.txt")))
    print("Item's path and name:", path.split(str(path.realpath("textfile.txt"))))


    # Get modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the time was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been", td, "since the file was modified")
    print("Or,", td.total_seconds(),"seconds")
    

if __name__ == "__main__":
    main()