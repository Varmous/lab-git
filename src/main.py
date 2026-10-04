"""CLI-программа: вычисление чисел Фибоначчи и 20-угольных чисел.

Использование:
    python main.py fib     - вычислить число Фибоначчи
    python main.py fig     - вычислить 20-угольное число
    python main.py         - показать справку
"""

import sys

from fibonacci import fibonacci
from figurate import twenty_gonal


def ask_n(min_value: int, label: str) -> int:
    """Запрашивает у пользователя целое число n >= min_value."""
    while True:
        raw = input(f"Введите n для {label} (n >= {min_value}): ").strip()
        try:
            n = int(raw)
        except ValueError:
            print(f"Ошибка: '{raw}' не является целым числом. Повторите ввод.")
            continue
        if n < min_value:
            print(f"Ошибка: n должно быть >= {min_value}. Повторите ввод.")
            continue
        return n


def run_fibonacci() -> int:
    """Спрашивает n и выводит число Фибоначчи."""
    n = ask_n(min_value=0, label="числа Фибоначчи")
    result = fibonacci(n)
    print(f"F({n}) = {result}")
    return 0


def run_figurate() -> int:
    """Спрашивает n и выводит 20-угольное число."""
    n = ask_n(min_value=1, label="20-угольного числа")
    result = twenty_gonal(n)
    print(f"P20({n}) = {result}")
    return 0


def print_help() -> int:
    """Показывает справку."""
    print("Использование:")
    print("  python main.py fib   - вычислить число Фибоначчи F(n), n >= 0")
    print("  python main.py fig   - вычислить 20-угольное число P(n), n >= 1")
    print("  python main.py       - показать эту справку")
    return 0


def main() -> int:
    """Точка входа."""
    if len(sys.argv) < 2:
        return print_help()

    command = sys.argv[1].lower()

    if command == "fib":
        return run_fibonacci()
    elif command == "fig":
        return run_figurate()
    else:
        print(f"Неизвестная команда: {command}")
        print()
        return print_help()


if __name__ == "__main__":
    sys.exit(main())