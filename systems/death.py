from components import Attributes
from components.appearance import Appearance
from components.brain import Brain
from components.coordinates import Coordinates
from components.enums import ControlMode
from components.faction import Faction
from components.material import Material
from components.target_value import TargetValue
from engine import colors, palettes
from engine.constants import PRIORITY_LOW


def run(scene):
    healths = [f for f in scene.cm.get(Attributes) if (f.hp <= 0)]
    for health in healths:
        entity = health.entity
        scene.cm.delete_component(health)

        brain = scene.cm.get_one(Brain, entity)
        if brain.control_mode is ControlMode.PLAYER:
            brain.control_mode = ControlMode.DEAD_PLAYER
        else:
            scene.cm.delete_component(brain)

        renderable = scene.cm.get_one(Appearance, entity=entity)
        renderable.symbol = '%'
        renderable.color = palettes.BLOOD

        coords = scene.cm.get_one(Coordinates, entity=entity)
        coords.priority = PRIORITY_LOW

        faction = scene.cm.get_one(Faction, entity=entity)
        if faction:
            scene.cm.delete_component(faction)

        material = scene.cm.get_one(Material, entity=entity)
        material.blocks = False
        material.blocks_sight = False

        target_value = scene.cm.get_one(TargetValue, entity=entity)
        if target_value:
            scene.cm.delete_component(target_value)
