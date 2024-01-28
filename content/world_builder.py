from components.events.build_world_events import BuildWorld
from components.events.start_game_events import StartGame
from components.world_building.add_player_step import AddPlayerStep
from components.world_building.delete_world_builder import DeleteWorldBuilder
from components.world_building.place_copses import PlaceTrees
from components.world_building.place_flowers import PlaceFlowers
from components.world_building.place_lakes import PlaceLakes
from components.world_building.place_river import PlaceRiver
from components.world_building.place_roads import PlaceRoads
from components.world_building.place_rocks import PlaceRocks
from components.world_building.set_world_name import SetWorldName
from engine import core
from engine.components.entity import Entity


def make_world_build():
    entity_id = core.get_id()
    return (
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name="Worldbuilder"),
            BuildWorld(entity=entity_id),
            AddPlayerStep(entity=entity_id),
            PlaceLakes(entity=entity_id),
            # PlaceRiver(entity=entity_id),
            # PlaceRoads(entity=entity_id),
            PlaceTrees(entity=entity_id),
            PlaceRocks(entity=entity_id),
            PlaceFlowers(entity=entity_id),
            SetWorldName(entity=entity_id),
            DeleteWorldBuilder(entity=entity_id),
            StartGame(entity=entity_id)
        ]
    )
