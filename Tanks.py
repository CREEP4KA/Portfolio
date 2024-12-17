from math import *
from ion import *
from kandinsky import *
from random import *
from turtle import write
from time import sleep

speed = 1


class Bullet:
  
  def __init__(self,x,y,a,tank):
    self.x = x
    self.y = y
    self.a = a
    self.precedent = None
    self.tank = tank
    
  def trajectoire(self):
    self.precedent = (self.x,self.y)
    self.x += speed * cos(radians(self.a))
    self.y += speed * sin(radians(self.a))
    self.collide()      
    self.affichage()
  
  def erase(self):
    fill_rect(int(self.precedent[0]-2),int(self.precedent[1]-2),4,4,"white")
  
  def affichage(self):
    self.erase()
    fill_rect(int(self.x-2),int(self.y-2),4,4,"red")
    
  def collide(self):
    if get_pixel(int(self.x),int(self.y))== (0,0,255) and self.tank != p1:
      p1.alive = False
      p1.destroy()
      return True
    elif get_pixel(int(self.x),int(self.y))==(82,195,0) and self.tank != p2:  
      p2.alive = False
      p2.destroy()
      return True
    return False
    
  
  
  
class Player:
  
  def __init__(self,x,y,a,color_tank,angle):
    self.x = x
    self.y = y
    self.a = a
    self.x_canon = self.x
    self.y_canon = self.y
    self.color_tank = color_tank
    self.angle = angle
    self.precedent = None
    self.alive = True
  
  def rotate(self):
    self.a += self.angle
    if self.a >= 360:
      self.a -= 360
    if self.a <= 0:
      self.a += 360
    self.a = round(self.a)
    

  def avancer(self):
    self.precedent = (self.x,self.y)
    self.x += speed * cos(radians(self.a))
    self.y += speed * sin(radians(self.a))  
    self.canon()
    fill_rect(int(self.precedent[0]-5),int(self.precedent[1]-5),10,10,"white")
    fill_rect(int(self.x-5),int(self.y-5),10,10,self.color_tank)
  
  def affichage(self):
    
    fill_rect(int(self.x-5),int(self.y-5),10,10,self.color_tank)
          
  def canon(self):
    self.precedent_canon = (self.x_canon,self.y_canon)

    self.x_canon = self.x + (speed+6) * cos(radians(self.a))
    self.y_canon = self.y + (speed+6) * sin(radians(self.a))  

    fill_rect(int(self.precedent_canon[0]-3),int(self.precedent_canon[1]-3),6,6,"white")
    fill_rect(int(self.x_canon-3),int(self.y_canon-3),6,6,self.color_tank)
    self.affichage()
  
  def destroy(self):
    if self.alive == False:
      for _ in range(100):
        set_pixel(randint(int(self.x-30),int(self.x+30)),randint(int(self.y-30),int(self.y+30)),"red")
        set_pixel(randint(int(self.x-30),int(self.x+30)),randint(int(self.y-30),int(self.y+30)),"orange")
    
def shoot(player):
  if len(bullets)<bullet_cap :
    if bullets == [] or sqrt((player.x-bullets[-1].x)**2+(player.y-bullets[-1].y)**2) > 40 :
      bullets.append(Bullet(player.x,player.y,player.a,player))
      for loop in range(20):
        bullets[-1].trajectoire()
      

bullets = []
bullet_cap = 30

p1 = Player(60,111,0,"blue",2)
p2 = Player(260,111,0,"green",2)

p1.affichage()
p2.affichage()


while p1.alive == True and p2.alive == True:
  p1.canon()
  p2.canon()
  anti_spam = 0
  
  if keydown(KEY_ZERO) or keydown(KEY_NINE):
    if keydown(KEY_ZERO):
      if anti_spam == 0:
        shoot(p1)
        p1.angle *= -1
      p1.avancer()
      anti_spam = 1
      if not keydown(KEY_NINE):
        p2.rotate()
      
    if keydown(KEY_NINE):
      if anti_spam == 0:
        shoot(p2)
        p2.angle *= -1  
      p2.avancer()
      anti_spam = 1
      if not keydown(KEY_ZERO):
        p1.rotate() 
    
  
  else:
    anti_spam = 0
    p1.rotate() 
    p2.rotate()

  for element in bullets:
    element.trajectoire()
    if get_pixel(int(element.x),int(element.y)) == (0,0,0):
      element.erase()
      del bullets[bullets.index(element)]