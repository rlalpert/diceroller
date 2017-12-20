from diceroller import parse_input

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