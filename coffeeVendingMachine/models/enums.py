from enum import Enum , auto

class Ingredient(Enum):
    WATER = auto()
    MILK = auto()
    BEANS = auto()
    SUGAR = auto()

class DrinkType(Enum):
    ESPRESSO = auto()
    CAPUCCINO = auto()
    LATTE = auto()
    BLACK_COFFEE = auto()

class AddOn(Enum):
    EXTRA_MILK = auto()
    EXTRA_SUGAR = auto()
    EXTRA_SHOT = auto()