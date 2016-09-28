import os, time, random
os.system("clear")

def name():
    os.system("clear")
    fileref=open("/storage/sdcard0/Download/people.txt", "r")
    x=fileref.readlines()
    for i in x:
        value=i.split(";")
        print(value[0], value[3])  
    time.sleep(4)
    fileref.close()   
    menu()

def location():
    os.system("clear")
    fileref=open("/storage/sdcard0/Download/people.txt", "r")
    x=fileref.readlines()
    for i in x:
        value=i.split(";")
        print(value[1], value[2])  
    time.sleep(4)
    fileref.close()   
    menu()
def menu():
    os.system("clear")
    menuin=input("""Which operation would you like to run?
Name(1)
Location(2)
Quit(3)
""")
    menuin=menuin.title()
    if menuin=="1":   
        name()
    elif menuin=="2":
        location()
    elif menuin=="3":
        os.system("clear")
        print("Goodbye")
        time.sleep(2)
        quit()
    else:
        print("Invalid input, please try again")
        time.sleep(2)
        menu()
menu()
