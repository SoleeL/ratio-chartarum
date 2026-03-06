# domain/game/value_objects/phase.py

from enum import Enum


class Phase(str, Enum):
    BASE_TYPE_SELECTION = "BASE_TYPE_SELECTION"
    BASE_SELECTION = "BASE_SELECTION"
    BOARD = "BOARD"