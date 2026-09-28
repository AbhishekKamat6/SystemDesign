from abc import ABC , abstractmethod
from models.signal_color import SignalColor

class Base(ABC):

    @abstractmethod
    def signal_change(self,color:SignalColor):
        pass