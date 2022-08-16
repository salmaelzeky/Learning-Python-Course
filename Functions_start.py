def func1():
    print("I am a function")
    
def func2(arg1, arg2):
    print(arg1, " ", arg2)
    
def cube(x):
    return x * x * x
    
def power(num, x = 1 ):
    result = 1;
    for i in range(x):
        result = result * num
    return result
    
    
def multi_add(*args):
    result = 0
    for x in args: 
        result = result + x
    return result    
    
func1() # The function is called directly
print(func1()) # The output of the function is printed. It prints the return value of the functoin
print(func1) # Printing the value of the functoin definition itself

print(power(2))
print(power(2, 3))

# Order of the args does not matter if you are calling them by their names

print(multi_add(2, 3, 4))