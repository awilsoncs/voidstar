from engine.components.energy_actor import EnergyActor

intro = "You have been tasked with protecting this village from the hordelings. "

class ShowHelpDialogue(EnergyActor):
    def act(self, scene) -> None:
        scene.popup_message(intro)
        scene.cm.delete_component(self)
