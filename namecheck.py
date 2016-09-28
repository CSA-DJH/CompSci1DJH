#daniel Herbowy
#checking names
import os
os.system("clear")
infile=open("/storage/sdcard0/Download/namelength.txt", "r")
afile=infile.readlines()
for i in range(6):  #for loop that runs 6 times
    x=afile[i].split()  #splits the list
    num1=(int(len(x[0])))  #gets the length of the name
    num2=(int(afile[i+6]))   #gets the number to compare too
    if num1==num2:  #compares the lenghts
        print("The length is correct!")
    else:
        print("The length is not correct!")
infile.close()
