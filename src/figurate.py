"""Модуль вычисления 20-угольных фигурных чисел.
Формула: P(n) = (18 * n^2 - 16 * n) / 2
"""

def twenty_gonal(n: int) -> int:
    """
    Возвращает n-е 20-угольное фигурное число.
    
    :param n: целое положительное число (1 <= n <= 5000).
    :raises TypeError: если n не целое число.
    :raises ValueError: если n выходит за пределы допустимого диапазона.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n < 1:
        raise ValueError("Число должно быть положительным (n >= 1)")
    if n > 5000:
        raise ValueError("Число слишком большое (максимум 5000)")

    return (18 * n * n - 16 * n) // 2
