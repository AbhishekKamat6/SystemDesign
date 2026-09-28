

from dataclasses import dataclass , field
from strategy.base import SignalTimingStartegy
from state.base import SignalState
from state.red import RedState
from observer.base import SignalObserver
import threading

@dataclass(slots=True)
class TrafficSignal:

    id : str
    timing_strategy : SignalTimingStartegy
    _state : SignalState = field(default_factory=RedState) #every signal starts safely at red
    _observers : list[SignalObserver] = field(default_factory=list)
    _lock : threading.Lock = field(default_factory=threading.Lock)

    @property
    def current_colour(self):
        return self._state.color

    @property
    def current_duration_seconds(self)->int:
        return self.timing_strategy.get_duration_seconds(self._state.color)

    def add_observers(self,observer:SignalObserver)->None:
        self._observers.append(observer)

    def force_state(self,new_state:SignalState)->None:
        with self._lock : 
            self._state = new_state
            self._notify_observers()

    def _notify_observers(self):

        for observer in self._observers :
            observer.on_signal_change(self._state.color)