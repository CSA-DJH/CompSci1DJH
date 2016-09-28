import os,time
os.system("clear")
lives=3
def check2(entry1,entry2,file1,file2):
    ref1=open(file1,"r")   #opens the file
    list1=ref1.readlines()   #reads the lines
    list1=[item.strip() for item in list1]   #strips the lines
    ref2=open(file2,"r")
    list2=ref2.readlines()
    list2=[item.strip() for item in list2]
    if entry1 in list1:
        if entry2 in list2:                     #checks if the username and password is in the list
            if list1.index(entry1)==list2.index(entry2):   #checks if password matches with the username
                return True
    else:
        return(False)
while lives>0:
    username=input("Please enter your username: ").upper()
    password=input("Please enter your password: ")
    if check2(username,password,"/storage/sdcard0/Download/usernames.txt","/storage/sdcard0/Download/passwords.txt")==True: #checks username and pswd
        print("Logged in!\nWelcome %s!"%username)
        time.sleep(1)
        quit()
    else:
        print("Incorrect login information! Please try again!")
        time.sleep(1)
        lives-=1
print("You have entered incorrect login information too many times!")
