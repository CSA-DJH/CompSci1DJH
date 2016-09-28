f = open("/storage/sdcard0/Download/studentdata.txt", "r")

for aline in f:
    items = aline.split()
    if len(items[2:]) > 6:
        print(items[0])

f.close()
