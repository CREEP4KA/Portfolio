import random
import tkinter
import os


ip = ".".join(map(str, (random.randint(0, 255)
                        for _ in range(4))))
def yes():
    print("your IP adress is : ", ip)
def no():
    os.system("start")



l = tkinter.Label( text = "YOU WON THE NEW IPHONE WTFFFF")
l.config(font =("OMGG", 14))

b1 = tkinter.Button( text = "GET IT !!!!" , command= yes())

b2 = tkinter.Button(text = "Sell my soul to SATAN", command= no())

l.pack()
b1.pack()
b2.pack()



tkinter.mainloop()
