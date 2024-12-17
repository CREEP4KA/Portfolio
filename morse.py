from random import *

morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
norm = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

while True:
  x = randint(0,25)
  
  if randint(0,1) == 1:
    print(morse[x])
    if input("What is this letter ? : ") == norm[x]:
      print("TRUE")      
    else :
      print("FALSE it was : "+norm[x])
  else:
    print(norm[x])
    if input("What is this letter ? : ")==morse[x]:
      print("TRUE")      
    else :
      print("FALSE it was : "+morse[x])
  print("")
  print("")
  




