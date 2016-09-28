
import os, random
os.system("clear")
def avarage():
    random1=[]   #adds a empty list    
    num1=100        
    
    for k in range(0, 101):     
        num2=random.randrange(0,1001)      #runs a range 100 times makes a random number 100 times
        random1.append(num2)
        print(num2)
        
    random1=[int(i) for i in random1]    #ints the list
    num3=sum(random1)      #adds the list together
    num4=(num3/num1)    #gets the avarage
    num4=str(num4)  
    print("the avarage of 100 random numbers between 0 and 1000 is "+num4)   #prints the avarage number of 100 random
    
    
avarage()
    
    
    