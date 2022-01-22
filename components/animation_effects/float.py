import random
from dataclasses import dataclass

import settings
from components import Coordinates
from components.base_components.timed_actor import TimedActor


@dataclass
class AnimationFloat(TimedActor):
    """Randomly float up or right."""
    duration: int = 10
    timer_delay: int = 125
    delete_on_complete: bool = True  # whether to delete the entity when the path is done

    def update_animation(self, scene):
        entity = self.entity
        coords = scene.cm.get_one(Coordinates, entity=entity)
        up_or_over = random.choice([(0, -1), (1, 0)])
        coords.x += up_or_over[0]
        coords.y += up_or_over[1]

        if coords.x >= settings.MAP_WIDTH or coords.y <= 0:
            scene.cm.delete(entity)

    def act(self, scene):
        self.update_animation(scene)
        self.duration -= 1
        if self.duration < 0:
            scene.cm.delete(self.entity)
        else:
            self.pass_turn()
