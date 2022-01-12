import logging
from dataclasses import dataclass, field

from engine import constants
from engine.core import get_id


@dataclass
class Component(object):
    id: int = field(default_factory=get_id)
    entity: int = constants.INVALID

    def on_component_delete(self, cm):
        """Called by the CM when the component is deleted."""
        pass

    def _log_debug(self, message):
        logging.debug(self.__msg_format(message))

    def _log_warning(self, message):
        logging.warning(self.__msg_format(message))

    def _log_info(self, message):
        logging.info(self.__msg_format(message))

    def _log_error(self, message):
        logging.error(self.__msg_format(message))

    def __msg_format(self, message):
        return f"EID#{self.entity}::{self.__class__.__name__}#{self.id} - {message}"

