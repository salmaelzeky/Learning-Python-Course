try:
    x = 10 / 0
except:
    print("well that did not work!")
    
    
try:
    answer = input("what should I divide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You cannot divide by 0")
except ValueError as e: 
    print("You did not give me a valid num!")
    print(e)
finally: 
    print("This code works well")
    