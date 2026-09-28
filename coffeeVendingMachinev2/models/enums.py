from enum import auto , Enum

class DrinkType(Enum):
    ESPRESSO = auto()
    CAPPUCINO = auto()
    LATTE = auto()

class IngredientType(Enum):
    WATER = auto()
    SUGAR = auto()
    MILK = auto()

class Addons(Enum):
    EXTRA_MILK = auto()
    EXTRA_SUGAR = auto()
    EXTRA_WATER = auto()