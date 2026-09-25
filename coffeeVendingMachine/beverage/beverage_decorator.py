from beverage.base_beverage import Beverage

from dataclasses import dataclass


@dataclass(slots=True)
class BeverageDecorator(Beverage):
    inner : Beverage