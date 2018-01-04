# Diceroller

* Rolls DnD style dice.

# To-Do

* Get average rolls from roll info.
* Setup more tests
* Move private functions to another file
* Move config into separate file

# Setup Virtual Environment

`python3 -m venv env`

`source env/bin/activate`

# Install Packages

`pip install -r requirements.txt`

# Usage

Can be run from the command line or as a package.

As a package:

```python
import diceroller

# returns an integer with the total of the roll
diceroller.roll("1d20 +3 -1d10")

# returns a tuple
#   first item is an integer of the total
#   second item is a list of dictionaries with information on each roll
diceroller.roll_detailed("-2d10 +2")

```

# Testing

To watch (run from project directory):
`pytest -f .`

Detailed test info:
`pytest -v`
