from dataclasses import dataclass

from engine.base_components.energy_actor import EnergyActor
from components.events.die_events import Die
from components.stomach import Stomach
from components.tags.peasant_tag import PeasantTag
from engine import constants
from engine.base_components.entity import Entity


@dataclass
class EatAction(EnergyActor):
    """Instance of a live attack."""
    target: int = constants.INVALID

    def act(self, scene) -> None:
        self._log_debug(f"attempting to eat {self.target}")
        this_entity = scene.cm.get_one(Entity, entity=self.entity)
        target_entity = scene.cm.get_one(Entity, entity=self.target)
        if not target_entity:
            self._log_debug(f"attempted to eat {self.target} but it was gone!")
            return
        scene.warn(f"{this_entity.name} ate a {target_entity.name}!")
        if scene.cm.get_one(PeasantTag, entity=self.target):
            scene.cm.stash_entity(self.target)
            stomach = scene.cm.get_one(Stomach, entity=self.entity)
            stomach.contents = self.target
        else:
            scene.cm.add(Die(entity=self.target, killer=self.entity))

        scene.cm.delete_component(self)
