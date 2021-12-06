from typing import NewType, Dict, Type, List, TypeVar

from engine.component import Component

T = TypeVar('T')
EntityId = NewType('EntityId', int)
ComponentType = NewType('ComponentType', Type[T])
ComponentList = NewType('ComponentList', List[ComponentType])
EntityDict = NewType('EntityDict', Dict[ComponentType, List[Component]])
EntityDictIndex = NewType('EntityIndex', Dict[EntityId, EntityDict])
