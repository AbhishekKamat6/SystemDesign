from dataclasses import dataclass
from observers.base import Base
from models.signal_color import SignalColor

@dataclass(slots=True)
class PedestrianSignal(Base):

    crossing_id : str

    def signal_change(self, color:SignalColor):

        if color.value == SignalColor.RED :
            print(f"{self.crossing_id} : signal is red pedestrians cannot cross")
        else :
            print(f"{self.crossing_id} : pedestrians can start crossing")

        

    

     