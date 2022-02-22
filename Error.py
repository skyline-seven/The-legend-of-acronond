import enestats
from save import *
import os
import random
import time
from Functions import *
import Functions

# Cheats
def cheat():
  print("Cheat Menu:\n\n(1) Edit Stats")
  yek = input("")
  if yek == "1":
    print("Set your Stats:")
    coins = input("")
    exp = input("")
    lvl = input("")
    hp = input("")
    damage = input("")
    
    f = open('save.py', 'w')
    f.write("coins = " + str(coins) + "\n")
    f.write("exp = " + str(exp) + "\n")
    f.write("level = " + str(lvl) + "\n")
    f.write("hp = " + str(hp) + "\n")
    f.write("damage = " + str(damage) + "\n")
    f.close()