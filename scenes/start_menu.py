from collections import OrderedDict

from procgen.zonebuilders.debug_field import DebugFieldBuilder
from procgen.zonebuilders.fields import FieldBuilder


def get_start_menu():
    from scenes.defend_scene import DefendScene
    from scenes.navigation_menu_scene import NavigationMenuScene
    from scenes.quit_scene import QuitScene

    option_map = OrderedDict()
    option_map['New Game'] = DefendScene(zonebuilder=FieldBuilder(peasants=3))
    option_map['Debug Field'] = DefendScene(zonebuilder=DebugFieldBuilder(peasants=1))
    option_map['Quit'] = QuitScene()
    return NavigationMenuScene(
        title="Oh No! It's THE HORDE!",
        option_scene_map=option_map,
    )
