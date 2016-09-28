import os
os.system("clear")
num1=input("What phrase would you like to change?")
    
dic={"I":"Go","like":"bake","cats":"a","and":"yummy","dogs":"blueberry","they":"filling","are":"banana","very":"creame","fuzzy":"cake","guys":"now"}

newword = []
words = num1.split()
for word in words:
    if word in dic:
        newword.append(dic[word])
    
    else:
        newword.append(word)
for i in range(len(num1.split())):
    newword[i]=newword[i].strip("',[,]")
print(((str(newword).strip("',[,]")).replace("'","")).replace(",",""))




