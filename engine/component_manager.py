import logging
from collections import defaultdict
from time import perf_counter, perf_counter_ns
from typing import Set, Dict, List, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import force_instant_defaults

import settings
from components import Entity
from components.component import Component
from engine.core import time_ms, timed
from engine.types import EntityDict, EntityDictIndex, ComponentType

# Sets default values during instantiation, so that we don't need to commit the db when creating new entities.
force_instant_defaults()


class ComponentManager(object):
    """Provide an interface between the disk and game logic."""
    def __init__(self):
        self.db: Session = None  # persistent game data
        self.components: EntityDict = defaultdict(list)
        self.components_by_entity: EntityDictIndex = defaultdict(lambda: defaultdict(list))
        self.components_by_id: Dict[int, Component] = {}
        self.component_types: List[ComponentType] = []
        self.current_zone: int = None

    # properties
    @property
    def entities(self) -> Set[int]:
        return set(k for k in self.components_by_entity.keys())

    # data orchestration methods
    def thaw(self, zone: int) -> None:
        """Unpack components for this zone into their managed lists."""
        self.freeze()
        logging.debug(f'Thawing zone: {zone}')
        t0 = time_ms()

        for component_type in self.component_types:
            self._thaw_components_by_type(component_type, zone)
        self.current_zone = zone
        entity_count = len(self.components[Entity])

        t1 = time_ms()
        logging.debug(f'Successfully thawed zone: {zone}, entities loaded: {entity_count} in {t1-t0}ms')

    def _thaw_components_by_type(self, component_type: ComponentType, zone: int) -> None:
        """Thaw all components of a given type in a given zone."""
        if component_type is not Entity:
            components_q = self.db.query(component_type) \
                .join(Entity, Entity.id == component_type.entity) \
                .filter(Entity.zone == zone)
        else:
            components_q = self.db.query(Entity).filter(Entity.zone == zone)
        for component in components_q:
            self._add_component_to_indexes(component, component_type)
        self.components[component_type] = components_q.all()

    def _add_component_to_indexes(self, component: Component, component_type: ComponentType) -> None:
        """Add a component to ComponentManager's indexes."""
        entity_component_dict = self.components_by_entity[component.entity]
        components = entity_component_dict[component_type]
        components.append(component)
        self.components_by_id[component.id] = component

    def freeze(self) -> None:
        """Freeze a zone, committing it to the database and removing it from execution."""
        print(f'Freezing zone.')
        self.db.commit()
        self.components = defaultdict(list)
        self.components_by_entity = defaultdict(lambda: defaultdict(list))
        self.components_by_id = {}
        self.current_zone = None

    # data manipulation methods
    def add(self, component: Component, *components: Component) -> None:
        """Add one or more components to the ComponentManager."""
        self._add(component)
        for component in components:
            self._add(component)

    def commit(self) -> None:
        """Commit all transactions to the DB."""
        if self.db:
            self.db.commit()

    def get(self, component_type: ComponentType) -> List[Component]:
        """Get all components of a given type."""
        return self.components[component_type]

    def get_entity(self, entity: int) -> EntityDict:
        """Get a dictionary representing an Entity."""
        return self.components_by_entity[entity]

    def get_all(self, component_type: Type[Component], entity: int) -> List[Component]:
        """Get all components of a given type for a given entity."""
        return self.components_by_entity[entity][component_type]

    # TODO consider whether we really want to support this.
    def get_one(self, component_type: Type[Component], entity) -> Component:
        """Get a single component of a given type for a given entity."""
        output = self.components_by_entity[entity][component_type]
        if output:
            return output[0]
        return None

    def get_component_by_id(self, cid) -> List[Component]:
        """Get a specific component by component ID."""
        return self.components_by_id[cid]

    def delete(self, entity: int) -> None:
        """
        Delete an entity and its components.

        Does not delete any references to the entity or its components.
        """
        for component_type in self.component_types:
            components = self.get_all(component_type, entity)
            for component in components:
                self.delete_component(component)
        if entity in self.entities:
            self._delete_entity_from_indexes(entity)

    def _delete_entity_from_indexes(self, entity: int) -> None:
        components = self.components_by_entity[entity]
        for component_type, components in components.items():
            for component in components:
                self.components[component_type].remove(component)
                del self.components_by_id[component.id]
        del self.components_by_entity[entity]

    def delete_component(self, component: Component) -> None:
        """
        Delete a single component.

        Does not delete any references to the component.
        """
        if not component:
            raise ValueError("Cannot delete None.")
        entity = component.entity
        if _get_is_persistent(type(component)):
            # TODO this is fragile
            if component._sa_instance_state.persistent:
                self.db.delete(component)
        if entity in self.entities:
            component_type = type(component)
            if component in self.components[component_type]:
                self.components[component_type].remove(component)
            if component in self.components_by_entity[component.entity][component_type]:
                self.components_by_entity[component.entity][component_type].remove(component)
            if component.id in self.components_by_id:
                del self.components_by_id[component.id]

    # database control methods
    def close(self) -> None:
        """Close the db."""
        if self.db:
            self.db.close()

    def connect(self, world_name: str) -> None:
        """
        Connect the ComponentManager to a sqlite3 db named [world_name].world.

        If the ComponentManager already has an open db, connect() will close that db before opening the new one.
        """
        if self.db:
            self.close()
        engine = create_engine(f'sqlite:///{world_name}.world', echo=settings.MEMORY_ECHO)
        Component.metadata.create_all(engine)
        self.db = sessionmaker(bind=engine)()
        self.component_types = Component.__subclasses__()

    # private methods
    def _add(self, component: Component) -> None:
        """Add a component to the db."""
        if _get_is_persistent(type(component)):
            self.db.add(component)
        entity = component.entity
        component_class = component.__class__
        self.components_by_entity[entity][component_class].append(component)
        self.components[component_class].append(component)
        self.components_by_id[component.id] = component


def _get_is_persistent(component: Component) -> bool:
    return (
        '__persistent__' not in component.__dict__
        or component.__persistent__
    )
