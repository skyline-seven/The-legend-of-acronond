from enestats import *
from save import *
from Error import *
import os
import random
import time
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
# Main Functions
def mobgen():
  rando = random.randint(1,1)
def battle():
  if rando == 1:
    while zombiehp != 0 or hp != 0:
    
      print("A Wild Zombie attacks")
      print("What would you like to do\n\n(1) Attack\n\n(2) Defend\n\n(3) Run")
      Battle = input("")
      if Battle == "1":
        print("Attacking Zombie")
        time.sleep(0.5)
        zombiehp -= damage
        print("Zombie Hp:", zombiehp)
        print("The Zombie attacked")
        hp -= zombieatk
        print("Your Hp", hp)
        
      
def opcheck():
  print("Welcome Your current options are\n\n(1) Grind\n\n(2) Check Stats\n\n(3) leave\n\n(4) Save")
  options = input("")
  
  if options == "1":
    mobgen()
    battle()
  elif options == "2":
    cs()
  elif options == "3":
    exit()
  elif options == "4":
    save()
  elif options == "9923":
    print("Cheat Menu Active")
    cheat()
  else:
    print("Error")
        
def save():
  print("Saving...")
  f = open('save.py', 'w')
  f.write("coins = " + str(coins) + "\n")
  f.write("exp = " + str(exp) + "\n")
  f.write("level = " + str(lvl) + "\n")
  f.write("hp = " + str(hp) + "\n")
  f.write("damage = " + str(damage) + "\n")
  time.sleep(5)
  f.close()
  print("Saved!")
def cs():
  print("Your stats are:\nHealth:",hp)
  print("Level:",lvl)
