import tracery

rules = {
    'origin': 'the #adj# #noun#',
    'adj': [
        'dark',
        'light',
        'brilliant',
        'mystical',
        'glowing',
        'heavenly',
        'gilded'
    ],
    'noun': [
        'waves',
        'aether',
        'nebulae',
        'void',
        'stars',
        'realms'
    ]
}

def get_file_name():
    name = get_name()
    return name.replace(' ', '-')

def get_name():
    grammar = tracery.Grammar(rules)
    return grammar.flatten("#origin#")