from uuid import uuid4

import tcod.event
import tcod.noise


def get_key_event():
    """Handle tcod key events."""
    for event in tcod.event.get():
        if event.type == "KEYDOWN":
            return event


def wait_for_char():
    while True:
        for e in tcod.event.wait():
            if e.type == 'KEYDOWN':
                return e


def get_noise_generator(dimensions=3):
    return tcod.noise.Noise(dimensions=dimensions, octaves=32)


def get_id():
    return uuid4().int >> 65
