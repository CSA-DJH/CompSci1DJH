#Daniel Herbowy

import os
os.system("clear")
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "   #defines all letters and spaces
cypher="zxcvbnmlkjhgfdsaqwertyuiopZXCVBNMLKJHGFDSAQWERTYUIOP "        #encoded letters

def greeting():
    num7=input("what is your name?")    #asks for a name
    num7=num7.title();         #capitalizes the first letter of the word
    print("Hello "+num7+"!")    #prints a greeting
    
def encrypt():
    num1=input("What phrase would you like to encrypt? (NO SPECIAL CHARACTERS OR NUMBERS) ")   #asks for a phrase to encrypt
    num2=""            #makes an empty variable
    for num4 in num1:            #for loop
        num3=alphabet.find(num4)  #finds the letter to replace
        num2+=cypher[num3]    #adds the encrypted phrase to num2
    print(num2)    #prints the encrypted phrase
    
def decrypt():
    num1=input("(What phrase would you like to decrypt? (NO SPECIAL CHARACTERS OR NUMBERS) ") #asks what to decrypt
    num2=""     #blank variable
    for num4 in num1:              #blank variable
        num3=cypher.find(num4)        #find the letters needed to decrypt
        num2+=alphabet[num3]             #adds the decrypted phrase to the blank variable
    print(num2)    #prints the decrypted phrase

def choose():
    num8=input("1 to encrypt, 2 to decrypt, 3 to quit")    #asks if you want to encrypt decrypt or quit
    num8=int(num8)       #ints num8
    if num8==1:       #if num8 is 1, runs the encryption function
        encrypt()
    elif num8==2:      #if num8 is 2, runs the decryption function
        decrypt()
    elif num8==3:          #if num8 is 3, quits
        print("goodbye")
        print("FIRE "*35493)
        quit()
    
def again():
    num9=input("would you like to run it again? 1 for yes, 2 for no")  #asks if you want to run it again
    num9=int(num9)
    if num9==1:           #if num9 is 1, runs the choose function
        choose()
    elif num9==2:     #if num9 is 2, quits
        print("Goodbye")
        print("FIRE "*35493)
        quit()
    while 1<2:     #an infinate whle loop to run the again function
        again()    
           
greeting()
choose()
again()





