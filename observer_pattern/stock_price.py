from dataclasses import dataclass , field
from stock_observer import StockObserver

@dataclass(slots=True)
class StockPrice:

    price = field(default=0)
    observers = field(default_factory=list) # --> Aggregation

    def register(self,observer):
        self.observer.append(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.price)

    def price_update(self):
        self.notify_observer()



