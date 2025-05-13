# -*- coding: utf-8 -*-

import numpy as np

# 0 aucun
# 1 pierre
# 2 feuille
# 3 ciseaux

# 0 nulle
# 1 perdue
# 2 gagnée

# nombre jouees

# proportion gagnée


valeur_mystere = input("[coup joué, résultat, nombre jouées, winrate]\n").split(",")
valeur_mystere = [int(k) for k in valeur_mystere]


entrees = np.array( ([3,0,0,0],[3,0,0,0],
                     
                     [1,2,0,0],[3,1,0,0],
                     [2,1,1,0],[3,2,1,1],
                     [1,1,2,0],[2,2,2,1],
                     [1,1,3,0],[2,2,3,1],
                     [3,2,4,0],[2,1,4,1],
                     [1,1,5,1/5],[2,2,5,4/5],
                     [1,2,6,1/6],[3,1,6,5/6],
                     [2,1,7,2/7],[3,2,7,5/7],
                     [1,1,8,2/8],[2,2,8,6/8],
                     
                     [1,0,0,0],[1,0,0,0],
                     [1,0,1,0],[1,0,1,0],
                     [1,0,2,0],[1,0,2,0],
                     [3,1,3,0],[1,2,3,0],
                     
                     [3,2,0,0],[2,1,0,0],
                     
                     [1,1,0,0],[2,2,0,0],
                     
                     [1,2,0,0],[2,1,0,0],
                     
                     
                     valeur_mystere

                     
                     ) , dtype = float)

y_pierre = np.array( ([0],[0],
                      
                      [1],[0],
                      [0],[0],
                      [1],[0],
                      [1],[0],
                      [0],[0],
                      [1],[0],
                      [1],[0],
                      [0],[0],
                      [1],[0],
                      
                      [1],[1],
                      [1],[1],
                      [1],[1],
                      [0],[1],
                      
                      [0],[0],
                      
                      [1],[0],
                      
                      [1],[0]
                      
                      ) , dtype = float)

y_feuille = np.array( ([0],[0],
                      
                      [0],[0],
                      [1],[0],
                      [0],[1],
                      [0],[1],
                      [0],[1],
                      [0],[1],
                      [0],[0],
                      [1],[0],
                      [0],[1],
                      
                      [0],[0],
                      [0],[0],
                      [0],[0],
                      [0],[0],
                      
                      [0],[1],
                      
                      [0],[1],
                      
                      [0],[1]
                      
                      ) , dtype = float)

y_ciseaux = np.array( ([1],[1],
                      
                      [0],[1],
                      [0],[1],
                      [0],[0],
                      [0],[0],
                      [1],[0],
                      [0],[0],
                      [0],[1],
                      [0],[1],
                      [0],[0],
                      
                      [0],[0],
                      [0],[0],
                      [0],[0],
                      [1],[0],
                      
                      [1],[0],
                      
                      [0],[0],
                      
                      [0],[0]
                      
                      ) , dtype = float)


entrees = entrees/np.amax(entrees, axis = 0)

X = np.split(entrees,[len(entrees)-2])[0]
Prediction = np.split(entrees,[len(entrees)-2])[1]


class NeuralNetwork:
    def __init__(self):
        self.inputSize = 4
        self.outputSize = 1
        self.hiddenSize = 5
        
        self.W1 = np.random.randn(self.inputSize,self.hiddenSize)
        self.W2 = np.random.randn(self.hiddenSize,self.outputSize)
        
    def forward(self,X):
        
        self.z =np.dot(X,self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2,self.W2)
        output = self.sigmoid(self.z3)
        return output
    def sigmoid(self, s):
        return 1/(1+np.exp(-s))
    
    def sigmoidPrime(self,s):
        return s * (1-s)
    
    def backward(self,X,y,output) :
        
        self.output_error = y - output
        self.output_delta = self.output_error * self.sigmoidPrime(output)
        
        self.z2_error = self.output_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
        
        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.output_delta)
        
    def train(self,X,y):
        output = self.forward(X)
        self.backward(X,y,output)
        
        
reseau = NeuralNetwork() 
output = reseau.forward(X)

for i in range(30):
    print(str(i) + "\n")
    print("Valeurs d'entrées : \n" + str(X))
    print("Sortie attendue : \n" + str(y_pierre) + "\n" + str(y_feuille)+ "\n" + str(y_ciseaux))
    print("Sortie prédite :\n" + str(np.matrix.round(reseau.forward(X),2)))
    print()
    reseau.train(X,y_pierre)
    reseau.train(X,y_feuille)
    reseau.train(X,y_ciseaux)
