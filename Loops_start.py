
def main(): 
    x = 0 
    
    while (x < 5):
      print (x)
      x+=1
    
    print("--------------------")
    
    for x in range (5, 10):
        print(x)
    
    print("--------------------")
  
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    for d in days:
        print(d)
        
    for x in range (5, 10):
        if x == 7 :
            break
        if x % 2 == 0 : 
            continue
        print(x)
        
    for i,d in enumerate(days):
        print(i , d)
        
if __name__ == "__main__":
    main()