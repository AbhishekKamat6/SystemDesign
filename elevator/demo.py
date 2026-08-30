from core.controller import ElevatorController
from strategy.nearest_car import NearestCarStrategy
from models.enums import Direction


def scenerio_look_sweep_and_observer()->None : 

    ctrl = ElevatorController(car_count=2, floors=15, strategy=NearestCarStrategy())

    ctrl.request_pickup(5, Direction.UP)
    ctrl.request_pickup(3, Direction.UP)
    for t in range(8):
        ctrl.step()

    ctrl.request_floor(0, 12)  # rider boarded car 0, wants floor 12
    for t in range(8, 20):
        ctrl.step()


def scenario_duplicate_dedup() -> None:
    print("\n=== 2. Duplicate hall calls collapse to one stop ===")
    ctrl = ElevatorController(car_count=1, floors=15, strategy=NearestCarStrategy())
    ctrl.request_pickup(7, Direction.UP)
    ctrl.request_pickup(7, Direction.UP)  # second press: no-op
    status = ctrl.get_status()[0]
    print(f"pending stops after two identical presses: {status.pending_stops}  (expect [7])")

def scenario_overload_blocks_movement() -> None:
    print("\n=== 4. Overload refuses movement even with a stop pending ===")
    ctrl = ElevatorController(car_count=1, floors=15, strategy=NearestCarStrategy())
    ctrl.request_pickup(9, Direction.UP)
    ctrl.cars[0].is_overloaded = True

    for t in range(3):
        ctrl.step()
    status = ctrl.get_status()[0]
    print(f"floor after 3 ticks while overloaded: {status.current_floor}  (expect 0, unmoved)")

    ctrl.cars[0].is_overloaded = False
    for t in range(9):
        ctrl.step()
    status = ctrl.get_status()[0]
    print(f"floor after load clears + 9 ticks: {status.current_floor}  (expect 9)")


def scenario_maintenance_redispatch() -> None:
    print("\n=== 5. Pulling a car mid-trip re-dispatches its stops ===")
    ctrl = ElevatorController(car_count=2, floors=15, strategy=NearestCarStrategy())
    ctrl.request_pickup(10, Direction.UP)  # car 0 (nearest) takes this

    ctrl.set_maintenance(0, on=True)  # pull car 0 before it arrives

    stops = {c.id: c.pending_stops for c in ctrl.cars.values()}
    print(f"pending stops per car after pulling car 0: {stops}  (expect stop moved to car 1)")


if __name__ == "__main__":
    scenerio_look_sweep_and_observer()
    # scenario_duplicate_dedup()
    # scenario_overload_blocks_movement()
    # scenario_maintenance_redispatch()

