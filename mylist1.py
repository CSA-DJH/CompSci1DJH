#daniel Herbowy
import os
os.system("clear")

def mylist():        #makes a function
    num1=[76]          
    num2=['92.3']
    num3=["hello"]         #defines all variables to add
    num4=[True]
    num5=[4]
    num6=[76]
    mylist=[]            #makes an empty list
    num7=mylist+num1  #adds the first variable
    print(num7)  
    num8=num7+num2     #adds second
    print(num8)
    num9=num8+num3    #adds third
    print(num9)
    num10=num9+num4     #adds fourth
    print(num10)
    num11=num10+num5    #adds fifth
    print(num11)
    num12=num11+num6     #adds sixth
    print(num12)
    
mylist()