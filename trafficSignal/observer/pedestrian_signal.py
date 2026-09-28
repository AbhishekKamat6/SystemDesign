
from dataclasses import dataclass
from observer.base import SignalObserver
from models.signal_model import SignalColor

@dataclass(slots=True)
class PedestrianSignal(SignalObserver):
    crossing_id : str

    def on_signal_change(self,new_color:SignalColor):
        if new_color == SignalColor.RED :
            print(f"Pedestrian crossing {self.crossing_id} : WALK signal ON")
        else:
            print(f"Pedestrian crossing {self.crossing_id} : WALK signal OFF")
