from abc import ABC , abstractmethod
from dataclasses import dataclass
from models.signal_color import SignalColor

@dataclass(slots=True)
class Base(ABC):

    def time_calculation(self,color:SignalColor):
        pass