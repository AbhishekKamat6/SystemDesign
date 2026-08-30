from abc import ABC , abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from core.elevator import Elevator

class ElevatorState(ABC):

    @abstractmethod
    def step(self,car:"Elevator") -> None :
      pass