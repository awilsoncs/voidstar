from components import Coordinates
from components.animation_effects.animation_path import AnimationPath
from components.path_node import PathNode
from engine import core


def update_animation_path(scene, animation_path):
    entity = animation_path.entity
    path_nodes = scene.cm.get_all(PathNode, entity=entity)
    try:
        next_node = next(p for p in path_nodes if p.step == animation_path.current_step)
        coords = scene.cm.get_one(Coordinates, entity=entity)

        coords.x = next_node.x
        coords.y = next_node.y

        animation_path.current_step += 1
    except StopIteration:
        scene.cm.delete(entity)


def run(scene):
    animation_paths = scene.cm.get(AnimationPath)
    for animation_path in animation_paths:
        if core.time_ms() > animation_path.next_update_time:
            update_animation_path(scene, animation_path)
            animation_path.next_update_time = core.time_ms() + animation_path.delay_ms




