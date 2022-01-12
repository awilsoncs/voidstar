import logging

from components import Coordinates
from components.pickup_gold import GoldPickup
from components.step_listeners.on_step_listener import StepListener
from engine import palettes


class PickupGoldOnStep(StepListener):
    """Whenever the owning entity takes a step into a gold containing square, pick it up."""

    def on_step(self, scene, point):
        logging.debug(f"EID#{self.entity}::PickupGoldOnStep checking for gold at new location")
        for event in scene.cm.get(GoldPickup):
            gold_coords = scene.cm.get_one(Coordinates, entity=event.entity)
            if gold_coords.is_at_point(point):
                scene.cm.delete(event.entity)
                scene.gold += event.amount
                scene.message(f'You found {event.amount} gold.', color=palettes.GOLD)
