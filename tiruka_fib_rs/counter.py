from .singleton import Singleton


class Counter(metaclass=Singleton):
    def __init__(self) -> None:
        self._value = 0

    def increment(self) -> None:
        self._value += 1

    def decrement(self) -> None:
        self._value -= 1

    @property
    def value(self) -> int:
        return self._value
