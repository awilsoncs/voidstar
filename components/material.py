from sqlalchemy import Integer, Column, Boolean

from components.component import Component, component_repr


class Material(Component):
    __tablename__ = 'material'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, nullable=False)
    blocks = Column(Boolean, default=False)
    blocks_sight = Column(Boolean, default=False)

    def __repr__(self):
        return component_repr(self)
