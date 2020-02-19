from sqlalchemy import Column, Integer, String, Boolean

from components.component import Component, component_repr


class Entity(Component):
    __tablename__ = 'entity'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, nullable=False)
    name = Column(String(50), index=True, nullable=False)
    abstract = Column(Boolean, default=False, nullable=False)
    static = Column(Boolean, default=False, nullable=False)  # if true, hide from 'interact' functionality
    zone = Column(Integer, index=True)

    def get_readable_key(self):
        return f'{self.name}@{self.id}'

    def __repr__(self):
        return component_repr(self)
