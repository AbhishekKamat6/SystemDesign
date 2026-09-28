
from models.signal_model import SignalColor
from dataclasses import dataclass , field
from strategy.base import SignalTimingStartegy

DEFAULT_DURATIONS = {
    SignalColor.GREEN : 25,
    SignalColor.YELLOW : 4,
    SignalColor.RED : 30
}

@dataclass(slots=True)
class FixedTimingStrategy(SignalTimingStartegy):

    durations : dict[SignalColor,int] = field(default_factory=lambda:dict(DEFAULT_DURATIONS))

    def get_duration_seconds(self, color):
        if color not in self.durations:
            raise ValueError(f"No duration configured for {color}")

        return self.durations[color]

