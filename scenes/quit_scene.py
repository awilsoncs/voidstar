from engine import GameScene


class QuitScene(GameScene):
    """Exit the game."""

    def __init__(self):
        super().__init__()

    def update(self):
        self.controller.pop_scene()
        self.controller.pop_scene()
