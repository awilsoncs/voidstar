from dataclasses import dataclass

from components.events.peasant_events import PeasantDiedListener, PeasantAddedListener


@dataclass
class Population(PeasantAddedListener, PeasantDiedListener):
    population: int = 0

    def on_peasant_added(self, scene):
        self._log_info("population increased")
        self.population += 1

    def on_peasant_died(self, scene):
        self._log_info("population decreased")
        self.population -= 1
        if self.population <= 0:
            scene.popup_message("All of the peasants were killed! The king will have your head for this. Game Over.")
            scene.pop()