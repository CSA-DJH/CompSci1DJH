import os, time
os.system("clear")
def adding():
    x=0
    for i in range(500):
        if x>=500:
            print(str(x)+' is the total.')      
            break   
        nums=input("pick a number between 1 and 100. ")
        nums=int(nums)
        x+=nums
        print('x='+str(x))
        if nums>100:
            print("Error")
            time.sleep(1)
            os.system("clear")
            adding()
        elif nums<1:
            print("Error")
            time.sleep(1)
            os.system("clear")
            adding()
        
   
adding()
