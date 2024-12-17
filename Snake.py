from math import *
from random import *
from kandinsky import *
from time import *
from ion import *

def board():
  x=0
  i=1
  c1=["0",'green',color(0,255,0)]
  for loop in range(16):
    y=0
    for loop in range(12):
      if (x,y) not in snake+[the_apple]:
        fill_rect(x,y,20,20,c1[i])
      y+=20
      i*=-1
      if (x,y) not in snake+[the_apple]:
        fill_rect(x,y,20,20,c1[i])
      y+=20
      i*=-1
    i*=-1
    x+=20


def apple(x,y):
  fill_rect(x+2,y+5,16,10,'red')
  fill_rect(x+5,y+2,10,16,'red')
  fill_rect(x+7,y+4,2,2,'white')
  fill_rect(x+10,y,2,4,color(0,100,0))
  
def body(x,y,c):
  fill_rect(x,y,20,20,c)
  
def right(tab):
  tab.insert(0,(tab[0][0]+20,tab[0][1]))
  if tab[0] != the_apple:
    del tab[-1]
    
def left(tab):
  tab.insert(0,(tab[0][0]-20,tab[0][1]))
  if tab[0] != the_apple:
    del tab[-1]
    
def up(tab):
  tab.insert(0,(tab[0][0],tab[0][1]-20))
  if tab[0] != the_apple:
    del tab[-1]
    
def down(tab):
  tab.insert(0,(tab[0][0],tab[0][1]+20))
  if tab[0] != the_apple:
    del tab[-1]

  
    

direction = "right"
snake = [(40,100)]  
the_apple=tuple()
speedi = 0.1
score=0

board()
sleep(0.5)

the_apple=(randint(5,15)*20,randint(0,10)*20)
apple(the_apple[0],the_apple[1])

while True:
  board()  
  
  speedi = 0.1-(len(snake)*0.005)
  
  i=255
  for element in snake:
    body(element[0],element[1],color(0,0,i))
    i-=5
  if direction == "right" or direction == "left":
    fill_rect(snake[0][0]+7,snake[0][1]+2,6,6,"white")
    fill_rect(snake[0][0]+7,snake[0][1]+12,6,6,"white")
    fill_rect(snake[0][0]+9,snake[0][1]+4,2,2,"black")
    fill_rect(snake[0][0]+9,snake[0][1]+14,2,2,"black")
  else:
    fill_rect(snake[0][0]+2,snake[0][1]+7,6,6,"white")
    fill_rect(snake[0][0]+12,snake[0][1]+7,6,6,"white")
    fill_rect(snake[0][0]+4,snake[0][1]+9,2,2,"black")
    fill_rect(snake[0][0]+14,snake[0][1]+9,2,2,"black")
  
  if direction=="right":
    right(snake)
    sleep(speedi)
  
  if direction=="left":
    left(snake)
    sleep(speedi)
    
  if direction=="up":
    up(snake)
    sleep(speedi)
    
  if direction=="down":
    down(snake)
    sleep(speedi)
    
  if keydown(KEY_RIGHT) and direction!="left":
    direction="right"
  
  if keydown(KEY_LEFT) and direction!="right":
    direction="left"
    
  if keydown(KEY_UP) and direction!="down":
    direction="up"
  
  if keydown(KEY_DOWN) and direction!="up":
    direction="down"
  
  if snake[0][0]>310 or snake[0][0]<0 or snake[0][1]>210 or snake[0][1]<0 or snake[0] in snake[1:]:
    break
  
  if snake[0]==the_apple:
    while the_apple in snake:
      the_apple=(randint(0,15)*20,randint(0,10)*20)
    apple(the_apple[0],the_apple[1])
    score +=1
draw_string("score : "+str(score),0,0)