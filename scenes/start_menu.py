from collections import OrderedDict



def get_start_menu():
    from scenes.defend_scene import DefendScene
    from scenes.navigation_menu_scene import NavigationMenuScene
    from scenes.quit_scene import QuitScene

    option_map = OrderedDict()
    option_map['New Game'] = DefendScene()
    # option_map['Debug Field'] = DefendScene()
    option_map['Quit'] = QuitScene()
    return NavigationMenuScene(
        title="Oh No! It's THE HORDE!",
        option_scene_map=option_map,
    )
