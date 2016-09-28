import os
os.system("clear")
start = input('when do you leave?')
stay = input('how long do you stay?')
start = int(start)
stay = int(stay)
num1 = start + stay
num2 = num1%7
num2=str(num2)
print("you will return on the "+num2)
