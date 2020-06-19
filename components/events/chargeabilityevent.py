from dataclasses import dataclass

from engine.component import Component


@dataclass
class ChargeAbilityEvent(Component):
    """Indicate that the player took an action."""
    pass
