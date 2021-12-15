from components.game_start_listeners.game_start_listener import GameStartListener


class AnnounceGameStart(GameStartListener):

    def on_game_start(self, scene):
        scene.popup_message("You have been tasked with protecting the peasants of the Toshim Plains.")
        scene.popup_message("At the end of each season, the horde will come, ravenous in hunger.")
        scene.cm.delete_component(self)
