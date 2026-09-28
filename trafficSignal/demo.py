from strategy.fixed_timing import FixedTimingStrategy
from traffic_signal import TrafficSignal
from observer.pedestrian_signal import PedestrianSignal
from intersection_controller import IntersectionController

strategy = FixedTimingStrategy()

north_south = TrafficSignal("NS-1",strategy)
east_west = TrafficSignal("EW-1",strategy)


north_south.add_observers(PedestrianSignal("NS=Crossing"))
east_west.add_observers(PedestrianSignal("EW=Crossing"))


controller = IntersectionController(north_south,east_west)

# phase 0 , NS = GREEN and EW = RED
# phase 1 , NS = YELLOW and EW = RED
# phase 2 ,  NS = RED and EW = GREEN


for i in range(4):
    print(
        f"Phase{i} : NS = {north_south.current_colour.value}"
        f"({north_south.current_duration_seconds}s)"
        f"EW={east_west.current_colour.value} ({east_west.current_duration_seconds}s)"
    )

    controller.step()
