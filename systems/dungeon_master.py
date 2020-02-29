from components.faction import Faction


def run(scene):
    faction_members = scene.cm.get(Faction)
    if not any(f for f in faction_members if f.faction is Faction.Options.PEASANT):
        scene.popup_message("All of the peasants were killed! You lose.")
        scene.pop()

    if not any(f for f in faction_members if f.faction is Faction.Options.MONSTER):
        scene.popup_message("You stopped the hordeling invasion! But more come...")
        scene.next_level()
