from abc import ABC , abstractmethod
from models.signal_model import SignalColor

class SignalState(ABC):

    @property
    @abstractmethod
    def color(self)->SignalColor:
        pass
