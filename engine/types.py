from typing import NewType, Dict, Type, List, TypeVar, Tuple

from engine.components.component import Component

T = TypeVar('T')
U = TypeVar('U')
EntityId = NewType('EntityId', int)
ComponentType = NewType('ComponentType', Type[T])
ComponentList = NewType('ComponentList', List[ComponentType])
Entity = NewType('Entity', Tuple[EntityId, List[Component]])
EntityDict = NewType('EntityDict', Dict[ComponentType, List[Component]])
EntityDictIndex = NewType('EntityIndex', Dict[EntityId, EntityDict])

# An entity consisting of more than one tile
ComplexEntity = NewType('ComplexEntity', Tuple[EntityId, List[Entity]])
