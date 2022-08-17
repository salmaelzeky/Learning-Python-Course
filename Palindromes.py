

from operator import le
from tkinter import W


def main():
    word = input("Enter string to test for palindrome or 'exit':")    
    
    i = 0 
    pal_test = False
    #j = len(word) -1
  
  
    new_word = ""
    for x in word:
        if x.isalnum():
            new_word += x
    for i in new_word:
       print("i", i)    
       if word == "exit":
           pal_test = False
           break 
    
       for j in reversed(new_word) :    
           if len(new_word) % 2 == 0 : 
               if i == j : 
                   pal_test = True
                   continue
               else:
                   pal_test = False
                   break
           else:
               i = range (len(new_word)//2)
               j = range (len(new_word)//2)
               if i == j : 
                   pal_test = True
                   continue
               else:
                   pal_test = False
                   break
                
       
            
        
    print(pal_test)



if __name__ == "__main__":
    main()