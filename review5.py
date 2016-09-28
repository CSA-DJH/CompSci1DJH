

import os
os.system('clear')
def main():
    length5list=[]
    list2=[]
    print("please enter ten words")
    for b in range(10):
        num1=input("please enter a word: ")
        if len(num1)==5:
            length5list.append(num1)
        else:
            list2.append(num1)
          
    if length5list!=[]:
        print(length5list,"have 5 letter in them")
    elif length5list==[]:
        print("You entered no word with five letters in it")
main()




