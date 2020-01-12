from sqlalchemy import Column, Integer

from components.component import Component, component_repr


class Owner(Component):
    __tablename__ = 'owner'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, index=True, nullable=False)
    owner = Column(Integer, nullable=False)

    def __repr__(self):
        return component_repr(self)
