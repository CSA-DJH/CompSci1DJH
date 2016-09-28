import os
os.system("clear")
def main():
  alphalist2=['w','x','y','z']   #defines letters
  print(alphalist2 * 5)       #prints the list 5 times
  alphalist2[0:0] = ('a','b','c')     #adds a b and c
  print(alphalist2 * 3)     #prints it three times
main()