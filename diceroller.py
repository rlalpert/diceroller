#! python3
# diceroller.py - Rolls DnD Style Dice

import re
from random import randint

def roll(user_input):
  # Authenticate Roll
  roll_regex = re.compile(r'^(\d{1,3})d(\d{1,3})$')
  mo = roll_regex.search(user_input)

  if mo != None:
    print("{match} is valid.".format(match=mo.group(0)))
    dice_roll = mo.group(0)
    dice_count = int(mo.group(1))
    dice_type = int(mo.group(2))
    # print(randint(1, dice_type))
    total = 0
    for i in range(dice_count):
      print("Rolling " + str(i+1) + " of " + dice_roll + "...")
      this_roll = randint(1, dice_type)
      print(this_roll)
      total += this_roll
    print("Total is " + str(total))
  else:
    print("I'm sorry, I can't do that, Dave.")

while True:
  # Get input from user
  print("Please roll: ")
  user_input = input()
  try:
    roll(user_input)
  except Exception as e:
    print("Error {e}.".format(e=e))