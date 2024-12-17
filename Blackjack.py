# -*- coding: utf-8 -*-


import random
cartes = ["2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♥",
          "2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦",
          "2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣",
          "2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠"]

numbers = ["2","3","4","5","6","7","8","9","10"]
cartes_shuffled= [cartes.pop(random.randint(0,len(cartes)-1)) for k in range(len(cartes))]
used = []

class Main:
    

    def distrib(self,deck):
        
        carte = random.choice(cartes_shuffled)
        deck.append(str(carte))
        used.append(cartes_shuffled.index(carte))
        del cartes_shuffled[cartes_shuffled.index(carte)]
            
    def vider(self,deck):
        deck = []
            
    def somme(self,deck):
        
        total = 0
        
        for element in deck:
            
            if element[0] == "A":
                if total > 10 :
                    total += 1
                else :
                    total += 11
                    
            elif element[0] in numbers:
                total += int(element[0])
                
            else:
                total += 10
                
        return total
    
    def nb_cartes(self,deck):
        return len(deck)
    
class Partie:
    
    def __init__(self, cartes_joueur = [], cartes_dealer = [] ):
        
        self.cartes_joueur = cartes_joueur
        self.cartes_dealer = cartes_dealer
        
    def distribuer(self):
        for loop in range(2):
            tapis1.distrib(self.cartes_joueur)
            tapis1.distrib(self.cartes_dealer)
        
    def ajouter(self,deck):
        tapis1.distrib(deck)
        
    def reset(self):
        tapis1.vider(self.cartes_dealer)
        tapis1.vider(self.cartes_joueur)
    
    def check_loose(self,deck):
        
        if tapis1.somme(deck) > 21:
            return True
        else :
            return False
        
    def show(self):
        
        return "\nCartes du joueur : " + str(self.cartes_joueur) + " | Cartes du dealer " + str(self.cartes_dealer) 
        
    def game(self):
        
        self.distribuer()
        
        while  (not self.check_loose(self.cartes_dealer) and not self.check_loose(self.cartes_joueur)):
            
            print(self.show()+"\n")

            test = input("1- Continue | 2- Stop\n")

            if test !="2" and test !="1" :
                pass
            
            else: 
                
                if test == "1":
                    self.ajouter(self.cartes_joueur)
                    self.show()
                
                if tapis1.somme(self.cartes_dealer) <= 17 and tapis1.somme(self.cartes_dealer) <= tapis1.somme(self.cartes_joueur):
                    self.ajouter(self.cartes_dealer)
       
                    if self.check_loose(self.cartes_joueur) or self.check_loose(self.cartes_dealer):
                        pass
                    
                elif test=="2":
                    while not self.check_loose(self.cartes_dealer) and tapis1.somme(self.cartes_dealer) <= 17:
                        self.ajouter(self.cartes_dealer)
            
            
        if not self.check_loose(self.cartes_joueur) :
            
            if not self.check_loose(self.cartes_dealer):
        
                if tapis1.somme(self.cartes_joueur)>tapis1.somme(self.cartes_dealer):
            
                    if tapis1.somme(self.cartes_joueur)==21:
                        print("-----------Blackjack !-----------")
                    print("-----------PLAYER WINS------------\n")
                    
                elif tapis1.somme(self.cartes_joueur)==tapis1.somme(self.cartes_dealer):
                    if tapis1.nb_cartes(self.cartes_joueur)<tapis1.nb_cartes(self.cartes_dealer):
                        if tapis1.somme(self.cartes_joueur)==21:
                            print("-----------Blackjack !-----------")
                        print("-----------PLAYER WINS------------")
                    else :
                        print("----------PLAYER LOSES------------")
                else :
                    print("----------PLAYER LOSES------------")
            else:
                if tapis1.somme(self.cartes_joueur)==21:
                    print("-----------Blackjack !-----------")
                print("-----------PLAYER WINS------------")
                
        else :
            print("----------PLAYER LOSES------------")
        
        print(self.show())
        
        self.reset()
    
tapis1 = Main()
partie1 = Partie()

print()
print()
partie1.game()
