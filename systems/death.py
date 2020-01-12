from components import Attributes
from components.appearance import Appearance
from components.brain import Brain
from components.coordinates import Coordinates
from engine import colors
from engine.constants import PRIORITY_LOW


def run(scene):
    dead_fighters = [f for f in scene.cm.get(Attributes) if (f.hp <= 0)]
    for dead_fighter in dead_fighters:
        entity = dead_fighter.entity
        health = scene.cm.get_one(Attributes, entity)
        brain = scene.cm.get_one(Brain, entity)
        scene.cm.delete_component(brain)
        renderable = scene.cm.get_one(Appearance, entity=entity)
        renderable.symbol = '%'
        renderable.color = colors.dark_red
        coords = scene.cm.get_one(Coordinates, entity=entity)
        coords.priority = PRIORITY_LOW
        coords.blocks = False
        coords.blocks_sight = False
        scene.cm.delete_component(health)
