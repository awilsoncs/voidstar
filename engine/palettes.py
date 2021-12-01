from engine.colors import from_hex

# Shamelessly stolen: https://lospec.com/palette-list/fantasy-24
BACKGROUND = (0, 0, 0)
GRASS = (57, 87, 28)
FOILAGE_B = (31, 36, 10)
FOILAGE_C = (165, 140, 39)
GOLD = (239, 172, 40)
WHITE = (239, 216, 161)
GABRIEL_2_1 = (171, 92, 28)
GABRIEL_2_2 = (24, 63, 57)
GABRIEL_2_3 = (239, 105, 47)
STRAW = (239, 183, 117)
GABRIEL_2_5 = (165, 98, 67)
GABRIEL_3_1 = (119, 52, 33)
GABRIEL_3_2 = (114, 65, 19)
GABRIEL_3_3 = (42, 29, 13)
GABRIEL_3_4 = (57, 42, 28)
GABRIEL_3_5 = (104, 76, 60)
STONE = (146, 126, 106)
WATER = (39, 100, 104)
# (239, 58, 12),
# (69, 35, 13),
LIGHT_WATER = (60, 159, 156)
HORDELING = (155, 26, 10)
# (54, 23, 12),
BLOOD = (85, 15, 10)
# (48, 15, 10)


if __name__ == '__main__':
    for color in [
        '1f240a',
        '39571c',
        'a58c27',
        'efac28',
        'efd8a1',
        'ab5c1c',
        '183f39',
        'ef692f',
        'efb775',
        'a56243',
        '773421',
        '724113',
        '2a1d0d',
        '392a1c',
        '684c3c',
        '927e6a',
        '276468',
        'ef3a0c',
        '45230d',
        '3c9f9c',
        '9b1a0a',
        '36170c',
        '550f0a',
        '300f0a',
    ]:
        print(from_hex('#' + color))
