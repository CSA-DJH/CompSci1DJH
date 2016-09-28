#Daniel Herbowy
import string, time, os
workersin=['']   #makes a blank list
workersout=['']   #makes a second blank list
global workersin
global workersout     #globalizes the empty lists
def menu():
    os.system('clear')
    print('--------------------')
    print('''Press 1 to clock in 
press 2 to clock out
press 3 to see the clocked in workers                
press 4 to see the clocked out workers
press 5 to check if a worker is clocked in or out
press 6 quit

--------------------''')      #ask what you want to do
    num1=input('Entry: ')
    if num1=='1':
        entry()         #if 1 runs entry
    elif num1=='2':
        entry1()        #if 2 runs entry1
    elif num1=='3':
        print(workersin)       #if 3 prints the clocked in workers
        time.sleep(5)
        menu()                        
    elif num1=='4':
        print(workersout)        #if four prints the clocked out workers
        time.sleep(5)
        menu()
    elif num1=='5':
        checking()          #if five runs checking
        time.sleep(5)
    elif num1=='6':    #if 6 quits
        quit()
    else:
        print("not a valid command")   #if anything else runs the menu again
        time.sleep(3)
        menu() 

def entry():
    os.system('clear')
    global workersin 
    name1=input('what is the workers name? ') #asks for a name
    name1=name1.title()    #titles the name
    workersin.append(name1)    #adds the name to the empty list
    workersin.append(", ")     
    print(''.join(workersin))   #joins names together
    workersin.append("; ")   #adds a ;
    menu() 
    
def entry1():
    os.system('clear')
    global workersout 
    name2=input('what is the workers name? ')   #ask for a name 
    name2=name2.title()    #titles the name
    workersout.append(name2)    #adds it to an empty list
    workersout.append(", ")     #adds ,
    print(''.join(workersout))   #joins names together
    workersout.append("; ")   #adds ;
    menu() 
    
def checking():
    num2=input("who would you like to check?") #asks for a name to check
    num2=num2.title()   #titles it
    num3=workersin.count(num2)   #checks if the name is in the list
    num3=int(num3)
    if num3>0:
        print("That person is clocked in")     #if it finds the name prints he is clocked in
        time.sleep(5)
        menu()
    elif num3<=0:
        print("that person is clocked out")    #if there is no name prints that he is clocked out
        time.sleep(5)
        menu()
    
    

menu() 