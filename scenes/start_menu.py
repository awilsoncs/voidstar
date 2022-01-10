from collections import OrderedDict


def get_start_menu():
    from scenes.defend_scene import DefendScene
    from scenes.navigation_menu_scene import NavigationMenuScene
    from scenes.quit_scene import QuitScene
    from scenes.load_game_scene import LoadMenuScene

    option_map = OrderedDict()
    option_map['New Game'] = DefendScene()
    option_map['Load Game'] = LoadMenuScene()
    option_map['Quit'] = QuitScene()
    return NavigationMenuScene(
        title="Oh No! It's THE HORDE!",
        option_scene_map=option_map,
    )
