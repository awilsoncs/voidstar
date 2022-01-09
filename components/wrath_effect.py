import logging
from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from components.actors.hordeling_spawner import HordelingSpawner
from components.actors.hordeling_spawner import HordelingSpawner
from components.death_listeners.die import Die
from components.tags.hordeling_tag import HordelingTag


@dataclass
class WrathEffect(EnergyActor):
    """Hordelings will spawn at this object's location."""
    energy_cost: int = EnergyActor.INSTANT

    def act(self, scene):
        logging.debug("Wrath triggered")
        logging.debug("Erasing the origin of evil")
        spawners = scene.cm.get(HordelingSpawner)
        for spawner in spawners:
            scene.cm.delete(spawner.entity)

        logging.debug("Obliterating hordelings")
        hordelings = [h.entity for h in scene.cm.get(HordelingTag)]
        for hordeling in hordelings:
            scene.cm.add(Die(entity=hordeling, killer=scene.player))
        scene.cm.delete_component(self)
