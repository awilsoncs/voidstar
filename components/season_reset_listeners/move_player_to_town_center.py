import logging

from components import Coordinates
from components.attack_start_listeners.attack_start_actor import AttackStartListener
from components.game_start_listeners.game_start_listener import GameStartListener
from components.tags.town_center_flag import TownCenterFlag


class MovePlayerToTownCenter(GameStartListener, AttackStartListener):
    def on_game_start(self, scene):
        self.move_player(scene)

    def on_season_reset(self, scene):
        self.move_player(scene)

    def on_attack_start(self, scene):
        self.move_player(scene)

    def move_player(self, scene):
        logging.info(f"EID#{self.entity}::MovePlayerToTownCenter moving player to town center")
        flag = scene.cm.get(TownCenterFlag)[0]
        coord = scene.cm.get_one(Coordinates, entity=flag.entity)
        player = scene.cm.get_one(Coordinates, entity=scene.player)
        player.x = coord.x
        player.y = coord.y
