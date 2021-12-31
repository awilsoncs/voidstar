from components.attack_start_listeners.attack_start_actor import AttackStartListener


class BattleMusic(AttackStartListener):
    def on_attack_start(self, scene):
        scene.sound.play('battle')
