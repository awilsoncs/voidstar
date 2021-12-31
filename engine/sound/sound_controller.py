from abc import ABC, abstractmethod


class SoundController(ABC):
    @abstractmethod
    def play(self, track: str):
        pass
