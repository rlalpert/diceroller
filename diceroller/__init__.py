#! /usr/bin/python3
# diceroller.py - Rolls DnD Style Dice

import re
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

def _parse_input(user_input):
    # remove all whitespace
    stripped_input = user_input.replace(' ', '')
    # regex for dice-roll format
    roll_regex = re.compile(r'(([+-]{1})(\d{1,4})d(\d{1,4}))(?!d|\d+)')
    # opening roll with no positive modifier
    opening_roll_regex = re.compile(r'(^(\d{1,4})d(\d{1,4}))(?!d|\d+)')
    # regex for modifiers
    modifier_regex = re.compile(r'[+-]{1}\d{1,4}(?!d|\d+)')
    # positive modifier at start of line special case
    opening_modifier_regex = re.compile(r'^\d{1,4}(?!d|\d+)')

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

def _convert_to_rolls(roll_list):
    """
    Takes list created by _parse_input() and converts all items to Roll class
    """
    rolls_list = []
    for item in roll_list:
        if type(item) is tuple:
            dice_count = int(item[2])
            dice_type = int(item[3])
            all_rolls = []
            total = 0
            multiplier = int(item[1] + str(1))
            for i in range(dice_count):
                this_roll = randint(1, dice_type)
                all_rolls.append(this_roll)
                total += this_roll
            rolls_list.append(
                Roll(item[0], 
                    multiplier,
                    0,
                    dice_count,
                    dice_type,
                    all_rolls,
                    total*multiplier)
                )
        elif type(item) is str:
            multiplier = 0
            modifier = int(item[1:])
            if int(item) > 0:
                multiplier = 1
            else:
                multiplier = -1
            total = modifier * multiplier
            rolls_list.append(
                Roll(item,
                    multiplier,
                    modifier,
                    0,
                    0,
                    None,
                    total)
                )
    return rolls_list

def _get_total(rolls_list):
    total = 0
    for roll in rolls_list:
        total += roll.total
    return total

def roll(user_input):
    """
    Returns the result of the roll only as an integer.
    """
    parsed_input = _parse_input(user_input)
    parsed_rolls = _convert_to_rolls(parsed_input)
    total = _get_total(parsed_rolls)
    return total

def roll_detailed(user_input):
    """
    Returns a dictionary with the following keys:
    - total (int)
    - rolls (list)
    - modifiers (list)
    """
    parsed_input = _parse_input(user_input)
    parsed_rolls = _convert_to_rolls(parsed_input)
    total = _get_total(parsed_rolls)
    rolls = []
    for roll in parsed_rolls:
        if roll.all_rolls:
            for r in roll.all_rolls:
                rolls.append(r * roll.multiplier)
    modifiers = [roll.modifier*roll.multiplier for roll in parsed_rolls if roll.modifier]
    return {"total": total, "rolls": rolls, "modifiers": modifiers}

def roll_detailed_dev(user_input):
    """
    Returns a dictionary with the following keys:
    - total (int)
    - detailed_rolls (list)
        -- the detailed rolls expose all Rolls in dictionary format
    """
    parsed_input = _parse_input(user_input)
    parsed_rolls = _convert_to_rolls(parsed_input)
    total = _get_total(parsed_rolls)
    detailed_rolls = [roll.__dict__ for roll in parsed_rolls]
    return {"total": total, "detailed_rolls": detailed_rolls}
