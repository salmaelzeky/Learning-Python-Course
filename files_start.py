from importlib.resources import contents


def main():
    # Open a file for writing and create it if it doesn't exist
    # myfile = open("textfile.txt", "w+")
    
    # myfile = open("textfile.txt", "a+")

    # for i in range(10):
    #     myfile.write("This is some text \n")
        
    # myfile.close()   
     
    myfile = open("textfile.txt", "r")
    if myfile.mode == 'r':
        contents = myfile.read()
        print(contents)
        fl = myfile.readlines()
        for x in fl:
            print(x)
if __name__ == "__main__":
    main()