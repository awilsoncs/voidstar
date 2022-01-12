import logging
from dataclasses import dataclass

from components.actors.actor import Actor
from components.delete_listeners.delete_listener import DeleteListener
from components.relationships.owner import Owner


@dataclass
class ResetOwnerAnimation(DeleteListener):
    def on_delete(self, scene):
        owner = scene.cm.get_one(Owner, entity=self.entity)

        # todo unhardcode this
        peasant = scene.cm.get_one(Actor, entity=owner.owner)
        self._log_debug(f"triggered, owner={owner.owner}")

        peasant.can_animate = True
