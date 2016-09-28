infile=open("/storage/sdcard0/Download/studentdata.txt", "r")
for aline in infile:
    grades=aline.split()
    alist=[]
    for i in range(len(grades)-1):
        alist.append(int(grades[i+1]))
    print("%s, %s"%(grades[0],(sum(alist)/len(alist))))
infile.close()







