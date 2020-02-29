import logging
from time import perf_counter_ns
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


def time_ms():
    return int(perf_counter_ns() / 1000000)


def timed(ms):
    def outer(func):
        def inner(*args, **kwargs):
            t0 = time_ms()
            func(*args, **kwargs)
            t1 = time_ms()
            if t1-t0 > ms:
                logging.warning(f'call to {func} took {t1-t0}ms (>{ms}ms)')
        return inner
    return outer