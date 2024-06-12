from .tiruka_fib_rs import calculate_times, calculate_parameters


class NumpyInterface:
    def __init__(self) -> None:
        self.inventory = {}

    def calc_times(self, distance, traffic_grade):
        result = calculate_times({}, distance, traffic_grade)
        self.inventory["car_time"] = result["times"][0][0]
        self.inventory["truck_time"] = result["times"][1][0]

    def calc_parameters(self, car_time, truck_time):
        result = calculate_parameters({}, car_time, truck_time)
        self.inventory["distance"] = result["parameters"][0][0]
        self.inventory["traffic_grade"] = result["parameters"][1][0]
