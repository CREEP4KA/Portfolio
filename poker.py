# -*- coding: utf-8 -*-

import random
cartes = ["2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♥"
          "2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦"
          "2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣"
          "2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠"]

cartes_shuffled= [cartes.pop(random.randint(0,len(cartes)-1)) for k in range(len(cartes))]

used = []




class Distribution:
    
    def __init__(self,nb_joueurs):
        
        
        self.cartes_joueur = []
        self.nb_joueurs = nb_joueurs
    
    def distrib(self):
        
        
        for loop in range(2):
            carte = random.choice(cartes_shuffled)
            self.cartes_joueur.append(str(carte))
            used.append(cartes_shuffled.index(carte))
            del cartes_shuffled[cartes_shuffled.index(carte)]
            
        return self.cartes_joueur
            
    def show(self):
        
        return self.cartes_joueur
        

partie = Distribution(2)
