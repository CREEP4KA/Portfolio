from math import *
from kandinsky import *
from random import *
from ion import *
from time import sleep
from turtle import *

class Panel:
  def __init__(self,x,y,l):
    self.x=x
    self.y=y
    self.l=l
    self.precedent=(self.x,self.y)

  def affichage(self): 
    fill_rect(self.precedent[0]-5,self.precedent[1],5,-self.l,"white")
    fill_rect(self.x-5,self.y,5,-self.l,"black")
    
  def up(self):
    self.precedent=(self.x,self.y)
    if self.y >= 50:
      self.y-=1
    self.affichage()
  
  def down(self):
    self.precedent=(self.x,self.y)
    if self.y <= 222:
      self.y+=1
    self.affichage()
  

class Ball:
  def __init__(self,x,y,a):
    self.x=x
    self.y=y
    self.a=a
    self.score = 0
    self.precedent=(self.x,self.y)
  
  def avancer(self):
    self.precedent = (self.x,self.y)
    self.x += speedi * cos(radians(self.a))
    self.y += speedi * sin(radians(self.a))

  def affichage(self):
     fill_rect(int(self.precedent[0]-2),int(self.precedent[1]+1),5,-3,"white")
     fill_rect(int(self.precedent[0]-1),int(self.precedent[1]+2),3,-5,"white")
          
     fill_rect(int(self.x-2),int(self.y+1),5,-3,"black")
     fill_rect(int(self.x-1),int(self.y+2),3,-5,"black")
  
  def rebond(self):
    if (self.y <= 3 and self.a <= 0) or (self.y >= 219 and self.a >= 0):
      self.a *= -1
      self.a += randint(-5,5)
    
    if (self.x<=20 and self.x>=15 and self.y >= p1.y-p1.l and self.y<=p1.y) or (self.x<=300 and self.x>=295 and self.y >= p2.y-p2.l and self.y<=p2.y):
      if self.a <= 0:
        self.a = -180-self.a
        self.a += randint(-5,5)
      else:
        self.a = 180-self.a
        self.a += randint(-5,5)        
      self.score += 1
def menu(x):
  fill_rect(0,0,320,222,"black")
  if x==1:
    fill_rect(45,156,96,50,"yellow")  
  else :
    fill_rect(189,156,96,50,"yellow")
      
  fill_rect(49,160,88,42,"black")
  fill_rect(193,160,88,42,"black")
  
  fill_rect(50,161,86,40,"white")
  fill_rect(194,161,86,40,"white")
  draw_string("solo",70,171)
  draw_string("multi",214,171)

  fill_rect(83,120,154,-85,"white")
  fill_rect(88,115,144,-75,"black")

  fill_rect(93,103,5,-50,"white")
  fill_rect(222,103,5,-50,"white")
  
  fill_rect(140,70,40,-5,"white")
  fill_rect(140,93,40,-5,"white")
  draw_string("<-PONG->",120,70)

while True:
  score = 0  
  speedi = 0.3
  select = 1
  
  menu(select)
  while not keydown(KEY_OK):
    if keydown(KEY_LEFT) or keydown(KEY_RIGHT):
      select*=-1
      menu(select)
      sleep(0.2)


  p1 = Panel(20,111,50)
  if select == 1:
    p2 = Panel(300,222,222)
  else :
    p2 = Panel(300,111,50)


  balle = Ball(160,111,randint(-30,30))
  if random() > 0.5:
    if balle.a <= 0:
      balle.a = -180-balle.a
      balle.a += randint(-5,5)
    else:
      balle.a = 180-balle.a
      balle.a += randint(-5,5)        

  fill_rect(0,0,320,222,"white")  
  p2.affichage()
  p1.affichage()
  balle.affichage()
  sleep(1)
  
  while balle.x > 5 and balle.x < 315:
  
    p1.affichage()
    p2.affichage()
    balle.affichage()
  
    if keydown(KEY_UP):
      p1.up()
    if keydown(KEY_DOWN):
      p1.down()
    if keydown(KEY_SIX):
      p2.up()
    if keydown(KEY_THREE):
      p2.down()
  
    balle.rebond()
    balle.avancer()
    #color(0,0,0)
    #draw_string(str(balle.score),130,222)
    if speedi < 3.3:
      speedi *= 1.0005
    print(speedi)
  while not keydown(KEY_OK):
    pass
    
  sleep(0.3)



