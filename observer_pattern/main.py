from stock_price import StockPrice
from price_display_observer import PriceDisplayObserver
from alert_observer import AlertObserver



stock = StockPrice()

display = PriceDisplayObserver()
alert = AlertObserver()

stock.register(display)
stock.register(alert)