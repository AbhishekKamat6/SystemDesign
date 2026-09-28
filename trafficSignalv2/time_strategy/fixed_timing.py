from dataclasses import dataclass , field
from models.signal_color import SignalColor
from time_strategy.base import Base

DEFAULT_TIMINGS = {
    SignalColor.RED : 30,
    SignalColor.YELLOW : 4,
    SignalColor.GREEN : 24
}

@dataclass(slots=True)
class FixedTimingStrategy(Base):

    time : dict = field(default_factory=lambda:dict(DEFAULT_TIMINGS))

    def time_calculation(self,color):

      if self.time.get(color) is None :
         raise ValueError(f"Colour is not configure for default timings , color : {color}")

      return  self.time.get(color)



