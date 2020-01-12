from sqlalchemy import Integer, Column, ForeignKey

from components.component import Component, component_repr


class CursorResult(Component):
    __tablename__ = 'cursor_result'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, ForeignKey('entity.id', ondelete='CASCADE'), unique=True, index=True, nullable=False)
    x = Column(Integer, default=None)
    y = Column(Integer, default=None)

    def __repr__(self):
        return component_repr(self)
