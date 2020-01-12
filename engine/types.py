from typing import Tuple, NewType, Dict, Type, List

import sqlalchemy.types as types
from sqlalchemy import VARCHAR

from components.component import Component
from engine import colors

EntityDict = NewType('EntityDict', Dict[Type[Component], List[Component]])
EntityDictIndex = NewType('EntityIndex', Dict[int, EntityDict])
ComponentType = NewType('ComponentType', Type[Component])


class Color(types.TypeDecorator):
    """Convert between database hex color and app tuple color."""

    @property
    def python_type(self):
        return Tuple

    def process_literal_param(self, value, dialect):
        return colors.to_hex(value)

    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        return colors.to_hex(value)

    def process_result_value(self, value, dialect):
        return colors.from_hex(value)
