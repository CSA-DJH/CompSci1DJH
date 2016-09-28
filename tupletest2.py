import os    
os.system("clear")
x=[]
print("PART B")
print("-----------------------------------------------------------------------------")
def startString(char, stringlist):
    newlist = []
    newlist1=[]
    for string in stringlist:
        if string.startswith(char):    #if the string starts with x, appends it to newlist
            newlist.append(string)
        else:
            newlist1.append(string)    #if it doesnt start with x, appends it to newlist1
    newlist.sort()
    newlist1.sort()   #sorts the lists
    print(newlist)
    print(newlist1)

    newlist.append(newlist1)   #adds the two lists together
    print(newlist)
startString('x', ['mix', 'xyz', 'apple', 'xanadu', 'aardvark', 'maf'])

print("-----------------------------------------------------------------------------")
print("PART D")
print("-----------------------------------------------------------------------------")


def numbers(list1):
    list2=[]    
    for i in list1:        
        if not i in list2:  #if the number isnt in lits two appends and keeps going  
            list2.append(i)    #appends the number not in the list
    print(list2)
numbers([0,0,1,1,1,2,2,3,3,3,5,5])