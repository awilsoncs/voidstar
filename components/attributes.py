from sqlalchemy import Column, Integer

from components.component import Component, component_repr


class Attributes(Component):
    __tablename__ = 'attributes'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, index=True, nullable=False)
    hp = Column(Integer, default=10, nullable=False)
    max_hp = Column(Integer, default=10, nullable=False)

    def __repr__(self):
        return component_repr(self)
