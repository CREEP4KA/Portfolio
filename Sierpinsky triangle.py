from random import *
from turtle import color
from math import sqrt,acos,pi
from kandinsky import *


def triangle_g(x):
  return x*sqrt(3)+100*sqrt(3)

def triangle_d(x):
  return -x*sqrt(3)+100*sqrt(3)


def triangle():
  angles = [(-100,100),(100,100),(0,-100*sqrt(3)+100)]
  
  turtle_x = randint(-100,100)
  if turtle_x >= 0:
    turtle_y = randint(-100,int(triangle_d(turtle_x)))
  else :
    turtle_y = randint(-100,int(triangle_g(turtle_x)))
    
  while True:
    select = choice(angles)
    turtle_x = int((turtle_x+select[0])/2)
    turtle_y = int((turtle_y+select[1])/2)
    set_pixel(turtle_x+160,turtle_y+111,'black')
    
def square():
  angles = [(100,100),(100,-100),(-100,100),(-100,-100),(0,100),(100,0),(0,-100),(-100,0)]
  turtle_x = randint(-100,100)
  turtle_y = randint(-100,100)
  
  while True:
    select = choice(angles)        
    turtle_x = int((turtle_x-select[0])/3+select[0])
    turtle_y = int((turtle_y-select[1])/3+select[1])
    set_pixel(turtle_x+160,turtle_y+111,"black")

def pentagon():
  angles = [(-60,100),(60,100),(97.08,-14.13),(0,-84.66),(-97.08,-14.13)]
  turtle_x = randint(-100,100)
  turtle_y = randint(-100,100)
  
  while True:
    select = choice(angles)        
    turtle_x = int((turtle_x-select[0])/3+select[0])
    turtle_y = int((turtle_y-select[1])/3+select[1])
    set_pixel(turtle_x+160,turtle_y+111,"black")

def hexagon():
  angles = [(-60,100),(60,100),(120,-3.92),(60,-107.85),(-60,-107.85),(-120,-3.92)]
  turtle_x = randint(-100,100)
  turtle_y = randint(-100,100)

  while True:
    select = choice(angles)        
    turtle_x = int((turtle_x-select[0])/3+select[0])
    turtle_y = int((turtle_y-select[1])/3+select[1])
    set_pixel(turtle_x+160,turtle_y+111,"black")

def julia():
  a = complex(0,0)
  c = 0
  
  
  c = 0.165625
  z = (sqrt(0.818125)*i)**2
  while True:
    z**2+c