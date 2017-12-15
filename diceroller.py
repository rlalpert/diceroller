#! /usr/bin/python3
# diceroller.py - Rolls DnD Style Dice

import re, pprint
from random import randint

class Roll:
  def __init__(self, dice_roll, dice_count, dice_type, all_rolls, total):
    self.dice_roll = dice_roll
    self.dice_count = dice_count
    self.dice_type = dice_type
    self.all_rolls = all_rolls
    self.total = total

def create_roll(user_input):
  # Authenticate Roll
  roll_regex = re.compile(r'^(\d{1,3})d(\d{1,3})$')
  roll_object = {}

  mo = roll_regex.search(user_input)

  # if mo != None:
  #   print("{match} is valid.".format(match=mo.group(0)))
  #   dice_roll = mo.group(0)
  #   dice_count = int(mo.group(1))
  #   dice_type = int(mo.group(2))
  #   total = 0
  #   for i in range(dice_count):
  #     print("Rolling " + str(i+1) + " of " + dice_roll + "...")
  #     this_roll = randint(1, dice_type)
  #     print(this_roll)
  #     total += this_roll
  #   print("Total is " + str(total))
  # else:
  #   print("I'm sorry, I can't do that, Dave.")
  if mo != None:
    dice_roll = mo.group(0)
    dice_count = int(mo.group(1))
    dice_type = int(mo.group(2))
    all_rolls = []
    total = 0

    for i in range(dice_count):
      this_roll = randint(1, dice_type)
      all_rolls.append(this_roll)
      total += this_roll
  else:
    print("That is not a valid roll. Rolls should take the form ___d___.")
    return
  roll = Roll(dice_roll, dice_count, dice_type, all_rolls, total)
  print(str(roll.total) + '\n' + str(roll.all_rolls))
  return roll

while True:
  # Get input from user
  print("Please roll: ")
  user_input = input()
  try:
    create_roll(user_input)
  except ValueError as e:
    print("You can't roll a zero-sided di.")
  except Exception as e:
    print("ERROR: {e}.".format(e=e))