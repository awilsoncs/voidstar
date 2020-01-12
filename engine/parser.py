"""
Define loading dictionary-specified abstract entities into component objects.
"""
import os

import yaml

import settings
from components.component import get_table_name_to_class_mapping
from engine import core, colors


def get_entities_from_yaml(directory=None):
    """Load a multi-document yaml file into a list of entities in dict form."""
    y = dict()
    directory = directory or settings.DATA_DIR
    for dir_path, dir_names, file_names in os.walk(directory):
        for file_name in [f for f in file_names if f.endswith('.yml')]:
            file_to_load = os.path.join(dir_path, file_name)
            with open(file_to_load, 'r') as f:
                yamls_from_file = yaml.load_all(f)
                for yaml_from_file in yamls_from_file:
                    y.update(yaml_from_file)
    resolve_type_dependencies(y)
    resolve_macros(y)
    return get_components_from_multiblob(y)


def resolve_macros(blob):
    for key in blob:
        resolve_macros_for_key(blob, key)


def resolve_macros_for_key(blob, key):
    """Resolve all $macros within a given entity blob."""
    blob_to_resolve = blob[key]
    for component_key, data in blob_to_resolve.items():
        if isinstance(data, list):
            for i, item in enumerate(data):
                if item.startswith('$'):
                    data[i] = blob[item.replace('$')]
        elif isinstance(data, str) and data.startswith('$'):
            blob_to_resolve[component_key] = blob[data.replace('$', '')]


def resolve_type_dependencies(blob):
    """Resolve all type inheritance info in the given blob."""
    for key in blob:
        resolve_type_dependency_for_key(blob, key)


def resolve_type_dependency_for_key(blob, key):
    """Given a game data blob and a key, resolve any type inheritance info."""
    if 'type' in blob[key]:
        type_key = blob[key]['type']
        new_blob = {}
        resolve_type_dependency_for_key(blob, type_key)
        new_blob.update(blob[type_key])
        new_blob.update(blob[key])
        blob[key] = new_blob
        del blob[key]['type']


def get_components_from_multiblob(entity_blobs: dict):
    """Transform entity blobs into a list of components."""
    output = []
    for _, blob in entity_blobs.items():
        if 'entity' in blob:
            new_entity = get_components_from_blob(core.get_id(), blob)
            output.append(new_entity)
    return output


def get_components_from_blob(entity_id: int, blob: dict):
    output = []
    for table_name, data in blob.items():
        if isinstance(data, list):
            for component_blob in data:
                component = build_component(table_name, entity_id, component_blob)
                output.append(component)
        else:
            component = build_component(table_name, entity_id, data)
            output.append(component)
    return output


def build_component(table_name, entity_id, data):
    table_class_map = get_table_name_to_class_mapping()

    component = table_class_map[table_name](entity=entity_id, **data)
    if table_name == 'entity':
        component.abstract = True
    # these items aren't written in their explicit form
    if 'color' in component.__dict__:
        component.color = colors.get_color_from_text(component.color)
    if 'bg_color' in component.__dict__:
        component.bg_color = colors.get_color_from_text(component.bg_color)
    return component
