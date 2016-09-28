import os, time
os.system("clear")
mylist=[]
for x in range(2):
    input1=input("Enter a word. ")
    mylist.append(input1)
    print(mylist)
    time.sleep(1)
for y in range(2):
    input2=input("Enter a word. ")
    mylist=mylist+[input2]
    print(mylist)
    time.sleep(1)
