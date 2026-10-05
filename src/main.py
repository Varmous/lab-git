import sys

from fibonacci import fibonacci
from figurate import twenty_gonal


def ask_n(min_value: int, label: str) -> int:
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
    n = ask_n(min_value=0, label="числа Фибоначчи")
    result = fibonacci(n)
    print(f"F({n}) = {result}")
    return 0


def run_figurate() -> int:
    n = ask_n(min_value=1, label="20-угольного числа")
    result = twenty_gonal(n)
    print(f"P20({n}) = {result}")
    return 0


def print_help() -> int:
    print("Использование:")
    print("  py main.py fib   - вычислить число Фибоначчи F(n), n >= 0")
    print("  py main.py fig   - вычислить 20-угольное число P(n), n >= 1")
    print("  py main.py       - показать эту справку")
    return 0


def main() -> int:
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
