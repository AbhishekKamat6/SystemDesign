from abc import ABC , abstractmethod


class State(ABC):

    @abstractmethod
    def insert_money(self,machine,amount):
        pass

    @abstractmethod
    def validate_and_select(self,machine,drink_type,addons):
        pass

    @abstractmethod
    def dispense(self,machine):
        pass

    @abstractmethod
    def refund(self,machine):
        pass