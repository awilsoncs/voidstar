import os
from collections import namedtuple

from components import Entity, Appearance
from engine import colors
from engine.parser import build_component, get_components_from_blob, get_entities_from_yaml

TestCase = namedtuple(
    'TestCase',
    [
        'input',
        'output'
    ]
)

COMPONENT_TEST_CASES = [
    TestCase({'entity': {'name': 'orc'}}, Entity(entity=0, name='orc', abstract=True)),
    TestCase(
        {'appearance': {'symbol': 'o', 'color': 'light green', 'bg_color': 'light blue'}},
        Appearance(entity=52, symbol='o', color=colors.light_green, bg_color=colors.light_blue)
    )
]


def test_build_component():
    for i, o in COMPONENT_TEST_CASES:
        table_name, data = i.popitem()
        component = build_component(table_name, o.entity, data)
        assert component == component


ENTITY_FROM_BLOB_CASES = [
    TestCase(
        {
            'entity': {'name': 'orc'},
            'appearance': {'symbol': 'o', 'color': 'light green', 'bg_color': 'light blue'}
        },
        [
            Entity(entity=0, name='orc', abstract=True),
            Appearance(entity=0, symbol='o', color=colors.light_green, bg_color=colors.light_blue)
        ]
    )
]


def test_get_entity_from_blob():
    for test_case in ENTITY_FROM_BLOB_CASES:
        entity = get_components_from_blob(0, test_case.input)
        for component in entity:
            assert component in test_case.output
        for component in test_case.output:
            assert component in entity


def test_entity_inheritance():
    entities = get_entities_from_yaml(os.path.join('.', 'engine', 'tests', 'test_data'))
    assert len(entities) == 1
