#! /usr/bin/python3
# diceroller.py - Rolls DnD Style Dice

import re, pprint
from random import randint

class Roll:
    def __init__(self, dice_roll, multiplier, modifier, dice_count, dice_type, all_rolls, total):
        self.dice_roll = dice_roll
        # multiply by 1 for a positive number, multiply by -1 for a negative number
        self.multiplier = multiplier
        self.modifier = modifier
        self.dice_count = dice_count
        self.dice_type = dice_type
        self.all_rolls = all_rolls
        self.total = total

def parse_input(user_input):
    # remove all whitespace
    stripped_input = user_input.replace(' ', '')
    # regex for dice-roll format
    roll_regex = re.compile(r'(([+-]{1})(\d+)d(\d+))(?!d|\d+)')
    # opening roll with no positive modifier
    opening_roll_regex = re.compile(r'(^(\d+)d(\d+))(?!d|\d+)')
    # regex for modifiers
    modifier_regex = re.compile(r'[+-]{1}\d{1,3}(?!d|\d+)')
    # positive modifier at start of line special case
    opening_modifier_regex = re.compile(r'^\d{1,3}(?!d|\d+)')

    roll_matches = roll_regex.findall(stripped_input)
    opening_roll_matches = opening_roll_regex.findall(stripped_input)
    modifier_matches = modifier_regex.findall(stripped_input)
    opening_modifier_matches = opening_modifier_regex.findall(stripped_input)

    # Add a plus sign to any positive modifiers at the start of the line
    if opening_modifier_matches:
        opening_modifier_matches[0] = '+' + opening_modifier_matches[0]
    if opening_roll_matches:
        whole_roll = '+' + opening_roll_matches[0][0]
        opening_roll_matches[0] = (whole_roll, '+', opening_roll_matches[0][1], opening_roll_matches[0][2])

    # return a list of parsed roll information
    return opening_roll_matches + roll_matches + modifier_matches + opening_modifier_matches

def convert_to_rolls(roll_list):
    """
    Takes list created by parse_input() and converts all items to Roll class
    """
    # for item in roll_list:
    #     if type(item) is tuple:

    #     elif type(item) is str:

if __name__ == '__main__':
    while True:
        print('Please roll: ')
        user_input = input()
        print(parse_input(user_input))

# def create_roll(user_input):
#     # Authenticate Roll
#     roll_regex = re.compile(r'^(\d{1,3})d(\d{1,3})$')
#     roll_object = {}

#     mo = roll_regex.search(user_input)

#     if mo != None:
#         dice_roll = mo.group(0)
#         dice_count = int(mo.group(1))
#         dice_type = int(mo.group(2))
#         all_rolls = []
#         total = 0

#         for i in range(dice_count):
#             this_roll = randint(1, dice_type)
#             all_rolls.append(this_roll)
#         total += this_roll
#     else:
#         print("That is not a valid roll. Rolls should take the form ___d___.")
#         return
#     roll = Roll(dice_roll, dice_count, dice_type, all_rolls, total)
#     return roll

# while True:
#     print("Please roll (or hit enter to roll 1d20): ")
#     user_input = input()
#     try:
#         if user_input == '':
#             # roll 1d20 by default
#             my_roll = create_roll('1d20')
#             print(str(my_roll.total) + '\n' + str(my_roll.all_rolls))
#         else:
#             my_roll = create_roll(user_input)
#             print(str(my_roll.total) + '\n' + str(my_roll.all_rolls))
#     except ValueError as e:
#         print("You can't roll a zero-sided di.")
#     except Exception as e:
#         print("ERROR: {e}.".format(e=e))