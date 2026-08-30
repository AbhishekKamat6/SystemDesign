from dataclasses import dataclass , field
from models.enums import Direction
from core.elevator import Elevator
from strategy.scheduling_strategy import SchedulingStrategy
from exception.exceptions import InvalidFloorException , UnkownCarException , NoCarAvailableException , CarInMaintenanceException
import threading
from models.request import HallRequest 

@dataclass(slots=True,frozen=True)
class CarStatus:

    id : int
    current_floor : int
    direction : Direction
    state_name : str
    in_service : bool
    overloaded : bool 
    door_open : bool 
    pending_stops : list[int]

    @classmethod
    def of(cls,car:Elevator)->"CarStatus" :
        return cls(
            id = car.id,
            current_floor = car.current_floor,
            direction = car.direction,
            state_name = car.state,
            in_service=car.in_service,
            overloaded=car.overloaded,
            door_open=car.door.is_open,
            pending_stops=car.pending_stops,
        )

@dataclass(slots=True)
class ElevatorController():

    car_count : int
    floors : int
    strategy : SchedulingStrategy

    cars : dict[int,Elevator]  = field(init=False) #it means don't include cars in the generated __init__().Instead, you want the controller itself to create the cars.Thats when __post_init__ comes in
    _pending : set[str] = field(default_factory=set,repr=False) # default_factory=set creates a fresh empty set for every object while repr=False hides that internal set from the dataclass's printed representation.
    _pending_lock : threading.Lock = field(default_factory=threading.Lock,repr=False)

    # After the dataclass has finished its normal initialization, run this additional initialization code
    def __post_init__(self) -> None :
        if self.car_count < 1:
            raise ValueError("Car count must be >= 1")
        if self.floors < 2 :
            raise ValueError("Floors must be >= 2")
        self.cars = {i : Elevator(i) for i in range(self.car_count)}

    # internals
    def _validate_floor(self,floor:int)->None:
        if not ( 0 <= floor < self.floors ):
            raise InvalidFloorException(floor)

    def _get_car(self,car_id:int)->Elevator:
        car = self.cars.get(car_id)

        if car is None:
            return UnkownCarException(car_id)
        return car

    def _clear_served_hall_calls(self,floor:int)->None:

        with self._pending_lock : 
            self._pending = {k for k in self._pending if not k.startswith(f"{floor}:")  }
                          #  ↑       ↑                  ↑
                          #  |       |              condition
                          #  |       |
                          #  |    loop through pending
                          #  |
                          # what we want to put
                          # into the new set
    
    # rider facing
    def request_pickup(self,floor:int , direction:Direction):

        self._validate_floor(floor)
        request = HallRequest(floor,direction)

        with self._pending_lock : 
            if request.key in self._pending : 
                return

            self._pending.add(request.key)
            in_service = [c for c in self.cars.values() if c.in_service ]
            car = self.strategy.pick_car(in_service,request) if in_service else None

            if car is None : 
               self._pending.discard(request.key)
               raise NoCarAvailableException()

            car.add_stop(floor)

    def request_floor(self,car_id:int , floor:int)->None:

        self._validate_floor(floor)
        car = self._get_car(car_id)

        if not car.in_service:
            raise CarInMaintenanceException(car_id)

        car.add_stop(floor)

    # --- building facing -------------------------------------------------
    def step(self) -> None:
        for car in self.cars.values():
            before = (car.current_floor, car.direction, car.door.is_open)

            car.step()

            if car.current_floor != before[0]:
                self._clear_served_hall_calls(car.current_floor)

            after = (car.current_floor, car.direction, car.door.is_open)
            # if after != before:
            #     self._notify(car)

    def set_maintenance(self, car_id: int, on: bool) -> None:
        car = self._get_car(car_id)
        car.in_service = not on
        if on:
            self._redispatch_stops(car)

    def get_status(self) -> list[CarStatus]:
        return [CarStatus.of(c) for c in self.cars.values()]


            
     
   