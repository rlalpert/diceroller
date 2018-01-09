from diceroller import _parse_input
from diceroller import _convert_to_rolls
from diceroller import _get_total
from diceroller import Roll

def test_parse_input_regex():
    assert _parse_input('1d4 +7-2d9') == [('+1d4', '+', '1', '4'), ('-2d9', '-', '2', '9'), '+7']
    assert _parse_input('-200d8 +50 -10monster') == [('-200d8', '-', '200', '8'), '+50', '-10']
    assert _parse_input('50-2d8 + 100d100x') == [('-2d8', '-', '2', '8'), ('+100d100', '+', '100', '100'), '+50']
    assert _parse_input('-50-2d8 + 100d100x') == [('-2d8', '-', '2', '8'), ('+100d100', '+', '100', '100'), '-50']
    assert _parse_input('+50 - 2d8/15') == [('-2d8', '-', '2', '8'), '+50']
    assert _parse_input('+50-2d8') == [('-2d8', '-', '2', '8'), '+50']
    assert _parse_input('+25d8') == [('+25d8', '+', '25', '8')]
    assert _parse_input('25d8') == [('+25d8', '+', '25', '8')]

def test_convert_to_rolls_output():
    rolls = _parse_input('-100d10 + 5d8 -23 +8')
    actual_raw = _convert_to_rolls(rolls)
    actual = []
    for item in actual_raw:
        delattr(item, 'all_rolls')
        delattr(item, 'total')
        actual.append(item.__dict__)
    expected = [{'dice_roll': '-100d10', 'multiplier': -1, 'modifier': 0, 'dice_count': 100, 'dice_type': 10}, {'dice_roll': '+5d8', 'multiplier': 1, 'modifier': 0, 'dice_count': 5, 'dice_type': 8}, {'dice_roll': '-23', 'multiplier': -1, 'modifier': 23, 'dice_count': 0, 'dice_type': 0}, {'dice_roll': '+8', 'multiplier': 1, 'modifier': 8, 'dice_count': 0, 'dice_type': 0}]
    assert actual == expected 

def test_convert_to_rolls_totals_output():
    rolls = _parse_input('5d10+20')
    actual_raw = _convert_to_rolls(rolls)
    actual = []
    for item in actual_raw:
        actual.append(item.__dict__)
    for roll in actual:
        assert type(roll['total']) == int
        if roll['all_rolls']:
            for item in roll['all_rolls']:
                assert type(item) == int

def test_get_total():
    rolls_list = [
        Roll(0,0,0,0,0,0,15), 
        Roll(0,0,0,0,0,0,-5), 
        Roll(0,0,0,0,0,0,10)]

    assert _get_total(rolls_list) == 20



