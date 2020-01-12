import math


def distance(x1, y1, x2, y2):
    return math.sqrt(distance_squared(x1, y1, x2, y2))


def distance_squared(x1, y1, x2, y2):
    """Return the distance between two points, squared."""
    return (x1 - x2) ** 2 + (y1 - y2) ** 2