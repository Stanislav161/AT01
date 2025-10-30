import math
import unittest


def safe_modulo(a, b):
    """
    Вычисляет остаток от деления a на b.
    Возвращает остаток с тем же знаком, что и делимое (a).
    Выбрасывает ZeroDivisionError при делении на ноль.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")

    # Реализация, которая дает остаток с тем же знаком, что и делимое
    return a - b * math.trunc(a / b)


class TestSafeModulo(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(safe_modulo(10, 3), 1)
        self.assertEqual(safe_modulo(20, 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(safe_modulo(-10, 3), -1)
        self.assertEqual(safe_modulo(10, -3), 1)
        self.assertEqual(safe_modulo(-10, -3), -1)

    def test_zero_dividend(self):
        self.assertEqual(safe_modulo(0, 5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            safe_modulo(10, 0)
        with self.assertRaises(ZeroDivisionError):
            safe_modulo(0, 0)

    def test_edge_cases(self):
        self.assertEqual(safe_modulo(7, 7), 0)
        self.assertEqual(safe_modulo(1, 10), 1)
        self.assertEqual(safe_modulo(15, 4), 3)


if __name__ == "__main__":
    unittest.main()