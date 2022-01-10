import dataclasses
import json
from importlib import import_module
from inspect import isclass
from pathlib import Path
from pkgutil import walk_packages


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            data = dataclasses.asdict(o)
            data["class"] = o.__class__.__name__
            return data
        return super().default(o)


def save(components, file):
    # we don't want this object to get caught in the save game
    save_info = {
        "info": {
            "object_count": len(components)
        },
        "objects": components
    }

    save_data = json.dumps(save_info, cls=EnhancedJSONEncoder)
    with open(file, 'w+') as f:
        f.write(save_data)


def load(file):
    # iterate through the modules in the current package
    package_dir = Path(__file__).resolve().parent.parent.parent
    for (_, module_name, _) in walk_packages([package_dir]):

        # import the module and iterate through its attributes
        module = import_module(f"{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)

            if isclass(attribute):
                # Add the class to this package's variables
                globals()[attribute_name] = attribute

    with open(file, 'r') as f:
        data = json.load(f)

    components = []

    for _, obj in data["objects"].items():
        obj_class = obj["class"]
        if obj_class not in globals():
            raise ValueError(f"save game class not found: {obj_class}")
        else:
            del obj["class"]
            clz = globals()[obj_class]
            components.append(clz(**obj))
    return components


def _try_load_object(object):
    cls = object["class"]
    return object
