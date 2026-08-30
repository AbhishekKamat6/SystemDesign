from dataclasses import dataclass
from state.elevator_state import ElevatorState
from models.enums import Direction

@dataclass
class IdleState(ElevatorState):

    def step(self,car)->None:

        next_stop = car.next_stop_any_direction()

        if next_stop is None : 
            return 

        car._direction = Direction.UP if next_stop > car.current_floor else Direction.DOWN

        from state.moving_state import MovingState

        car.state = MovingState()