from dataclasses import dataclass

from components.component import Component


@dataclass
class AnimationPath(Component):
    current_step: int = 0
    delay_ms: int = 0  # how long to wait between steps
    next_update_time: int = 0
    delete_on_complete: bool = True  # whether to delete the entity when the path is done
