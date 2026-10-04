"""Модуль вычисления фигурных чисел.

Реализовано 20-угольное фигурное число:
    P(n) = (18 * n^2 - 16 * n) / 2
"""


def twenty_gonal(n: int) -> int:
    """
    Возвращает n-е 20-угольное фигурное число.

    :param n: целое число (n >= 1).
    :raises TypeError: если n не целое число.
    :raises ValueError: если n < 1.
    :return: n-е 20-угольное число.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n < 1:
        raise ValueError("Число должно быть положительным (n >= 1)")

    return (18 * n * n - 16 * n) // 2