from components.actors.actor import Actor


def run(scene) -> None:
    for actor in get_actors(scene):
        actor.act(scene)


def get_actors(scene):
    return [actor for actor in scene.cm.get(Actor) if actor.can_act()]
