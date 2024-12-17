alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

morse = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
norm = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z"}

def is_morse(phrase):
  for letter in phrase:
    if letter != " " and letter!= "-" and letter!= "." :
      return False
    return True

def is_norm(phrase):
    
  for letter in phrase:
    if letter != " " and letter not in alphabet:
      return False
    return True

def decoupage(phrase):
  mot = ""
  trad = []
  
  for element in phrase:
    
    if element != " ":
      mot += element
    
    else:
      trad.append(mot)
      mot = ""
 
  trad.append(mot)
  mot = ""
  return trad  
        
def traduction(phrase):
  final=""
  lignes = 1
  if is_morse(phrase)==True:
    for element in decoupage(phrase):
      if element != "":
        final+= norm[element]  
      else:
        if len(final)/(25*lignes)>=1:
          final+="\n"
          lignes += 1
        else:
          final+=" "
    return final
    
  elif is_norm(phrase)==True:

    for element in decoupage(phrase):
      for letter in element:
        final+= morse[letter]+" "
      
      if len(final)/(35*lignes)>=1:
        final+="\n"
        lignes += 1
      
      else:
        final+=" "
    
    return final
      
  
  else:
    return None
    
while True:
  phrase = str(input("phrase a traduire ?\n"))
  print(traduction(phrase))
  print()
  print()