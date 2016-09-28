import os
os.system("clear")
def num1():
    fileref=open('/storage/sdcard0/Download/names.txt','r')

    lines=fileref.read()
    print(lines)
    fileref.close()
    
num1()