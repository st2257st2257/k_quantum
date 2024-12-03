import abc
from typing import TypeVar, Generic, List, Union

T = TypeVar('T')  # Обобщенный тип элементов векторного пространства


class VectorSpace(abc.ABC, Generic[T]):
    """
    Абстрактный класс для векторного пространства.
    Определяет базовые операции.
    """

    @abc.abstractmethod
    def zero_vector(self) -> T:
        """Возвращает нулевой вектор."""
        pass

    @abc.abstractmethod
    def add(self, v1: T, v2: T) -> T:
        """Возвращает сумму двух векторов."""
        pass

    @abc.abstractmethod
    def scalar_multiply(self, scalar: float, v: T) -> T:
        """Возвращает произведение скаляра и вектора."""
        pass

    @abc.abstractmethod
    def negative(self, v: T) -> T:
        """Возвращает вектор, противоположный вектору v."""
        pass

    @abc.abstractmethod
    def dimension(self) -> int:
        """Возвращает размерность векторного пространства."""
        pass

    #  Дополнительный метод для удобства работы:
    def __eq__(self, other):
      """Проверка равенства двух объектов."""
      return id(self) == id(other)

