

from abc import ABC ,abstractmethod

class StockObserver(ABC):

   @abstractmethod
   def update(self,stock):
      pass