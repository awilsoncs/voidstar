from components.actors.energy_actor import EnergyActor


def run(scene):
    player_actor = scene.cm.get_one(EnergyActor, entity=scene.player)
    if player_actor.energy >= 0:
        return
    else:
        actors = scene.cm.get(EnergyActor)
        for actor in actors:
            if actor.is_recharging:
                actor.energy += 1
