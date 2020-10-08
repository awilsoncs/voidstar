import argparse
import cProfile
import logging

from engine.game_scene_controller import GameSceneController
from scenes.start_menu import get_start_menu


def main():
    game = GameSceneController('Oh No! It\'s THE HORDE!')
    game.push_scene(get_start_menu())
    game.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Oh No! It\'s THE HORDE!')
    parser.add_argument('--prof', action='store_true', help='profile the game')
    parser.add_argument('--debug', action='store_true', help='allow a crash when an exception is thrown')
    parser.add_argument('-l', '--log', choices=['INFO', 'WARNING', 'CRITICAL', 'ERROR', 'DEBUG'], default='INFO')
    args = parser.parse_args()

    logging.basicConfig()
    logging.getLogger().setLevel(args.log)

    if args.prof:
        pr = cProfile.Profile()
        pr.enable()
        main()
        pr.disable()
        pr.dump_stats('prof.txt')
    else:
        main()
