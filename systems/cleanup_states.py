from components.events.chargeabilityevent import ChargeAbilityEvent
from components.states.dizzy_state import DizzyState


def run(scene):
    deletables = [s for s in scene.cm.get(DizzyState) if s.duration < 1]
    for state in deletables:
        scene.cm.delete_component(state)

    for state in scene.cm.get(DizzyState):
        if scene.cm.get_one(ChargeAbilityEvent, entity=state.entity):
            state.duration -= 1