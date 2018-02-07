# Diceroller

* Rolls DnD style dice. 

# Usage

To install:

`pip install diceroller`

Example usage:

```python
import diceroller

# returns an int
diceroller.roll("1d20 +3 -1d10")
14

# returns a dictionary
diceroller.roll_detailed("2d20-1d6+3-1")
{"total": 18, "rolls": [12, 7, -3], "modifiers": [3, -1]}

# returns a significantly more complex dictionary
diceroller.roll_detailed_dev("2d20-1d8+2-1")
{'total': 24, 'detailed_rolls': 
  [{'dice_roll': '+2d20', 'multiplier': 1, 'modifier': 0, 'dice_count': 2, 
    'dice_type': 20, 'all_rolls': [15, 12], 'total': 27}, 
  {'dice_roll': '-1d8', 'multiplier': -1, 'modifier': 0, 'dice_count': 1, 
    'dice_type': 8, 'all_rolls': [4], 'total': -4}, 
  {'dice_roll': '+2', 'multiplier': 1, 'modifier': 2, 'dice_count': 0, 
    'dice_type': 0, 'all_rolls': None, 'total': 2}, 
  {'dice_roll': '-1', 'multiplier': -1, 'modifier': 1, 'dice_count': 0, 
    'dice_type': 0, 'all_rolls': None, 'total': -1}]}
```

# To-Do

* Get average rolls from roll info.
* Validate input so that they are 
  1. all integers
  2. do not exceed 4 digits
