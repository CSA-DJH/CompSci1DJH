import os,time,random
os.system("clear")

def greeting():
    print("Hello!!")
    name=input("What is your name? ")
    name=name.title()
    print("Hi "+name+"!")
    global name

greeting()

def race():
    print('''
The classes are:
    
=====================================================
Human - special ability - Agile, Sneaky
-----------------------------------------------------
Brute - special ability - Strong, Scary
-----------------------------------------------------
Bandito - special ability - Manipulator, Pickpocket
-----------------------------------------------------
Plebian - special ability - Average guy, Normal
=====================================================
    
 ''')
    
    
    pick=input("what class would you like too play? ")
    pick=pick.title()
    races=open("/storage/sdcard0/Download/finalproject1.txt", "r")    
    list1=races.readlines() 
    list1=[item.strip() for item in list1]
    player=open("/storage/sdcard0/Download/finalprojectplayer.txt", "w")
    if pick in list1:
        player.write(pick + '\n')
    else:
        print("That is not in the class list!  (be sure to spell correctly!)")
        time.sleep(1)
        os.system("clear")
        race()
    global player, pick
    time.sleep(1)
    os.system("clear")
  
     
def checking():   
    if pick=="Human":
       print("You picked Human! Hi, "+name+"!")
       print("What starting weapon would you like to choose?")
       fweapon=input("Your options are:  Chopping axe (1) or   Wooden baseball bat (2) .  ") 
       if fweapon=="1":
           player.write("Chopping axe"+ '\n')
       elif fweapon=='2':
           player.write("Wooden baseball bat"+ '\n')
       else:
           print("That is not a option!")
           time.sleep(1)
           os.system("clear")
           checking()

    elif pick=="Brute":
       print("You picked Brute! Hi, "+name+"!")
       print("What starting weapon would you like to choose?")
       fweapon=input("Your options are:  Sledgehammer (1) or   Rock (2).  ")
       if fweapon=="1":
           player.write("Sledgehammer"+ '\n')
       elif fweapon=='2':
           player.write("Rock"+ '\n')
       else:
           print("That is not a option!")
           time.sleep(1)
           os.system("clear")
           checking()


    elif pick=="Bandito":
       print("You picked Bandito! Hi, "+name+"!")
       print("What starting weapon would you like to choose?")
       fweapon=input("Your options are:  Switchblade(1)  or   Spikey gloves(2) .  ")
       if fweapon=="1":
           player.write("Switchblade"+ '\n')
       elif fweapon=='2':
           player.write("spikey gloves"+ '\n')
       else:
           print("That is not a option!")
           time.sleep(1)
           os.system("clear")
           checking()

    
    elif pick=="Plebian":
       print("You picked Plebian! Hi, "+name+"!")
       print("What starting weapon would you like to choose?")
       fweapon=input("Your options are:  Fists(1)  or   Fists(2).  ")
       
       if fweapon=="1":
           player.write("Fists"+ '\n')
       elif fweapon=='2':
           player.write("Fists"+ '\n')
       else:
           print("That is not a option!")
           time.sleep(1)
           os.system("clear")
           checking()

    elif pick=="Can Of Baked Beans":
        print("You are a can of baked beans...")
        time.sleep(2)
        quit()
     
    player.write("100")
    player.write('\n')
    player.close()
          
race()
checking()

def story():
    
    num1=open("/storage/sdcard0/Download/finalprojectplayer.txt", "r")
    num2=num1.readlines()
    os.system("clear")
    print('You were a lonely farmer until one day the evil Spartals came to your farm to collect taxes. You grabbed the nearest weapon, a '+ num2[1]+", and fended of a group a Spartals because you had enough of their repressive ways.")
    print("You swear to destroy the evil regime and bring fairness to the land!!")
    print("And with that you set off to bring down the evil king, Turtus.")
    time.sleep(10)

story()

def first():
    town=input("Would you like to go to the city(1), or to the small town(2)?")
    if town=="1":
        print("You decided to go to the city.")
    elif town=="2":
        print("you decided to go to the town.")
    else:
        print("That is not an option")
        first()
        
first()









