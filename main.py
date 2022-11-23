print("⚔️ Character Health Stat Generator ⚔️")

char_name = str(input("Name your warrior: "))

import random

roll = "yes"

def roll_side(sides):
  roll = random.randint(1,sides)
  return roll
  
def six_eight():
  roll6 = roll_side(6)
  roll8 = roll_side(8)
  health = roll6*roll8
  
  return health

while roll =="yes":
  health = six_eight()
  print("Your character's health is: ",health, "hp")
  roll = input("Generate new health stats for this character?")
