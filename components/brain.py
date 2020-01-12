from sqlalchemy import Column, Integer, Enum, Boolean

import components.enums
from components.component import Component, component_repr
from components.enums import Intention
from engine.constants import PRIORITY_MEDIUM


class Brain(Component):
    """Provides control and other 'mind' information."""
    __tablename__ = 'brain'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, index=True, nullable=False)
    control_mode = Column(Enum(components.enums.ControlMode))  # which system controls this entity
    priority = Column(Integer, default=PRIORITY_MEDIUM)
    take_turn = Column(Boolean, default=False)  # if True, take a turn on update

    # action management
    intention = Column(Enum(Intention), default=Intention.NONE)
    intention_target = Column(Integer)

    def __repr__(self):
        return component_repr(self)
