from dataclasses import dataclass

from components import Coordinates
from components.actors.calendar_actor import Calendar
from components.season_reset_listeners.seasonal_actor import SeasonResetListener
from content.farmsteads.houses import place_farmstead
from content.terrain.roads import connect_point_to_road_network


@dataclass
class AddFarmstead(SeasonResetListener):
    def on_season_reset(self, scene):
        calendar = scene.cm.get_one(Calendar, entity=self.entity)
        if calendar.season == 1:
            farmstead_id = place_farmstead(scene)
            farmstead_center = scene.cm.get_one(Coordinates, entity=farmstead_id).position
            connect_point_to_road_network(scene, farmstead_center)