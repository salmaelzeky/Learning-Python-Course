
from unittest import result


def main(): 
    x, y = 10, 100
    
    if x < y : 
        result = "x < y"
    elif x > y:
        result = "x > y"
    else: 
        result = "x = y"    
    print(result)
    
    result = "x < y" if x < y else "x > y"
    print(result)
    
    value = "one"
   
    match value:
        case "one" : 
            result = 1 
        case "two" : 
            result = 2
            
if __name__ == "__main__":
    main()