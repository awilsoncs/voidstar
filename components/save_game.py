import dataclasses
import json
import logging
from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from engine import palettes


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            data = dataclasses.asdict(o)
            data["class"] = str(type(o))
            return data
        return super().default(o)


@dataclass
class SaveGame(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    def act(self, scene) -> None:
        logging.info(f"EID#{self.entity}::SaveGame attempting to save game")
        game_state = json.dumps(scene.cm.components_by_id, cls=EnhancedJSONEncoder)
        with open('./game_save.json', 'w+') as f:
            f.write(game_state)
        logging.info(f"EID#{self.entity}::SaveGame save complete")
        scene.message("Game saved.", color=palettes.LIGHT_WATER)
        scene.cm.delete_component(self)

