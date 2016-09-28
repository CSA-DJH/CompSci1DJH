#daniel herbowy
#switching between adding and subing
import os
os.system("clear")
fileref=open('/storage/sdcard0/Download/numbers.txt','r')
x=(0)
    
for aline in fileref:
    val=aline.split()
    if x==6:
        quit()
    
    if x %2 == 0:
        num2=int(val[0]) 
        num3=int(val[1])  
        x=(x+1)
        print(num2+num3)
    else:      
        num4=int(val[0]) 
        num5=int(val[1])
        x=(x+1)
        print(num4-num5)
       
    


    
