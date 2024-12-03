import abc
from typing import TypeVar, Generic

T = TypeVar('T')  # Тип элементов алгебры

class Algebra(abc.ABC, Generic[T]):
    """
    Абстрактный класс для алгебраических структур.
    """

    @abc.abstractmethod
    def zero(self) -> T:
        """Возвращает нулевой элемент структуры."""
        pass

    @abc.abstractmethod
    def one(self) -> T:
        """Возвращает единичный элемент структуры."""
        pass

    @abc.abstractmethod
    def add(self, a: T, b: T) -> T:
        """Возвращает сумму элементов a и b."""
        pass

    @abc.abstractmethod
    def multiply(self, a: T, b: T) -> T:
        """Возвращает произведение элементов a и b."""
        pass

    @abc.abstractmethod
    def inverse_add(self, a: T) -> T:
        """Возвращает обратный элемент по сложению к элементу a."""
        pass


    @abc.abstractmethod
    def inverse_multiply(self, a: T) -> T:
        """Возвращает обратный элемент по умножению к элементу a."""
        pass


class IntegerAlgebra(Algebra[int]):
    """
    Конкретная реализация алгебры для целых чисел.
    """
    def zero(self) -> int:
        return 0

    def one(self) -> int:
        return 1

    def add(self, a: int, b: int) -> int:
        return a + b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def inverse_add(self, a: int) -> int:
        return -a

    def inverse_multiply(self, a: int) -> float:
        if a == 0:
            raise ZeroDivisionError("Деление на ноль")
        return 1 / a


