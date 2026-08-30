


class ATMException(Exception):
    pass

class InvalidAmountException(ATMException):
    def __init__(self,amount):
        super().__init__(f"Invalid amount : {amount}")


class InvalidPinException(ATMException):
    def __init__(self, attempts_left):
        super().__init__(f"Wrong pin , {attempts_left} attempts left")

class CardBlockedException(ATMException):
    def __init__(self):
        super().__init__("Card retained after 3 failed pin attempts")

class CardExpiredException(ATMException):
    def __init__(self):
        super().__init__("Card is expired")

class InsufficientBalanceException(ATMException):
    def __init__(self):
        super().__init__("Insufficient account balance")

class InsufficientCashException(ATMException):
    def __init__(self):
        super().__init__("ATM cannot dispense this amount with current notes")

class DailyLimitExceedException(ATMException):
    def __init__(self):
        super().__init__("Daily withdrawl limit is exceeded") 

class SessionNotFoundException(ATMException):
    def __init__(self):
        super().__init__("No active session - insert a card first")

class IllegalStateException(ATMException):
    pass
       

