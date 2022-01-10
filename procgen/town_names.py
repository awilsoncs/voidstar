import tracery

rules = {
    'origin': '#first##second#',
    'first': [
        'Spur',
        'Churl',
        'Whim',
        'Gale',
        'River',
        'Ton',
        'Gil',
        'Hel',
        'Bur',
        'Turl',
        'Fon',
        'Fil',
        'Til',
        'Shim',
        'To',
        'Cod',
        'Lin'
    ],
    'second': [
        'burg',
        'ham',
        'ton',
        'hill',
        'shim',
        'cod',
        'ling',
        'mont',
        'bog'
    ]
}


def get_file_name():
    name = get_name()
    return name.replace(' ', '-')


def get_name():
    grammar = tracery.Grammar(rules)
    return grammar.flatten("#origin#")
