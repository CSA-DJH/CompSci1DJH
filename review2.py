import os
os.system("clear")
def num2():
    temp1=(input('what is the temp in ferenhiet?'))
    temp1=int(temp1)
    temp2=(((temp1 - 32) * 5) / 9)
    temp2=str(temp2)
    print ('the temp in celceus is '+temp2)

num2()
