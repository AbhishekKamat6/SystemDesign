from abc import ABC , abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from core.elevator import Elevator

class SchedulingStrategy(ABC):

    @abstractmethod 
    def pick_car ( self , cars : list["Elevator"] ) -> "Elevator | None" : #readme1.md
        pass