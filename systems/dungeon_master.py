from components.tags import Tag


def run(scene):
    faction_members = scene.cm.get(Tag)
    if not any(f for f in faction_members if f.value == 'peasant'):
        scene.popup_message("All of the peasants were killed! You lose.")
        scene.pop()

    if not any(f for f in faction_members if f.value == 'hordeling'):
        scene.popup_message("You stopped the hordeling invasion! But more come...")
        scene.next_level()
