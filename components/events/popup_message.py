from dataclasses import dataclass

from components.base_components.timed_actor import TimedActor


@dataclass
class PopupMessage(TimedActor):
    timer_delay: int = TimedActor.REAL_TIME
    message: str = ""

    def act(self, scene):
        if self.next_update:
            scene.popup_message(self.message)
            scene.cm.delete_component(self)
