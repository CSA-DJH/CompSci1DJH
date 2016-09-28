#daniel Herbowy
import os, time
os.system("clear")

def menu():
    print("Hello!, What would you like to do?")
    print('''
    -----------------------------------------------------------------
    Press 1 for a greeting
    press 2 for a addition or substraction calculator
    press 3 to make a list of people attending an event
    press 4 to quit
    -----------------------------------------------------------------
    ''')
    num88=input("")  #asks what to do
    if num88=='1':  #if 1 runs name
        name()
    elif num88=='2':  #if 2 runs math1
        math1()
    elif num88=='3':  #if 3 runs party
        party()
    elif num88=='4':  #if 4 quits
        quit1()
    else:
        print("that is not an option")   #if something else is entered restarts the menu
        time.sleep(2)
        os.system("clear")
        menu()

def name():
    num1=input("what is your name?")
    num1=num1.title()
    print("hello "+ num1)    #asks for a name and prints a greeting
    time.sleep(2)
    os.system("clear")
    menu()
    
def math1():
    num2=input("if you would like to add two numbers, press 1, If you would like to substract two numbers, press 2")
    if num2=='1':
        num3=input("what is the first number?")   #if 1 asks for the two numbers to add
        num3=int(num3)
        num4=input("what is the second number?")
        num4=int(num4)
        num5=(num3+num4)
        num5=str(num5)
        print("those two numbers add up to "+num5)
        time.sleep(2)
        os.system("clear")
        menu()
    else:
        if num2=='2':
            num6=input("what is the first number?")
            num6=int(num6)
            num7=input("what is the second number?")       #if 2, asks for two numbers to sub
            num7=int(num7)
            num8=(num6-num7)
            num8=str(num8)
            print("substracting those two numbers equal "+num8)
            time.sleep(2)
            os.system("clear")
            menu() 
        else:
            print("that is not a option")  #if anything else is entered restarts math1
            time.sleep(1)
            os.system("clear")
            math1()
            
def party():
    num0=[]
    num1=input("how many people are attending (please enter a number)")  #asks how many people are attending
    num1=int(num1)
    for i in range(num1):          #asks for a persons name as many times as what was entered
        num2=input("what is the person's name")      
        num2=num2.title()
        num0.append(num2)   #titles the name and appends it to an empty list
    num0.sort()   #sorts the names
    glue=", "
    num0=glue.join(num0)   #gets rid of the [ and "
    print(num0 + " are attending the event.")  #prints haw namy people there are 
    time.sleep(3)
    os.system("clear")
    menu()
    
def quit1():
    os.system("clear")
    print("Goodbye")   #a function that quits
    quit()
    

menu()