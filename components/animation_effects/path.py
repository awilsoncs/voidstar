from dataclasses import dataclass

from components import Coordinates
from components.path_node import PathNode
from engine.base_components.timed_actor import TimedActor


@dataclass
class AnimationPath(TimedActor):
    current_step: int = 0
    timer_delay: int = 30
    delete_on_complete: bool = True  # whether to delete the entity when the path is done

    def act(self, scene):
        self.update_animation_path(scene)
        self.pass_turn()

    def update_animation_path(self, scene):
        entity = self.entity
        path_nodes = scene.cm.get_all(PathNode, entity=entity)
        try:
            next_node = next(p for p in path_nodes if p.step == self.current_step)
            coords = scene.cm.get_one(Coordinates, entity=entity)

            coords.x = next_node.x
            coords.y = next_node.y

            self.current_step += 1
        except StopIteration:
            scene.cm.delete(entity)
