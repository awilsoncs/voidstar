from components.build_world_listeners.add_player_step import AddPlayerStep
from components.build_world_listeners.build_world import BuildWorld
from components.build_world_listeners.delete_world_builder import DeleteWorldBuilder
from components.build_world_listeners.place_lakes import PlaceLakes
from components.build_world_listeners.place_map_boundary import PlaceMapBoundary
from components.build_world_listeners.place_peasants import PlacePeasants
from components.build_world_listeners.place_copses import PlaceTrees
from engine import core


def make_world_build():
    entity_id = core.get_id()
    return (
        entity_id,
        [
            BuildWorld(entity=entity_id),
            AddPlayerStep(entity=entity_id),
            PlaceMapBoundary(entity=entity_id),
            PlaceLakes(entity=entity_id),
            PlacePeasants(entity=entity_id),
            PlaceTrees(entity=entity_id),
            DeleteWorldBuilder(entity=entity_id)
        ]
    )
