from state.elevator_state import ElevatorState
from dataclasses import dataclass

@dataclass(slots=True)
class MovingState(ElevatorState):

    def step(self,car):
       if car.overloaded : 
           return

       car.move_one_floor()

       if car.stops.contains(car.current_floor):
           car.stops.remove(car.current_floor)
           car.door.open()

           from state.door_open_state import DoorOpenState
           car.state = DoorOpenState()
        

    