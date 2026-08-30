
from dataclasses import dataclass , field
from state.elevator_state import ElevatorState
from models.enums import Direction

DWELL_TICKS = 2   # how long doors stay open before attempting to close
MAX_REOPENS = 3   # after this many obstructed-close attempts, alert + pull from dispatch

@dataclass(slots=True)
class DoorOpenState(ElevatorState):

    dwell : int = DWELL_TICKS
    reopen_count : int = field(default=0)


    def step(self,car):

        if car.overloaded : 
            return

        self.dwell -= 1

        if self.dwell > 0 :
            return 

        if not car.door.close():

            self.reopen_count += 1
            self.dwell = DWELL_TICKS
            car.door.open()

            if self.reopen_count >= MAX_REOPENS : 
                self.raise_door_alert()
                car._in_service = False

            return

        match car.stops.is_empty:
            case True :
                car._direction = Direction.NONE
                from state.idle_state import IdleState
                car.state = IdleState()

            case False : 
                from state.moving_state import MovingState
                car.state = MovingState()
                 

        

