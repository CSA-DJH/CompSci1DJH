infile = open("/storage/sdcard0/Download/namecolor.txt", "r")
outfile = open("/storage/sdcard0/Download/namefavcolor.txt", "w")

aline = infile.readline()
while aline:
    items = aline.split()
    dataline = items[0] + ',' + items[3]
    outfile.write(dataline + '\n')
    aline = infile.readline()
    

infile.close()
outfile.close()
