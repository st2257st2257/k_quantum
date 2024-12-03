# Пример использования
from .models import IntegerAlgebra

algebra = IntegerAlgebra()

try:
  print(f"Ноль: {algebra.zero()}")
  print(f"Единица: {algebra.one()}")
  print(f"Сумма 2 + 3: {algebra.add(2, 3)}")
  print(f"Произведение 2  3: {algebra.multiply(2, 3)}")
  print(f"Обратный элемент 5 по сложению: {algebra.inverse_add(5)}")
  print(f"Обратный элемент 5 по умножению: {algebra.inverse_multiply(5)}")
  print(f"Обратный элемент 0 по умножению: {algebra.inverse_multiply(0)}") # Возвращает ошибку
except ZeroDivisionError as e:
  print(f"Ошибка: {e}")
