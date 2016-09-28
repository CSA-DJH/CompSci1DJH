def main():
    list1=[]
    list2=[]       #makes two empty lists
    print("please enter ten words")
    for b in range(10):        
        num1=input("please enter a word: ")     #runs a loop 10 times and asks for a word
                if len(num1)==5:     #if the word has 5 letters in it,adds it to list1
            list1.append(num1)
        else:
            list2.append(num1)    #if not 5 letters adds it to list2
          
    if list1!=[]:         #checks if the list has word in it
        print(list1,"have 5 letter in them")
    elif list1==[]:    #checks if the list has no words in it
        print("you entered no lettes with five letters in it")
    
    
    
main()
    
    