from components import Coordinates
from components.pickup_gold import PickupGold
from engine import PLAYER_ID
from engine.core import log_debug


def run(scene):
    for event in scene.cm.get(PickupGold):
        pickup_gold(scene, event)


@log_debug(__name__)
def pickup_gold(scene, event):
    # if the player is standing on this the gold nugget, delete the gold nugget and add 10 to their gold.
    coords = scene.cm.get_one(Coordinates, entity=event.entity)
    player_coords = scene.cm.get_one(Coordinates, entity=PLAYER_ID)

    if (
        coords.x == player_coords.x
        and coords.y == player_coords.y
    ):
        scene.cm.delete(event.entity)
        scene.gold += 10
