
from abc import ABC , abstractmethod
from models.signal_model import SignalColor


class SignalObserver(ABC):

   @abstractmethod
   def on_signal_change(self,signal_id:str,new_color:SignalColor):
      pass