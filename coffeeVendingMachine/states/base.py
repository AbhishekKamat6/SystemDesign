from abc import ABC , abstractmethod

class MachineState(ABC):

    @abstractmethod
    def insert_money(self,machine,amount):
        pass

    @abstractmethod
    def select_drink(self,machine,drink_type,addons):
        pass

    @abstractmethod
    def dispense(self,machine):
        pass

    @abstractmethod
    def refund(self,machine):
        pass