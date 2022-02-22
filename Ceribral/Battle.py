from Ceribral import enestats
from save import *
import os
import random
import time
from Functions import *
import Functions
# Variables
i = 1
coins = 0
exp = 0
lvl = 1
hp = 20
rando = 1
mobid = 0
options = 0
Battle = 0
damage = 2
# Battle Functions
def mobgen():
  rando = random.randint(1,1)
def battle():
  if rando == 1:
    print("A Wild Zombie attacks")
    print("What would you like to do\n\n(1) Attack\n\n(2) Defend\n\n(3) Run")
    Battle = input("")
    if Battle == "1":
      print("Attacking Zombie")
      time.sleep(0.5)
      zombiehp - damage
      print("Zombie hp:", zombiehp)
      print("The Zombie attacked")
      hp - zombieatk