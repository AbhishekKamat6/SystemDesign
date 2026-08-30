from dataclasses import dataclass
from strategy.scheduling_strategy import SchedulingStrategy
from models.request import HallRequest
from core.controller import CarStatus
from models.enums import Direction

PENALTY = 100


def is_on_the_Way(car_direction:Direction, car_floor:int , request:HallRequest)->bool:
    match car_direction:
        case Direction.NONE:
            return True
        case Direction.UP:
            return request.direction == Direction.UP and car_floor <= request.floor
        case Direction.DOWN:
            return request.direction == Direction.DOWN and car_floor >= request.floor




@dataclass(slots=True)
class NearestCarStrategy(SchedulingStrategy):

    def pick_car(self, cars:list[CarStatus] , request:HallRequest)->CarStatus:
        best = None
        best_score = None

        for car in cars:
            distance = abs(car.current_floor - request.floor)
            on_the_way = is_on_the_Way(car.direction, car.current_floor, request)
            score = distance + (0 if on_the_way else PENALTY)
            if best_score is None or score < best_score : 
                best_score , best = score , car

        return best
