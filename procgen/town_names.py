import tracery

rules = {
    'origin': '0#first##second#',
    'first': [
        'Spur',
        'Churl',
        'Whim',
        'Gale',
        'River',
        'Ton',
        'Gil'
    ],
    'second': [
        'burg',
        'ham',
        'ton',
        'hill'
    ]
}


def get_file_name():
    name = get_name()
    return name.replace(' ', '-')


def get_name():
    grammar = tracery.Grammar(rules)
    return grammar.flatten("#origin#")
