from components import Brain


def run(scene):
    brains = scene.cm.get(Brain)
    # if we don't have any brains that need to take turns,
    if all(not b.take_turn for b in brains):
        reset_turns(brains)


def reset_turns(brains):
    for brain in brains:
        brain.take_turn = True
