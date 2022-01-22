import dataclasses
import json
import logging
from importlib import import_module
from inspect import isclass
from pathlib import Path
from pkgutil import walk_packages

from engine import core
from components.base_components.component import Component


class EnhancedJSONEncoder(json.JSONEncoder):
    """Provide a dataclass encoder."""
    def default(self, o):
        if dataclasses.is_dataclass(o):
            data = dataclasses.asdict(o)
            data["class"] = o.__class__.__name__
            return data
        return super().default(o)


def save(components, file, extra=None):
    if extra is None:
        extra = {}
    save_info = {
        "info": {
            "object_count": len(components["active_components"]),
            "extra": extra
        },
        "named_ids": core.get_named_ids(),
        "objects": components
    }

    save_data = json.dumps(save_info, cls=EnhancedJSONEncoder)
    with open(file, 'w+') as f:
        f.write(save_data)


def load(file):
    # iterate through the modules in the current package
    loadable_classes = _gather_loadable_classes()

    with open(file, 'r') as f:
        data = json.load(f)

    core.set_named_ids(data["named_ids"])

    active_components = _load_from_data(data["objects"]["active_components"], loadable_classes)
    expected_count = data["info"]["object_count"]
    real_count = len(active_components)
    if real_count != expected_count:
        logging.warning(f"Mismatched objects on load expected {expected_count}, found {real_count}")

    stashed_components = _load_from_data(data["objects"]["stashed_components"], loadable_classes)

    loaded_data = {
        "active_components": active_components,
        "stashed_components": stashed_components,
        "stashed_entities": data["objects"]["stashed_entities"]
    }
    return loaded_data


def _load_from_data(data, loadable_classes):
    """Load a set of data from loadable classes."""
    active_components = {}
    for key, obj in data.items():
        obj_class = obj["class"]
        if obj_class not in loadable_classes:
            raise ValueError(f"class not found: {obj_class}")
        else:
            del obj["class"]
            clz = loadable_classes[obj_class]
            active_components[key] = clz(**obj)
    return active_components


def _gather_loadable_classes():
    """Read the base_components directory to discover loadable base_components."""
    loadable_classes = {}

    # ignore this mess
    package_dir = Path(__file__).resolve().parent.parent.parent
    for (_, module_name, _) in walk_packages([package_dir]):

        # import the module and iterate through its attributes
        module = import_module(f"{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)

            if isclass(attribute) and issubclass(attribute, Component):
                # Add the class to this package's variables
                loadable_classes[attribute_name] = attribute
    return loadable_classes
