#daniel HErbowy
import os
os.system("clear")

print("---------------------------------------------")
def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new = []                    #empty list
    for value in a_list:       #for loop
        new_elem = value * value * value    #multiplies the list
        new.append(new_elem)    #appends the new list to the emtpy list
    return new

things = [1, 2, 3, 4, 5]        #list to change
print(things)
things = doubleStuff(things)     #makes the doubled list
print(things)

print("---------------------------------------------")
def num1():
    y=[1,3,5,[7,9],11]
    print(y[3][1])     #prints 9
    
num1()
print("---------------------------------------------")

def num2():
    z="My name is Billy Bob"
    x=z.split()   #splits the name into a list
    print(x)
    
num2()

print("---------------------------------------------")
def num3():
    a=['John', 'Jane', 'Jimmy', 'Jenny']
    num4=(";")
    print(num4.join(a)) #puts a semi collin between the names
    
num3()

print("---------------------------------------------")
