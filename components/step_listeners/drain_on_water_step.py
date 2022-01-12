import logging

from components import Coordinates
from components.actions.attack_action import AttackAction
from components.step_listeners.on_step_listener import StepListener
from components.tags.water_tag import WaterTag


class DrainOnStepOnWater(StepListener):
    """Whenever the owning entity takes a step into a gold containing square, pick it up."""

    def on_step(self, scene, point):
        logging.debug(f"EID#{self.entity}::DrainOnStepOnWater checking for water at new location")
        for event in scene.cm.get(WaterTag):
            water_coords = scene.cm.get_one(Coordinates, entity=event.entity)
            if water_coords.is_at_point(point):
                scene.cm.add(AttackAction(entity=event.entity, target=self.entity, damage=1))
