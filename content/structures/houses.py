from components.house_structure import HouseStructure
from content.allies import make_peasant
from content.structures.floorboard import make_floorboard
from content.structures.walls import make_wall
from engine import core


def make_house(root_id, resident, x, y):
    floorboard = make_floorboard(root_id, x, y, resident)

    upper_left = make_wall(root_id, x - 1, y - 1)
    upper_middle = make_wall(root_id, x, y - 1)
    upper_right = make_wall(root_id, x + 1, y - 1)
    middle_left = make_wall(root_id, x - 1, y)
    middle_right = make_wall(root_id, x + 1, y)
    bottom_left = make_wall(root_id, x - 1, y + 1)
    bottom_middle = make_wall(root_id, x, y + 1)
    bottom_right = make_wall(root_id, x + 1, y + 1)

    structure = HouseStructure(
        entity=root_id,
        house_id=root_id,
        upper_left=upper_left[0],
        upper_middle=upper_middle[0],
        upper_right=upper_right[0],
        middle_left=middle_left[0],
        middle_right=middle_right[0],
        bottom_left=bottom_left[0],
        bottom_middle=bottom_middle[0],
        bottom_right=bottom_right[0]
    )

    floorboard[1].append(structure)

    return [
        upper_left, upper_middle, upper_right,
        middle_left, floorboard, middle_right,
        bottom_left, bottom_middle, bottom_right
    ]


def make_peasant_home(x, y):
    house_id = core.get_id()
    peasant = make_peasant(house_id, x, y)
    return make_house(house_id, peasant[0], x, y) + [peasant]
