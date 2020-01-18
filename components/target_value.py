from sqlalchemy import Column, Integer

from components.component import Component, component_repr

PEASANT = 100
PLAYER = 50


class TargetValue(Component):
    __tablename__ = 'target_value'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, index=True, nullable=False)
    value = Column(Integer)

    def __repr__(self):
        return component_repr(self)
