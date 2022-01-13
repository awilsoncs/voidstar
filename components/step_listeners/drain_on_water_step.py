from components import Coordinates
from components.actions.attack_action import AttackAction
from components.events.step_event import StepListener
from components.tags.water_tag import WaterTag


class DrainOnStepOnWater(StepListener):
    """Whenever the owning entity takes a step into a gold containing square, pick it up."""

    def on_step(self, scene, point):
        self._log_debug(f"checking for water at new location")
        for event in scene.cm.get(WaterTag):
            water_coords = scene.cm.get_one(Coordinates, entity=event.entity)
            if water_coords.is_at_point(point):
                scene.cm.add(AttackAction(entity=event.entity, target=self.entity, damage=1))
