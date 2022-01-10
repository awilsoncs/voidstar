import logging
from time import perf_counter_ns

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
                if e.sym == tcod.event.K_RETURN:
                    return e
                return e


def get_noise_generator(dimensions=3):
    return tcod.noise.Noise(dimensions=dimensions, octaves=32)


def get_id(name=None):
    global ID_SEQ
    global NAME_ID_MAP

    if not name:
        ID_SEQ += 1
        return ID_SEQ

    if name in NAME_ID_MAP:
        return NAME_ID_MAP[name]
    else:
        NAME_ID_MAP[name] = get_id()
        return get_id(name)


ID_SEQ = 100
NAME_ID_MAP = {}


def get_named_ids():
    return NAME_ID_MAP


def set_named_ids(new_mapping):
    global NAME_ID_MAP
    logging.info("Core::set_named_ids id mapping loaded")
    NAME_ID_MAP = new_mapping


def time_ms():
    return int(perf_counter_ns() / 1000000)


def timed(ms, module):
    def outer(func):
        def inner(*args, **kwargs):
            logger = logging.getLogger(module)

            t0 = time_ms()
            func(*args, **kwargs)
            t1 = time_ms()
            if t1-t0 > ms:
                logger.warning(f'call to {func} took {t1-t0}ms (>{ms}ms)')
        return inner
    return outer


def log_debug(module):
    def outer(fn):
        def decorated(*args, **kwargs):
            logger = logging.getLogger(module)

            try:
                logger.debug(f' {fn.__name__} => {args} - {kwargs}')
                result = fn(*args, **kwargs)
                logger.debug(f' {fn.__name__} <= {result}')
                return result
            except Exception as ex:
                logger.debug("Exception {0}".format(ex))
                raise ex
        return decorated
    return outer
