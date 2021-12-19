import math
from itertools import product

from components import Coordinates


def clamp(number: int, min: int, max: int):
    assert min <= max, "clamp range cannot be zero"
    if number < min:
        return min
    elif number > max:
        return max
    else:
        return number


def distance(x1, y1, x2, y2):
    return math.sqrt(distance_squared(x1, y1, x2, y2))


def distance_squared(x1, y1, x2, y2):
    """Return the distance between two points, squared."""
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def get_3_by_3_square(x, y):
    return {
        (x+dx, y+dy) for dx, dy in product([-1, 0, 1], [-1, 0, 1])
    }


def get_3_by_3_box(x, y):
    square = get_3_by_3_square(x, y)
    square.remove((x, y))
    return square


def get_box(start_loc, end_loc):
    """Get a box defined by the top left and bottom right points."""
    tiles = set()
    start_x, start_y = start_loc
    end_x, end_y = end_loc

    for x in range(start_x, end_x+1):
        tiles.add((x, start_y))
        tiles.add((x, end_y))

    # for y in range(start_y, end_y+1):
    #     tiles.add((start_x, y))
    #     tiles.add((end_x, y))

    return tiles


def is_visible(scene, entity: int):
    coords = scene.cm.get_one(Coordinates, entity=entity)
    return coords and scene.visibility_map[coords.x, coords.y]
