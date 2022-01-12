import logging
from dataclasses import dataclass

import engine
import settings
from components import Entity, Coordinates, Attributes, Senses
from components.abilities.build_wall_ability import BuildWallAbility
from components.actors.energy_actor import EnergyActor
from components.brains.brain import Brain
from components.brains.painters.create_gold_actor import PlaceGoldController
from components.brains.painters.create_hordeling_actor import PlaceHordelingController
from components.brains.default_active_actor import DefaultActiveActor
from components.events.die_events import Die
from components.pathfinding.breadcrumb_tracker import BreadcrumbTracker
from components.serialization.load_game import LoadGame
from components.serialization.save_game import SaveGame
from components.wrath_effect import WrathEffect
from content.cursor import make_cursor
from content.farmsteads.houses import place_farmstead
from content.terrain.roads import connect_point_to_road_network
from gui.easy_menu import EasyMenu

@dataclass
class ShowDebug(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    def act(self, scene):
        scene.gui.add_element(
            EasyMenu(
                "Debug Options",
                {
                    "examine game objects": get_examine_game_objects(scene),
                    "heal": get_heal(scene),
                    "get rich": get_rich(scene),
                    "place hordeling": get_painter(scene, PlaceHordelingController),
                    "place gold": get_painter(scene, PlaceGoldController),
                    "wrath": get_wrath(scene, self.entity),
                    "suicide": get_suicide(scene),
                    "teleport to": get_teleport_to(scene),
                    "toggle ability": get_toggle_masonry(scene),
                    "toggle pathing": get_pathfinding_for(scene),
                    "spawn a home": get_spawn_home(scene),
                    "dump game state": get_dump_game(scene),
                    "read game state": get_read_game(scene)
                },
                settings.INVENTORY_WIDTH,
            )
        )
        scene.cm.delete_component(self)


def get_examine_game_objects(scene):
    def out_fn():
        entities = scene.cm.get(Entity)
        entities = [e for e in entities if not e.static]
        entities = sorted(entities, key=lambda e: e.id)
        scene.gui.add_element(
            EasyMenu(
                "Examine which?",
                {entity.get_readable_key(): get_examine_object(scene, entity.entity) for entity in entities},
                settings.INVENTORY_WIDTH,
            )
        )

    return out_fn


def get_examine_object(scene, entity):
    def out_fn():
        entity_blob = scene.cm.get_entity(entity)
        entity_component = entity_blob[Entity][0]
        print(f'Debug Show Item: {entity_component.name}')

        components = []

        for _, values in entity_blob.items():
            for component in values:
                if component not in components:
                    components.append(component)
        for component in components:
            print(f'\t{component}')

    return out_fn


def get_heal(scene):
    def out_fn():
        health = scene.cm.get_one(Attributes, entity=engine.constants.PLAYER_ID)
        if health:
            health.hp = health.max_hp

    return out_fn


def get_painter(scene, painter):
    def out_fn():
        coords = scene.cm.get_one(Coordinates, entity=scene.player)
        cursor = make_cursor(coords.x, coords.y)
        scene.cm.add(*cursor[1])
        player_controller = scene.cm.get_one(Brain, entity=scene.player)
        new_controller = painter(
            entity=scene.player,
            old_actor=player_controller.id,
            cursor=cursor[0]
        )
        scene.cm.stash_component(player_controller.id)
        scene.cm.add(new_controller)
    return out_fn


def place_gold(scene):
    def out_fn():
        coords = scene.cm.get_one(Coordinates, entity=scene.player)
        cursor = make_cursor(coords.x, coords.y)
        scene.cm.add(*cursor[1])
        player_controller = scene.cm.get_one(Brain, entity=scene.player)
        new_controller = PlaceGoldController(
            entity=scene.player,
            old_actor=player_controller.id,
            cursor=cursor[0]
        )
        scene.cm.stash_component(player_controller.id)
        scene.cm.add(new_controller)
    return out_fn


def get_rich(scene):
    def out_fn():
        scene.gold += 100

    return out_fn


def get_suicide(scene):
    def out_fn():
        scene.cm.add(Die(entity=scene.player))
    return out_fn


def get_teleport_to(scene):
    def out_fn():
        entities = scene.cm.get(Entity)
        entities = [e for e in entities if not e.static]
        entities = sorted(entities, key=lambda e: e.id)
        scene.gui.add_element(
            EasyMenu(
                "Examine which?",
                {entity.get_readable_key(): get_teleport_to_entity(scene, entity.entity) for entity in entities},
                settings.INVENTORY_WIDTH,
            )
        )

    return out_fn


def get_teleport_to_entity(scene, entity):
    def out_fn():
        target_coords = scene.cm.get_one(Coordinates, entity=entity)
        if target_coords:
            player_coords = scene.cm.get_one(Coordinates, entity=engine.constants.PLAYER_ID)
            player_coords.x = target_coords.x
            player_coords.y = target_coords.y
            senses = scene.cm.get_one(Senses, entity=engine.constants.PLAYER_ID)
            senses.dirty = True

    return out_fn


def get_wrath(scene, entity):
    def out_fn():
        scene.cm.add(WrathEffect(entity=entity))

    return out_fn


def get_activate_ability(scene):
    def out_fn():
        ability_map = {}

        has_masonry = scene.cm.get_one(BuildWallAbility, entity=scene.player)
        ability_map[f"Masonry ({'X' if has_masonry else ' '}"] = get_toggle_masonry(scene)

        scene.gui.add_element(
            EasyMenu(
                "Toggle which ability?",
                ability_map,
                settings.INVENTORY_WIDTH,
            )
        )

    return out_fn


def get_toggle_masonry(scene):
    def out_fn():
        ability = scene.cm.get_one(BuildWallAbility, entity=scene.player)
        if ability:
            logging.info("Enabling Masonry")
            scene.cm.delete_component(ability)
        else:
            logging.info("Disabling Masonry")
            scene.cm.add(BuildWallAbility(entity=scene.player))

    return out_fn


def get_pathfinding_for(scene):
    def out_fn():
        actors = scene.cm.get(DefaultActiveActor)
        entities = [scene.cm.get_one(Entity, entity=e.entity) for e in actors]
        entities = sorted(entities, key=lambda e: e.id)
        scene.gui.add_element(
            EasyMenu(
                "Toggle pathfinding for which?",
                {entity.get_readable_key(): get_show_pathing(scene, entity.entity) for entity in entities},
                settings.INVENTORY_WIDTH,
            )
        )

    return out_fn


def get_show_pathing(scene, entity):
    def out_fn():
        tracker = scene.cm.get_one(BreadcrumbTracker, entity=entity)
        if tracker:
            scene.cm.delete_component(tracker)
        else:
            scene.cm.add(BreadcrumbTracker(entity=entity))

    return out_fn


def get_spawn_home(scene):
    def out_fn():
        farmstead_id = place_farmstead(scene)
        farmstead_point = scene.cm.get_one(Coordinates, entity=farmstead_id).position
        connect_point_to_road_network(scene, farmstead_point, trim_start=2)
    return out_fn


def get_dump_game(scene):
    def out_fn():
        scene.cm.add(SaveGame(entity=scene.player))
    return out_fn


def get_read_game(scene):
    def out_fn():
        scene.cm.add(LoadGame(entity=scene.player))
    return out_fn
