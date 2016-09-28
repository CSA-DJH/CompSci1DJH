import os
os.system("clear")
x=['Marky', 'Ricky', 'Danny', 'Terry', 'Mikey', 'Davey', 'Timmy', 'Tommy', 'Joey', 'Robby', 'Sam', 'Brian']
y=0
for i in x:  #for loop that runs as many times as the list
    y=y+1
    if i=='Sam':   #if sam, prints the total number of names.
        print(y)