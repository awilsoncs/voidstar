import argparse
import cProfile
import logging
from collections import OrderedDict

from engine.game_scene_controller import GameSceneController
from scenes.navigation_menu_scene import NavigationMenuScene
from scenes.quit_scene import QuitScene
from scenes.defend_scene import DefendScene


def main(args):
    option_map = OrderedDict()
    option_map['New Game'] = DefendScene(peasants=1, monsters=1)
    option_map['Quit'] = QuitScene()
    start_menu_scene = NavigationMenuScene(
        title='Horde RL',
        option_scene_map=option_map,
    )
    game = GameSceneController("Horde RL")
    game.push_scene(start_menu_scene)
    game.start()


LOG_LEVEL_MAP = {
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'DEBUG': logging.DEBUG
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Horde RL')
    parser.add_argument('--prof', action='store_true', help='profile the game')
    parser.add_argument('--debug', action='store_true', help='allow a crash when an exception is thrown')
    parser.add_argument('-l', '--log', choices=['INFO', 'WARNING', 'CRITICAL', 'ERROR', 'DEBUG'], default='INFO')
    args = parser.parse_args()

    logging.basicConfig()
    logging.getLogger().setLevel(args.log)

    if args.prof:
        pr = cProfile.Profile()
        pr.enable()
        main(args)
        pr.disable()
        pr.dump_stats('prof.txt')
    else:
        main(args)
