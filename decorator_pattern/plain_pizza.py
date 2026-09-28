from dataclasses import dataclass
from pizza import Pizza

@dataclass(slots=True)
class PlainPizza(Pizza):

    initial_cost:int

    @property
    def cost(self):
        return self.initial_cost

    @property
    def desc(self):
        return "plain pizza"
