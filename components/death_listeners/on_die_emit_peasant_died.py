from dataclasses import dataclass

from components.events.die_events import DeathListener
from components.events.peasant_events import PeasantDied
from engine import core


@dataclass
class OnDieEmitPeasantDied(DeathListener):
    """Translate a peasant death into a population count decrement."""
    def on_die(self, scene):
        scene.cm.add(PeasantDied(entity=core.get_id("world")))
