#Daniel Herbowy
import os
os.system("clear")
fileref=open("/storage/sdcard0/Download/nameage.txt", "r")
for aline in fileref:
    values = aline.split()
    print(values[0], 'is', values[2], "years old." )

fileref.close()
