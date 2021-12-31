from components.game_start_listeners.game_start_listener import GameStartListener


class AnnounceGameStart(GameStartListener):

    def on_game_start(self, scene):
        scene.message("You have been tasked with protecting the peasants of the Toshim Plains.")
        scene.message("At the end of each season, the horde will come, ravenous in hunger.")
        scene.message("Press the 'h' key if you need help.")
        scene.cm.delete_component(self)
