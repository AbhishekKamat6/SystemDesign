from datetime import date, timedelta

from atm import Atm
from bank.in_memory_bank_service import InMemoryBankService
from cash.cash_handler import Note2000Handler, Note500Handler, Note100Handler
from cash.cash_dispenser import  CashDispenser
from model.models import Card, Account


def main():
    # --- Wire everything up ---
    bank = InMemoryBankService()
    bank.add_account(Account("ACC-1", 10000), "CARD-1", "1234")

    chain = Note2000Handler(10)
    chain.link_next(Note500Handler(20)).link_next(Note100Handler(50))
    atm = Atm(bank, CashDispenser(chain))

    # --- Run ---
    card = Card("CARD-1", "ACC-1", date.today() + timedelta(days=730))
    atm.insert_card(card)    # Idle -> CardInserted
    atm.enter_pin("12347")    # CardInserted -> Authenticated
    atm.enter_pin("1234")
    atm.withdraw(100)    # cash check, debit, Dispensing -> Idle
    atm.eject_card()  
    print(atm._last_dispensed_notes)

    atm.insert_card(card)    # Idle -> CardInserted
    atm.enter_pin("12347")    # CardInserted -> Authenticated
    atm.enter_pin("1234")
    atm.withdraw(2500)  # O/P -: Daily withdrawl limit is exceeded

    # prints: Dispensed: {2000: 1, 500: 3}
    #         Card returned

    atm.eject_card()

    print(atm.last_dispensed_notes)
 


if __name__ == "__main__":
    main()