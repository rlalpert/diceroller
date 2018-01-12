# Diceroller

* Rolls DnD style dice. 

# Usage

Diceroller can be run from the command line or as a package. It will search string input for DnD style dice rolls. 

As a package:

```python
import diceroller

# returns an integer with the total of the roll
diceroller.roll("1d20 +3 -1d10")

# returns a dictionary
#   "total" is an integer of the total
#   "all_rolls" is a list of dictionaries with information on each roll
diceroller.roll_detailed("-2d10 +2")
```

From the command line:

Set whether you want detailed information on each roll in `config.py`. Then, just run `__init__.py` and you'll be prompted to input a roll.

# To-Do

* Get average rolls from roll info.
* Setup more tests