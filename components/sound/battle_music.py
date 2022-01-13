from components.events.attack_started_events import AttackStartListener


class BattleMusic(AttackStartListener):
    def on_attack_start(self, scene):
        scene.sound.play('battle')
