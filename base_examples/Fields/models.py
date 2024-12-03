import abc
from abc import ABC


class Field(abc.ABC):
    """
    Абстрактный класс поля.
    Определяет базовые конструкции поля.
    """

    @abc.abstractmethod
    def zero(self):
        """Возвращает нулевой элемент поля. | Существование нулевого элемента."""
        pass

    @abc.abstractmethod
    def one(self):
        """Возвращает единичный элемент поля. | Существование единичного элемента."""
        pass


class FieldElement(Field, abc.ABC):
    """
    Абстрактный класс для элементов поля.
    Определяет базовые операции над элементами поля.
    """

    @abc.abstractmethod
    def __add__(self, other):
        """Возвращает сумму элементов a и b. | Коммутативность сложения."""
        pass

    @abc.abstractmethod
    def __mul__(self, other):
        """Возвращает произведение элементов a и b. | Наличие коммутативности по сложению."""
        pass

    @abc.abstractmethod
    def inverse_add(self, a):
        """Возвращает обратный элемент по сложению к элементу a. | Существование обратного по сложению."""
        pass

    @abc.abstractmethod
    def inverse_multiply(self, a):
        """Возвращает обратный элемент по умножению к элементу a. | Существование обратного для ненулевых."""
        pass

    @abc.abstractmethod
    def is_zero(self, a):
        """Проверяет, является ли элемент нулевым."""
        pass

    @abc.abstractmethod
    def __eq__(self, other):
        """Проверка равенства двух элементов."""
        pass


class IntegerModuloFieldElement(FieldElement, ABC):
    """ Пример реализации для целых чисел по модулю. """

    def __init__(self, value: int, modulus: int) -> None:
        self.value = value % modulus
        self.modulus = modulus

    def zero(self):
        # TODO: проверить корректность места определения нуля
        return 0

    def one(self):
        # TODO: проверить корректность места определения единицы
        return 1

    def __add__(self, other):
        if self.modulus != other.modulus:
            raise ValueError("Различные модули чисел")
        return IntegerModuloFieldElement(
            value=(self.value + other.value) % self.modulus,
            modulus=self.modulus)

    def __mul__(self, other):
        if self.modulus != other.modulus:
            raise ValueError("Различные модули чисел")
        return IntegerModuloFieldElement(
            value=(self.value * other.value) % self.modulus,
            modulus=self.modulus)

    def inverse_add(self, **kwargs):
        self.value = - self.value % self.modulus

    def inverse_multiply(self, **kwargs):
      if self.value == 0:
          raise ZeroDivisionError("Деление на ноль")
      for i in range(1, self.modulus):
          if (self.value * i) % self.modulus == 1:
              return i
      raise ZeroDivisionError("Обратный элемент не существует")

    def is_zero(self, **kwargs):
        return self.value == 0

    def __eq__(self, other):
        if not isinstance(other, IntegerModuloFieldElement):
          return False
        return self.value == other.value and self.modulus == other.modulus
