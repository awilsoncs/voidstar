from dataclasses import dataclass

from components.tags.tag import Tag


@dataclass
class CorpseTag(Tag):
    value: str = 'corpse'
