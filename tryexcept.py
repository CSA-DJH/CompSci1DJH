def valuetry():
    try:
        num2=input("what number")
        num2=int(num2)
        print(num2)
    except ValueError:
        print("wrong")
        valuetry()

def filetry():
    try:
        ref=open('hdfbs','r')
    except IOError:
        print("BAD")
    

def variabletry():
    try:
        print(x)
    except NameError:
        x=input("what is your name")
        print(x)
        

valuetry()
filetry()
variabletry()