import os, time
os.system("clear")

outfile = open("/storage/sdcard0/Download/guestlist1.txt", "w")
num1=(0)
if num1>0:
    print("goodbye")
    quit()
else:
    while num1==0:
        print("enter q to stop adding guests")
        num2=input("what is the name of the guest? ")
        time.sleep(1)
        if num2=="q":
            num1=(1)
            break
        else:
            outfile.write(num2 + '\n')
            os.system("clear")
        

outfile.close()
