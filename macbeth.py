import os
os.system("clear")
def find():
    l1=[]
    l2=[]
    files=open('/storage/sdcard0/Download/macbeth.txt','r')
    search=input("what are you looking for?  ")
    for x in files:
        if search in x:     #if the search is in x, num1 is x
            num1=(x)
    files.close()
    files=open('/storage/sdcard0/Download/macbeth.txt','r')
    lines=files.readlines()
    files.close()
    indx=lines.index(num1)
    start=(indx)
    while True:   #while loop
        if not lines[start].startswith("    "):   #ends the print
            break
        start-=(1)
        l1.append(lines[start])
    l1.reverse()
    l1.remove(l1[0])
    l1.append(lines[indx])
    end=(indx)
    while True:
        if not lines[end].startswith("    "):
            break
        end+=(1)
        l2.append(lines[end])
    passage=l1 + l2
    passage=''.join(passage)
    print(passage)
find()



