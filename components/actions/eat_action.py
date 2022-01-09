from dataclasses import dataclass

from components import Entity
from components.actors.energy_actor import EnergyActor
from components.death_listeners.die import Die
from engine import constants


@dataclass
class EatAction(EnergyActor):
    """Instance of a live attack."""
    target: int = constants.INVALID

    def act(self, scene) -> None:
        this_entity = scene.cm.get_one(Entity, entity=self.entity)
        target_entity = scene.cm.get_one(Entity, entity=self.target)

        scene.warn(f"{this_entity.name} ate {target_entity.name}!")
        scene.cm.add(Die(entity=self.target, killer=self.entity))


