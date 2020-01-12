from components import Senses
from components.coordinates import Coordinates


def run(scene):
    for senses in [s for s in scene.cm.get(Senses) if s.dirty]:
        coords = scene.cm.get_one(Coordinates, senses.entity)
        if senses.entity == 0 and coords:
            scene.map.compute_fov(coords.x, coords.y)
            scene.memory_map[scene.map.fov] = True
            senses.dirty = False
