from sqlalchemy import Column, Integer, Boolean

import settings
from components.component import Component, component_repr


class Senses(Component):
    __tablename__ = 'senses'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, index=True, nullable=False)
    sight_radius = Column(Integer, default=-1)
    dirty = Column(Boolean, default=True)

    def __init__(self, entity, sight_radius=settings.TORCH_RADIUS):
        self.entity = entity
        self.sight_radius = sight_radius

    def __repr__(self):
        return component_repr(self)
