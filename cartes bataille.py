import random,sleep
cartes=["1♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","V♠","Q♠","K♠","A♠",
        "1♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","V♣","Q♣","K♣","A♣",
        "1♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","V♥","Q♥","K♥","A♥",
        "1♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","V♦","Q♦","K♦","A♦"]
random.shuffle(cartes)

p1=[]
p2=[]
tour=0
def distribuer():
    for loop in range(27):
        p1.append(cartes[1])
        del(cartes[1])
        p2.append(cartes[1])
        del(cartes[1])

while len(p1) or len(p2) !=0:
    print("TOUR ",tour)
    sleep(1)
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    print("Player One       Player Two")
    print("   ",p1[0],"        ",p2[0],"    ")
    if p1[0]<p2[0]:
        print("-------Player 2 Wins--------")
        del(p1[0])
        del(p2[0])
    elif p1[0]>p2[0]:
        print("-------Player 1 Wins--------")
        del(p1[0])
        del(p2[0])
    else:
        print("Player One       Player Two")
        print("   ?        ?    ")
        print("   ",p1[2],"        ",p2[2],"    ")





