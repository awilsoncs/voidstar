from abc import ABC, abstractmethod
from typing import Tuple

from components.base_components.component import Component


class CostMapper(Component, ABC):
    @abstractmethod
    def get_cost_map(self, scene):
        raise NotImplementedError("Cannot use abstract base class")
