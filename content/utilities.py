from components import Entity
from components.attack_start_listeners.move_peasants_in import MovePeasantsIn
from components.game_start_listeners.announce_game_start import AnnounceGameStart
from components.season_reset_listeners.add_farmstead import AddFarmstead
from components.actors.calendar_actor import Calendar
from components.season_reset_listeners.collect_taxes import CollectTaxes
from components.season_reset_listeners.move_peasants_out import MovePeasantsOut
from components.season_reset_listeners.reset_health import ResetHealth
from components.season_reset_listeners.spawn_sapling_in_spring import SpawnSaplingInSpring
from components.season_reset_listeners.upgrade_houses import UpgradeHouse
from engine import core


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
            SpawnSaplingInSpring(entity=entity_id)
        ]
    ]
