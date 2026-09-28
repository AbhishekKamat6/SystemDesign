
from dataclasses import dataclass , field
from traffic_signal import TrafficSignal
from state.green import GreenState 
from state.red import RedState
from state.yellow import YellowState

PHASE_COUNT = 4

@dataclass(slots=True)
class IntersectionController:

    north_south_signal : TrafficSignal 
    east_west_signal : TrafficSignal
    _phase : int = field(default=0)

    def __post_init__(self) -> None:
        if self.north_south_signal is None or self.east_west_signal is None:
            raise ValueError("IntersectionController requires two non-null TrafficSignal instances")
        self._apply_phase()


    @property
    def phase(self):
        return self._phase

    def _apply_phase(self)->None:
        match self._phase:

            case 0 :
                self.north_south_signal.force_state(GreenState())
                self.east_west_signal.force_state(RedState())
            case 1:
                self.north_south_signal.force_state(YellowState())
                self.east_west_signal.force_state(RedState())
            case 2:
                self.north_south_signal.force_state(RedState())
                self.east_west_signal.force_state(GreenState())
            case 3:
                self.north_south_signal.force_state(RedState())
                self.east_west_signal.force_state(YellowState())
    
    def step(self)->None:
        self._phase = (self._phase + 1) % PHASE_COUNT
        self._apply_phase()

    