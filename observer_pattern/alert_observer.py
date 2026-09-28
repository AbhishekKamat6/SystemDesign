from stock_observer import StockObserver

class AlertObserver(StockObserver):

    def update(self):
        print("updates alert service")
