from enum import Enum, auto


class Role(Enum):
    """
    Interface for all employee role types.
    """
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()