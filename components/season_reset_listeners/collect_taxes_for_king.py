from components.season_reset_listeners.seasonal_actor import SeasonResetListener


class CollectTaxesForKing(SeasonResetListener):
    """Collect taxes from the player at the end of the year."""
    value: int = 25

    def on_season_reset(self, scene, season):
        if season != "Spring":
            scene.warn(f'The king will collect {self.value}c from you at the end of the year.')
            return

        if scene.gold < self.value:
            scene.popup_message(
                f"The king attempted to collect {self.value}c, "
                f"but you only had {scene.gold}c! For this, your life is forfeit. Game Over."
            )
            scene.pop()
            return

        scene.gold -= self.value
        old_value = self.value
        self.value += 25
        message = (
            f"The king collected {old_value}c from you at the end of the year. "
            f"Next year, the amount will be {self.value}c."
        )
        scene.popup_message(message)
