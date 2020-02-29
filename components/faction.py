import enum
from sqlalchemy import Column, Integer, Enum

from components.component import Component, component_repr


class Faction(Component):

    class Options(enum.Enum):
        NONE = 'none'
        MONSTER = 'monster'
        PEASANT = 'peasant'

    __tablename__ = 'faction'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, nullable=False)
    faction = Column(Enum(Options))

    def __repr__(self):
        return component_repr(self)
