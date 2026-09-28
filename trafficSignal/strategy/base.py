
from abc import ABC , abstractmethod 
from models.signal_model import SignalColor

class SignalTimingStartegy(ABC):

  @abstractmethod
  def get_duration_seconds(self,color:SignalColor)->int:
    pass
