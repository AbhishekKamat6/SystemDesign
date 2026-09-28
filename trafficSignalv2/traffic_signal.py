
from dataclasses import dataclass , field
from states.base import Base 
from states.red import RedState
from time_strategy.base import Base as Strategy
from models.signal_color import SignalColor

@dataclass(slots=True)
class TrafficSignal:

    time_strategy : Strategy 
    _state : Base = field(default_factory=RedState)
    _observers : list = field(default_factory=list)

    @property
    def color(self):
        return self._state.color

    @property
    def time(self):
        return self.time_strategy.time_calculation(self._state.color)

    def notify(self):
        for observer in self._observers:
            observer.signal_change(self._state.color)

    def change_signal(self,color:SignalColor):
        self._state = color
        self.notify()
    
    