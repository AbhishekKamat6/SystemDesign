

class UnknownDrinkException(Exception):
    def __init__(self, value):
       super().__init__(f"drink not found , drink_type : {value}")

class InvalidAmountException(Exception):
    def __init__(self):
       super().__init__(f"The amount you added is not valid")

class IllegalStateException(Exception):
    def __init__(self,value):
        super().__init__(value)

class InsufficientBalanceException(Exception):
    def __init__(self,cost,balance):
        super().__init__(f"Cost {cost} exceed balance {balance}")

class IngredientUnavailableException(Exception):
    def __init__(self, needs):
        super().__init__(f"Ingredients unavailable for needs: {needs}")
        self.needs = needs


class BrewFailureException(Exception):
    """Raised when the physical brew hardware fails mid-pour."""


