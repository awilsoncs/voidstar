import random

import engine
import settings
from components import Entity, Appearance, Coordinates, Attributes, Brain, Senses
from components.enums import Intention
from engine.palettes import Palette
from gui.menus import Menu
from systems.utilities import retract_intention


def run(scene):
    for brain in [b for b in scene.cm.get(Brain) if b.intention is Intention.SHOW_DEBUG_SCREEN]:
        scene.gui.add_element(
            Menu(
                "Debug Options",
                [
                    "examine game objects",
                    "heal",
                    "regenerate palette",
                    "suicide",
                    "test message",
                    "commit db",
                    "teleport to"
                ],
                settings.INVENTORY_WIDTH,
                handle_debug(scene)
            )
        )
        retract_intention(scene, brain.entity)


def handle_debug(scene):
    def callback(index):
        if index == 0:
            entities = scene.cm.get(Entity)
            entities = [e for e in entities if not e.static]
            entities = sorted(entities, key=lambda e: e.id)
            scene.gui.add_element(
                Menu(
                    "Examine which?",
                    [entity.name for entity in entities],
                    settings.INVENTORY_WIDTH,
                    handle_debug_objects(scene, entities)
                )
            )
        elif index == 1:
            health = scene.cm.get_one(Attributes, entity=engine.constants.PLAYER_ID)
            if health:
                health.hp = health.max_hp
        elif index == 2:
            new_palette = Palette()
            coordinates = scene.cm.get(Coordinates)
            coordinates = [c for c in coordinates if c.id != scene.player]
            for coord in coordinates:
                appearance = scene.cm.get_one(Appearance, coord.entity)
                if not appearance:
                    continue
                if coord.terrain and coord.blocks:
                    appearance.bg_color = random.choice(new_palette.secondary)
                else:
                    appearance.color = random.choice(new_palette.primary)
            scene.controller.reload()
        elif index == 3:
            health = scene.cm.get_one(Attributes, entity=engine.constants.PLAYER_ID)
            if health:
                health.hp = 0
        elif index == 4:
            scene.message("test message")
        elif index == 5:
            scene.cm.commit()
            scene.message("(dbg) db committed.", color=engine.colors.light_green)
        elif index == 6:
            entities = scene.cm.get(Entity)
            entities = [e for e in entities if not e.static]
            entities = sorted(entities, key=lambda e: e.id)
            scene.gui.add_element(
                Menu(
                    "Teleport to which?",
                    [entity.name for entity in entities],
                    settings.INVENTORY_WIDTH,
                    handle_teleport_to(scene, entities)
                )
            )
    return callback


def handle_debug_objects(scene, entities):
    def callback(index):
        if index is None:
            return
        target = entities[index]
        print(f'Debug Show Item: {target.name}')
        for _, values in scene.cm.get_entity(target.id).items():
            for component in values:
                print(f'\t{component}')

    return callback


def handle_teleport_to(scene, entities):
    def callback(index):
        if index is None:
            return
        target = entities[index]
        entity = target.id
        target_coords = scene.cm.get_one(Coordinates, entity=entity)
        if target_coords:
            player_coords = scene.cm.get_one(Coordinates, entity=engine.constants.PLAYER_ID)
            player_coords.x = target_coords.x
            player_coords.y = target_coords.y
            senses = scene.cm.get_one(Senses, entity=engine.constants.PLAYER_ID)
            senses.dirty = True
    return callback
