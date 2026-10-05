#Модуль вычисления чисел Фибоначчи.

def fibonacci(n: int) -> int:

    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n < 0:
        raise ValueError("Число должно быть неотрицательным (n >= 0)")

    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
