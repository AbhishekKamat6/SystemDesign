from beverages.beverage_decorator import BeverageDecorator
from models.enums import IngredientType


class ExtraMilk(BeverageDecorator):
    @property
    def cost(self):
        return self.inner.cost + 20

    @property
    def needs(self):
        n = self.inner.needs
        n[IngredientType.MILK] = n.get(IngredientType.MILK,0) + 20
        return n

    @property
    def description(self):
        return self.inner.description + ", Extra milk"

class ExtraSugar(BeverageDecorator):
    @property
    def cost(self):
        return self.inner.cost + 20

    @property
    def needs(self):
        n = self.inner.needs
        n[IngredientType.SUGAR] = n.get(IngredientType.SUGAR,0) + 20
        return n

    @property
    def description(self):
        return self.inner.description + ", Extra sugar"