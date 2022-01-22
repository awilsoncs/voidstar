from dataclasses import dataclass

from components.base_components.energy_actor import EnergyActor
from engine import palettes, core, serialization


@dataclass
class LoadGame(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT
    file_name: str = ''

    def act(self, scene) -> None:
        scene.cm.delete_component(self)

        self.load_world(scene)

    def load_world(self, scene):
        start = core.time_ms()
        self._log_info(f"attempting to read game")
        data = serialization.load(self.file_name)
        scene.cm.from_data(data)
        end = core.time_ms()
        self._log_info(f"loaded {len(data)} objects in {end - start}ms")
        scene.message("Game loaded.", color=palettes.LIGHT_WATER)



