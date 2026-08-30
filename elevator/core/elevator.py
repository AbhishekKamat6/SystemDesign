from dataclasses import dataclass,field
from models.door import Door
from models.enums import Direction
import threading
from state.elevator_state import ElevatorState
from state.idle_state import IdleState
from core.stop_set import StopSet

@dataclass(slots=True)
class Elevator:

  id : int
  capacity_kg : float = 800.0
  current_floor : int = 0 
  stops : StopSet = field(default_factory=StopSet)
  door : Door = field(default_factory=Door)

  _direction : Direction = field(default=Direction.NONE) # default is when you want to assign a value
  _state : ElevatorState = field(default_factory=IdleState) # default_factory is used when you want to create default value --? It roughly means _state = IdleState()
  _overloaded : bool = field(default=False,repr=False)
  _in_service :  bool = field(default=True,repr=False)
  _door_alert :  bool = field(default=False,repr=False)
  _lock : threading.Lock = field(default_factory=threading.Lock,repr=False)

  # props
  @property
  def direction(self):
    return self._direction

  @direction.setter
  def direction(self,value:Direction):
    self._direction = value

  @property
  def state(self):
    return self._state

  @state.setter
  def state(self,value):
    self._state = value

  @property
  def in_service(self):
    return self._in_service

  @in_service.setter
  def in_service(self,value):
    self._in_service = value

  @property
  def overloaded(self):
    return self._overloaded

  @overloaded.setter
  def overloaded(self,value):
    self._overloaded = value

  @property
  def door_alert(self):
    return self._door_alert

  @door_alert.setter
  def door_alert(self,value):
    self._door_alert = value

  @property
  def pending_stops(self) -> list[int] :
     return self.stops.snapshot()

  # commands
  def add_stop(self,floor:int):
    if self.current_floor != floor:
      self.stops.add(floor)

  def step(self)->None : 
    with self._lock:
      if self._in_service:
        self._state.step(self)

  def move_one_floor(self)->None:

    next_stop = self.next_stop_any_direction()

    if next_stop is None : 
      return

    self.direction = Direction.UP if next_stop > self.current_floor else Direction.DOWN

    self.current_floor += 1 if self._direction == Direction.UP else  -1


  def next_stop_any_direction(self)->int|None:

    match self.direction:
      case Direction.DOWN:
        primary , fallback = self.stops.floor , self.stops.ceiling
      case _:
        primary , fallback = self.stops.ceiling , self.stops.floor

    candidate = primary(self.current_floor)

    return candidate if candidate is not None else fallback(self.current_floor)

    

    
  


  
  
