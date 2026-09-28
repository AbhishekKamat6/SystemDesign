
class RecipeNotFoundException(Exception):
    def __init__(self,value):
        super().__init__(value)

class InvalidAmountException(Exception):
    def __init__(self,value):
        super().__init__(value)

class InvalidStateException(Exception):
    def __init__(self,value):
        super().__init__(value)

class QuantityNotAvailableException(Exception):
    def __init__(self,value):
        super().__init__(value)

class InSufficientBalanceException(Exception):
    def __init__(self,value):
        super().__init__(value)

class IngredientUnavailableException(Exception):
    def __init__(self,value):
        super().__init__(value)
        
