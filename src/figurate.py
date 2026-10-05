#Модуль вычисления фигурных чисел.

def twenty_gonal(n: int) -> int:

    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n < 1:
        raise ValueError("Число должно быть положительным (n >= 1)")

    return (18 * n * n - 16 * n) // 2
