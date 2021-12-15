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


def is_visible(scene, entity: int):
    coords = scene.cm.get_one(Coordinates, entity=entity)
    return coords and scene.visibility_map[coords.x, coords.y]
