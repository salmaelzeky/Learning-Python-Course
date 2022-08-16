
#Basic data types in python: Numbers, Strings, Booleans, Sequences, Dictionaries 

from operator import truediv


myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}



#re-declaring a variable works
myint = "abc"

#to access a member of a sequence type, use []
print(mylist[2])
print(mytuple[1])

#use slices to get parts of a sequence
print(mylist[1:5])
print(mylist[1:5:2])

#you can use slices to reverse a sequence
print(mylist[::-1]) # -1 is a step value, we did not determine the start or ending index

#dictionaries are accessed via keys
print(mydict["one"])

#ERROR: variables of different types cannot be combined

#global vs. local variable in functions
def someFunc():
    global mystr
    mystr = "def"
    print(mystr)
    
someFunc()
print(mystr)

del mystr
print(mystr)