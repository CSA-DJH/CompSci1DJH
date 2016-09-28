import os
os.system('clear')
def cat():
    newlist=['a','hello','c']
    print(newlist)
    newlist.append("apple")    #adds apple to newlist
    newlist.append(76)      #adds 76 to newlist
    print(newlist) 
    newlist[2:2]=['cat']    #adds cat
    print(newlist)
    newlist[0:0]=[99]      #adds 99
    print(newlist)
    print(newlist.index('hello'))  #tells which index hello is at
    print(newlist.count(76))    #counts how many 76s ther are
    
cat()