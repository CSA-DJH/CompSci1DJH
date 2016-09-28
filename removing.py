import os
os.system('clear')
def removing(): 
    num7=[76,'92.3','hello',True,4,76]   #defines all chracters
    print(num7)
    for i in range(1,7):     #range that runs 7 times
        del num7[-1]     #deletes the last character
        print(num7)      #prints
    
    
removing()