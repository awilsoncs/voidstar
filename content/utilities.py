from components.weather.snow_fall import SnowFall
from components.attack_start_listeners.move_peasants_in import MovePeasantsIn
from components.announce_game_start import AnnounceGameStart
from components.season_reset_listeners.add_farmstead import AddFarmstead
from components.actors.calendar_actor import Calendar
from components.season_reset_listeners.collect_taxes import CollectTaxes
from components.season_reset_listeners.die_in_winter import CropsDieInWinter
from components.weather.freeze_water import FreezeWater
from components.season_reset_listeners.move_peasants_out import MovePeasantsOut
from components.season_reset_listeners.reset_health import ResetHealth
from components.season_reset_listeners.spawn_sapling_in_spring import SpawnSaplingInSpring
from components.season_reset_listeners.upgrade_houses import UpgradeHouse
from components.weather.weather import Weather
from engine import core
from components.base_components.entity import Entity


def make_calendar():
    entity_id = core.get_id('calendar')
    return [
        entity_id,
        [
            Entity(id=entity_id, entity=entity_id, name='calendar'),
            AnnounceGameStart(entity=entity_id),
            Calendar(entity=entity_id),
            ResetHealth(entity=entity_id),
            CollectTaxes(entity=entity_id),
            UpgradeHouse(entity=entity_id),
            AddFarmstead(entity=entity_id),
            MovePeasantsOut(entity=entity_id),
            MovePeasantsIn(entity=entity_id),
            SnowFall(entity=entity_id),
            CropsDieInWinter(entity=entity_id),
            FreezeWater(entity=entity_id),
            Weather(entity=entity_id),
            SpawnSaplingInSpring(entity=entity_id)
        ]
    ]
