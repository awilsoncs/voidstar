from engine.types import ComponentType


def of_type(t: ComponentType, scene):
    scene.cm.delete_components(t)
