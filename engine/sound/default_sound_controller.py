import logging

from pygame import mixer

import settings
from engine.sound.sound_controller import SoundController


class DefaultSoundController(SoundController):
    def __init__(self):
        # https://stackoverflow.com/a/20021547
        mixer.init()

    def play(self, track: str):
        if track not in tracks:
            logging.warning(f"DefaultSoundController: missing sound track {track}")
            return
        if not settings.MUSIC_ENABLED:
            logging.debug("DefaultSoundController: Music is disabled in settings.")
            return

        resource = settings.resource_path(tracks[track])

        mixer.music.load(resource)
        mixer.music.play(fade_ms=2000)


tracks = {
    "theme": "./resources/theme.ogg",
    "town": "./resources/town.ogg",
    "battle": "./resources/battle.ogg"
}
