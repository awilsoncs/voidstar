from engine.components.energy_actor import EnergyActor

intro = "You have been tasked with protecting this village from the hordelings. " \
        "As you move around, the calendar will progress through the month. " \
        "On the 30th day, the horde will attack."

controls = "Move around with the arrow keys. Switch through your abilities with 'q' and 'e'. Use an ability with Space."

money = "Peasants, crops, and other items will grant you income. " \
        "Some abilities will cost gold coins to activate. A few will cost gold to maintain each season." \
        "At the end of each year, the king will expect a certain amount of taxes, so set some money aside."

money_pt2 = "By the way, you can use your 'Sell Things' ability to sell Trees to get some initial income."

attacks = "There are many kinds of hordelings, and the strength of the attacks will increase with time. " \
          "You should build defenses and hire warriors to help fight against their onslaught."


class ShowHelpDialogue(EnergyActor):
    def act(self, scene) -> None:
        scene.popup_message(intro)
        scene.popup_message(controls)
        scene.popup_message(money)
        scene.popup_message(money_pt2)
        scene.popup_message(attacks)
        scene.cm.delete_component(self)
