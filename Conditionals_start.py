
from unittest import result


def main(): 
    x, y = 10, 100
    
    if x < y : 
        result = "x < y"
    elif x > y:
        result = "x > y"
    else: 
        result = "x = y"    
    
    result = "x < y" if x < y else "x > y"

    value = "42"
    match value:
        case "one" : 
            result = 1 
        case "two" : 
            result = 2
        case _:
            result = -1
    print(result)
            
if __name__ == "__main__":
    main()