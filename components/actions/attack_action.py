from dataclasses import dataclass

from components.component import Component


@dataclass
class AttackAction(Component):
    """Object to signal that the owner entity is attacking the recipient."""
    recipient: int = None
    damage: int = 0
