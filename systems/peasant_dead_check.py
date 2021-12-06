from components.tags.peasant_tag import PeasantTag


def run(scene):
    faction_members = scene.cm.get(PeasantTag)
    if not faction_members:
        scene.popup_message("All of the peasants were killed! The king will have your head for this. Game Over.")
        scene.pop()
        return
