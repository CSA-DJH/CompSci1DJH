
import os,time
def add_fruit(inventory, fruit, quantity):
    try:
        inventory[fruit]=inventory[fruit]+quantity
    except:
        inventory[fruit]=quantity
    print("There are %s %s in inventory!"%(inventory[fruit],fruit))
    time.sleep(3)
def axinaquestion():
    os.system("clear")
    add_fruit(new_inventory, input("What fruit would you like to add inventory to? ").upper(), int(input("How many of this fruit would you like to add to the inventory? ")))
    axinaquestion()
new_inventory = {}
axinaquestion()