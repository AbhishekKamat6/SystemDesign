


class ElevatorSystemError(Exception):
    pass


class InvalidFloorException(ElevatorSystemError):
    def __init__(self,floor:int):
        super().__init__(f"Floor {floor} is outside the building")

class UnkownCarException(ElevatorSystemError):
    def __init__(self,car_id):
        super().__init__(f"car with card_id : {car_id} is not availabel")

class NoCarAvailableException(ElevatorSystemError):
    def __init__(self) -> None:
        super().__init__("Every car is out of service")

class CarInMaintenanceException(ElevatorSystemError):
    def __init__(self, car_id: int) -> None:
        super().__init__(f"Car {car_id} is in maintenance")
        self.car_id = car_id