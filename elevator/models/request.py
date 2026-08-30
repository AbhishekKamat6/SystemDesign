from dataclasses import dataclass
from models.enums import Direction

@dataclass(frozen=True,slots=True)
class Request:
    floor : int


@dataclass(frozen=True,slots=True)
class HallRequest(Request):
    """A hall (landing) call: someone outside a car pressing UP/DOWN."""

    direction : Direction = Direction.NONE

    @property
    def key(self)->str:
        return f"{self.floor}:{self.direction}"


@dataclass(frozen=True,slots=True)
class CabRequest(Request):
     """A cab (destination) call: someone inside a specific car picks a floor."""
