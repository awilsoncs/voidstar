from components import Attributes
from components.death_listeners.die import Die


def run(scene):
    """Invoke death effects for all creatures with 0 or fewer hps."""
    healths = [f for f in scene.cm.get(Attributes) if (f.hp <= 0)]
    for health in healths:
        scene.cm.add(Die(entity=health.entity))
