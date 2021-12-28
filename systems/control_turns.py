from components.actors.energy_actor import EnergyActor
from components.brains.brain import Brain


def run(scene):
    player_actor = scene.cm.get_one(Brain, entity=scene.player)
    if player_actor and player_actor.energy >= 0:
        return
    else:
        actors = scene.cm.get(EnergyActor)
        for actor in actors:
            if actor.is_recharging:
                actor.energy += 1
