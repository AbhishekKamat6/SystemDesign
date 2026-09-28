from dataclasses import dataclass , field
from traffic_signal import TrafficSignal
from states.red import RedState
from states.yellow import YellowState
from states.green import GreenState

PHASE_VALUE = 4

@dataclass(slots=True)
class IntersectionController:

    NorthSouthSignal : TrafficSignal
    EastWestSignal : TrafficSignal
    _phase : int = field(default=0)


    @property
    def phase(self):
        return self._phase

    def _apply_phase(self):

        match self._phase :
            case 0 :
                self.NorthSouthSignal.change_signal(GreenState())
                self.EastWestSignal.change_signal(RedState())
            case 1 : 
                self.NorthSouthSignal.change_signal(YellowState())
                self.EastWestSignal.change_signal(RedState())
            case 2 : 
                self.NorthSouthSignal.change_signal(RedState())
                self.EastWestSignal.change_signal(GreenState())
            case 3 : 
                self.NorthSouthSignal.change_signal(RedState())
                self.EastWestSignal.change_signal(YellowState())
            case 4 : 
                self.NorthSouthSignal.change_signal(GreenState())
                self.EastWestSignal.change_signal(RedState())
     
    def step(self):
        self._phase = (self._phase+1) % PHASE_VALUE
        self._apply_phase()


    