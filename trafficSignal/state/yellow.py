from dataclasses import dataclass
from state.base import SignalState
from models.signal_model import SignalColor

@dataclass(slots=True,frozen=True)
class YellowState(SignalState):

    @property
    def color(self)->SignalColor:
        return SignalColor.YELLOW
