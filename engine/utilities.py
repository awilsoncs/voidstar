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
    tiles = {(start_loc[0], start_loc[1])}
    for x in range(start_loc[0], end_loc[0]):
        tiles.add((x, start_loc[1]))
        tiles.add((x, end_loc[1]))

    for y in range(start_loc[1]+1, end_loc[1]-1):
        tiles.add((start_loc[0], y))
        tiles.add((end_loc[0], y))

    return tiles


def is_visible(scene, entity: int):
    coords = scene.cm.get_one(Coordinates, entity=entity)
    return coords and scene.visibility_map[coords.x, coords.y]
