import threading
from cash.cash_handler import NoteHandler
from exception.exceptions import InsufficientCashException

class CashDispenser:

    def __init__(self,chain:NoteHandler):
        self.chain = chain
        self._lock = threading.Lock()

    def can_dispense(self,amount:int)->bool:
        with self._lock:
            return amount > 0 and amount % 100 == 0 and self.chain.plan(amount)

    def dispense(self,amount:int)->dict:
        with self._lock:

            # if not self.chain.plan(amount,plan):
            #     raise InsufficientCashException()
            plan = {}
            plan = self.chain.commit(plan)
            return plan

    def refill(self, note_value:int , count:int ) -> int:
        handler = self.chain

        while handler:
            if handler.note_value == note_value:
                handler.refill(count)
                return handler.count

            handler = handler.next

        raise ValueError(f"No handler for denomination {note_value}")

