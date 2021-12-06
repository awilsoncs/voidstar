import math
from itertools import product


def distance(x1, y1, x2, y2):
    return math.sqrt(distance_squared(x1, y1, x2, y2))


def distance_squared(x1, y1, x2, y2):
    """Return the distance between two points, squared."""
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def get_3_by_3_square(x, y):
    return {
        (x+dx, y+dy) for dx, dy in product([-1, 0, 1], [-1, 0, 1])
    }