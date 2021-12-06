from collections import defaultdict
from typing import Set, Dict, List, Iterable, Generic, Type, Callable

from engine.component import Component
from engine.core import get_id, log_debug
from engine.types import EntityDictIndex, EntityDict, T, ComponentType, ComponentList


class ComponentManager(object):
    """Provide an interface between the disk and game logic."""
    def __init__(self):
        self.components: Dict[ComponentType, ComponentList] = defaultdict(list)
        self.components_by_entity: EntityDictIndex = defaultdict(lambda: defaultdict(list))
        self.components_by_id: Dict[int, Component] = {}
        self.component_types: List[ComponentType] = []

    # properties
    @property
    def entities(self) -> Set[int]:
        return set(k for k in self.components_by_entity.keys())

    def _add_component_to_indexes(self, component: T, component_type: Type[T]) -> None:
        """Add a component to ComponentManager's indexes."""
        entity_component_dict = self.components_by_entity[component.entity]
        components = entity_component_dict[component_type]
        components.append(component)
        self.components_by_id[component.id] = component

    @log_debug(__name__)
    def clear(self) -> None:
        """Clears the active zone. Note that this doesn't have any impact on persistence."""
        self.components = defaultdict(list)
        self.components_by_entity = defaultdict(lambda: defaultdict(list))
        self.components_by_id = {}

    # data manipulation methods
    def add(self, component: Component, *components: Component) -> None:
        """Add one or more components to the ComponentManager."""
        self._add(component)
        for component in components:
            self._add(component)

    def get(self, component_type: T, query: Callable[[T], bool] = lambda x: True) -> List[T]:
        """Get all components of a given type."""
        return [x for x in self.components[component_type] if query(x)]

    def get_entity(self, entity: int) -> EntityDict:
        """Get a dictionary representing an Entity."""
        return self.components_by_entity[entity]

    def get_all(self, component_type: Type[T], entity: int) -> List[T]:
        """Get all components of a given type for a given entity."""
        return self.components_by_entity[entity][component_type]

    # TODO consider whether we really want to support this.
    def get_one(self, component_type: Type[T], entity) -> Generic[T]:
        """Get a single component of a given type for a given entity."""
        output = self.components_by_entity[entity][component_type]
        if output:
            return output[0]
        return None

    def get_component_by_id(self, cid) -> Component:
        """Get a specific component by component ID."""
        return self.components_by_id[cid]

    def delete(self, entity: int) -> None:
        """
        Delete an entity and its components.

        Does not delete any references to the entity or its components.
        """
        components = self.get_entity(entity)

        for _, component_list in components.items():
            for component in component_list:
                self.delete_component(component)
        if entity in self.entities:
            self._delete_entity_from_indexes(entity)

    def delete_all(self, entities: Iterable[int]) -> None:
        for entity in entities:
            self.delete(entity)

    def _delete_entity_from_indexes(self, entity: int) -> None:
        components = self.components_by_entity[entity]
        for component_type, components in components.items():
            for component in components:
                self.components[component_type].remove(component)
        del self.components_by_entity[entity]

    def delete_component(self, component: Component) -> None:
        """
        Delete a single component.

        Does not delete any references to the component.
        """
        if not component:
            raise ValueError("Cannot delete None.")
        entity = component.entity
        if entity in self.entities:
            component_types = type(component).mro()
            for component_type in component_types:
                if component in self.components[component_type]:
                    self.components[component_type].remove(component)
                if component in self.components_by_entity[component.entity][component_type]:
                    self.components_by_entity[component.entity][component_type].remove(component)
            if component.id in self.components_by_id:
                del self.components_by_id[component.id]

    def delete_components(self, component_type: ComponentType) -> None:
        components_to_delete = [c for c in self.components[component_type]]
        for component in components_to_delete:
            self.delete_component(component)

    # private methods
    def _add(self, component: Component) -> None:
        """Add a component to the db."""
        component.id = get_id()
        entity = component.entity
        component_classes = type(component).mro()
        for component_class in component_classes:
            self.components_by_entity[entity][component_class].append(component)
            self.components[component_class].append(component)
        self.components_by_id[component.id] = component
