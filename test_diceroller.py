from diceroller import parse_input
from diceroller import convert_to_rolls
# def test_parse_input_regex():
#     """ Return in the format (roll string, positive or negative 1, dice count int, dice type int, modifier amount int) """
#     assert parse_input('1d4 +7-2d9') == [('1d4', 1, 1, 4, 0), ('-2d9', -1, 2, 9, 0), ('+7', 1, 0, 0, 7)]

def test_parse_input_regex():
    assert parse_input('1d4 +7-2d9') == [('+1d4', '+', '1', '4'), ('-2d9', '-', '2', '9'), '+7']
    assert parse_input('-200d8 +50 -10monster') == [('-200d8', '-', '200', '8'), '+50', '-10']
    assert parse_input('50-2d8 + 100d100x') == [('-2d8', '-', '2', '8'), ('+100d100', '+', '100', '100'), '+50']
    assert parse_input('-50-2d8 + 100d100x') == [('-2d8', '-', '2', '8'), ('+100d100', '+', '100', '100'), '-50']
    assert parse_input('+50 - 2d8/15') == [('-2d8', '-', '2', '8'), '+50']
    assert parse_input('+50-2d8') == [('-2d8', '-', '2', '8'), '+50']
    assert parse_input('+25d8') == [('+25d8', '+', '25', '8')]
    assert parse_input('25d8') == [('+25d8', '+', '25', '8')]

# actual = parse_input('25d8')
# assert isinstance(actual[0][3], str)
def test_convert_to_rolls_output():
    rolls = parse_input('-100d10 + 5d8 -23 +8')
    actual_raw = convert_to_rolls(rolls)
    actual = []
    for item in actual_raw:
        delattr(item, 'all_rolls')
        delattr(item, 'total')
        # item = item.__dict__
        # del item['all_rolls']
        actual.append(item.__dict__)
    expected = [{'dice_roll': '-100d10', 'multiplier': -1, 'modifier': 0, 'dice_count': 100, 'dice_type': 10}, {'dice_roll': '+5d8', 'multiplier': 1, 'modifier': 0, 'dice_count': 5, 'dice_type': 8}, {'dice_roll': '-23', 'multiplier': -1, 'modifier': 23, 'dice_count': 0, 'dice_type': 0}, {'dice_roll': '+8', 'multiplier': 1, 'modifier': 8, 'dice_count': 0, 'dice_type': 0}]
    assert actual == expected 
    # check total is int
    # check all_rolls





