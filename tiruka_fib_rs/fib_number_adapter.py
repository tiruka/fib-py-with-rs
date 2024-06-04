from .tiruka_fib_rs import fibonacci_number, fibonacci_numbers
from .counter import Counter


class TirukaFibNumberAdapter:
    def __init__(self, number_input: int | list[int]) -> None:
        self.input = number_input
        self.success: bool = False
        self.result: None | int | list[int] = None
        self.error_message: None | str = None
        self._counter: Counter = Counter()
        self._process_input()

    def _define_success(self) -> None:
        self.success = True
        self._counter.increment()

    def _process_input(self) -> None:
        if isinstance(self.input, int):
            self.result = fibonacci_number(self.input)
            self._define_success()
        elif isinstance(self.input, list):
            self.result = fibonacci_numbers(self.input)
            self._define_success()
        else:
            self.error_message = (
                "Invalid input type, input must be an integer or a list of integers."
            )

    @property
    def count(self) -> int:
        return self._counter.value
