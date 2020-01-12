from components import Entity
from engine import GameScene, core
from procgen.galaxy_names import get_file_name
from procgen.zonebuilders import fields
from scenes.simulation_scene import SimulationScene


class NewGameScene(GameScene):
    """Generate a player and a world model."""
    def __init__(self, debug=False):
        super().__init__(debug=debug)

    def update(self):
        """Start a new game."""
        self.cm.connect(get_file_name())
        zone_id = core.get_id()
        fields.build(self.cm, zone_id)

        zone = self.cm.get_one(Entity, entity=0).zone
        self.cm.thaw(zone)
        self.controller.pop_scene()
        self.controller.push_scene(SimulationScene(zone_id, debug=self.debug))
