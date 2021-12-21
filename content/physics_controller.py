from components.hole_dug_listeners.flood_nearby_holes import FloodHoles
from engine import core


def make_physics_controller():
    entity_id = core.get_id()

    return (
        entity_id,
        [
            FloodHoles(entity=entity_id)
        ]
    )
