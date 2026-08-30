import threading
from bank.bank_service import BankService
from model.models import Account,Card
from exception.exceptions import InsufficientBalanceException , DailyLimitExceedException

class InMemoryBankService(BankService):

    DAILY_LIMIT = 2500

    def __init__(self):
        self._accounts : dict[str,Account] = {}
        self._pins : dict[str,str] = {}
        self._lock = threading.Lock()

    def add_account(self, account:Account, card_number:str, pin:str):
        self._accounts[account.account_id] = account
        self._pins[card_number] = pin

    def verify_pin(self, card:Card, pin:str)->bool:
        return self._pins.get(card.card_number) == pin

    def get_balance(self,account_id:str):
        account = self._accounts.get(account_id)
        return account.balance

    def debit(self, account_id:str, amount:int):
        with self._lock:
            account = self._accounts.get(account_id)

            if account.balance < amount : 
                raise InsufficientBalanceException()
            if account._daily_used + amount > self.DAILY_LIMIT :
                raise DailyLimitExceedException()

            account.balance = account.balance - amount
            account._daily_used = account._daily_used + amount

            print(f"Debited {amount} from account {account_id}. New balance: {account.balance}. Daily used: {account._daily_used}")

    def credit(self, account_id:str , amount:int):
        with self._lock :
            account = self._accounts.get(account_id)
            account.balance = account.balance + amount


    