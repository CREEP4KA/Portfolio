# -*- coding: utf-8 -*-

from random import *

class Pokemon:
    
    def __init__(self,nom,niveau,points_de_vie,attaque_min,attaque_max,defense,vitesse):
        
        """constructeur"""
        
        self.nom = nom
        self.niveau = niveau
        self.__points_de_vie = points_de_vie
        self.attaque_min = attaque_min
        self.attaque_max = attaque_max
        self.defense = defense
        self.vitesse = vitesse
    
    def __str__(self):
        
        """Représentation de l'objet sous forme de chaine de caractères"""
        
        return self.nom + ", " + str(self.niveau) + ", " + str(self.__points_de_vie) + ", " + str(self.attaque_min) + ", "+ str(self.attaque_max) + ", " + str(self.defense)   
    
    def get_points_de_vie(self):
        
        """"Accesseur du nombre de points de vie"""
        
        return self.__points_de_vie
    
    def get_vitesse(self):
        
        """"Accesseur de la vitesse"""
        
        return self.vitesse
        
    def set_points_de_vie(self,valeur):
        
        """"Mutateur du nombre de points de vie"""
    
        self.__points_de_vie = int(valeur)
    
    
    def attaque(self):
        
        """Définit la valeur de l'attaque"""
        
        return randint(self.attaque_min, self.attaque_max)
    
    def defense_valeur(self):
        
        """Définit la valeur de la defense"""
        
        return int(randint(50,100) * self.defense/100)
    
    def est_en_vie(self):
        
        """Renvoie True si les points de vie sont supérieurs à zéro"""
        
        return self.get_points_de_vie() > 0


class Arene:
    
    def __init__(self, pokemon1, pokemon2, nom):
        """" Constructeur de la classe arene qui prends en arguments 2 pokemons"""
        
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.nom = nom
        
    def __str__(self):
        """renvoie un str"""
        
        return str(self.nom + ", " + self.pokemon1 + ", " + self.pokemon2)

    def fin(self):
        
        """Renvoie True si l'un des deux pokemons n'est plus en vie"""
        
        return not( self.pokemon1.est_en_vie()) or not(self.pokemon2.est_en_vie())
    
    def jouer_tour(self,attaquant,defenseur):
        
        """Modifie les points de vie du defenseur en fonction de la puissance d'attaque de l'attaquant"""
        
        val_attaque = attaquant.attaque()
        armure = defenseur.defense_valeur()
        degats = val_attaque-armure
        

        
        if degats > 0:
        
            if degats > defenseur.get_points_de_vie() :
                defenseur.set_points_de_vie(0)
            else:
                defenseur.set_points_de_vie(defenseur.get_points_de_vie()-(val_attaque-armure))
            print(attaquant.nom + " attaque avec une puissance de "+ str(val_attaque) +" "+ defenseur.nom +" absorbe " + str(armure) + " dégats")
       
            print(attaquant.nom + " : " + str(attaquant.get_points_de_vie()))
            print(defenseur.nom + " : " + str(defenseur.get_points_de_vie()))

        
    def plus_rapide(self,pokemon1,pokemon2):
        
        """détermine quel est le pokemon le plus rapide"""
        
        vitesse1 = random()*self.pokemon1.get_vitesse()
        vitesse2 = random()*self.pokemon2.get_vitesse()
        
        if vitesse1 > vitesse2:
            return self.pokemon1
        
        elif vitesse2 > vitesse1:
            return self.pokemon2
        
        else:
            return self.pokemon1 or self.pokemon2
        
    def combattre(self):
        
        """game loop"""

        
        while self.fin() != True:
            
            if self.plus_rapide(self.pokemon1,self.pokemon2) == self.pokemon1 :
                self.jouer_tour(self.pokemon1, self.pokemon2)
            
                if self.fin() != True:
                    self.jouer_tour(self.pokemon2, self.pokemon1)
            else:
                self.jouer_tour(self.pokemon2, self.pokemon1)
            
                if self.fin() != True:
                    self.jouer_tour(self.pokemon1, self.pokemon2)
            
    def vainqueur(self):
        
        """renvoie le nom du vainqueur si le combat est terminé et None sinon"""
        
        if self.pokemon1.est_en_vie() == True :
            
            return self.pokemon1.nom
        
        elif self.pokemon2.est_en_vie() == True:
            
            return self.pokemon2.nom
        
        else :
            return None
        
    def ko(self):
        
        """verifie quels sont les pokemons k-o"""
        
        if self.pokemon1.est_en_vie() == False :
            return self.pokemon1.nom
        elif self.pokemon2.est_en_vie() == False :
            return self.pokemon2.nom
        else :
            return None

poke1 = Pokemon("Dracaufeu",100,232,104,167,20,90)
poke2 = Pokemon("Tortank",100,132,102,165,30,70)


ABriand = Arene(poke1 , poke2, "ABriand")


proba = [0,0,0,0,0,0,0,0,1,1]

  

ABriand.combattre()
print(ABriand.vainqueur() + " a gagné")
print(ABriand.ko()+" est K-O")

    
