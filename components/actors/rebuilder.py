from dataclasses import dataclass

from components.actors.seasonal_actor import SeasonalActor
from components.owner import Owner


@dataclass
class Rebuilder(SeasonalActor):
    """Rebuilds broken down house walls."""
    def act(self, scene):
        parent_link = scene.cm.get_one(Owner, entity=self.entity)
        if not parent_link:
            raise NotImplementedError("cannot yet handle rebuilder without parent entity")