from typing import NewType, Dict, Type, List

from engine.component import Component

EntityDict = NewType('EntityDict', Dict[Type[Component], List[Component]])
EntityDictIndex = NewType('EntityIndex', Dict[int, EntityDict])
ComponentType = NewType('ComponentType', Type[Component])
