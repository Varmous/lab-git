"""CLI-программа: вычисление чисел Фибоначчи и 20-угольных чисел."""

import sys

from fibonacci import fibonacci
from figurate import twenty_gonal


def ask_n(min_value: int, max_value: int, label: str) -> int:
    """Запрашивает целое число в заданном диапазоне. Защищена от любых ошибок."""
    while True:
        try:
            raw = input(f"Введите n для {label} (от {min_value} до {max_value}): ").strip()
            
            # 1. Проверка на пустой ввод
            if not raw:
                print("Ошибка: ввод не может быть пустым. Повторите ввод.")
                continue
            
            # 2. Защита от слишком длинных строк
            if len(raw) > 10:
                print("Ошибка: введено слишком длинное число. Повторите ввод.")
                continue

            # 3. Проверка, что это целое число
            try:
                n = int(raw)
            except ValueError:
                print(f"Ошибка: '{raw}' не является целым числом. Повторите ввод.")
                continue

            # 4. Проверка нижней границы
            if n < min_value:
                print(f"Ошибка: n должно быть >= {min_value}. Повторите ввод.")
                continue
                
            # 5. Проверка верхней границы (лимит 5000)
            if n > max_value:
                print(f"Ошибка: n не должно превышать {max_value}. Повторите ввод.")
                continue
                
            return n

        # Ловим Ctrl+Z (Windows) или Ctrl+D (Linux)
        except EOFError:
            print("\nЗавершение работы (EOF). Выход.")
            sys.exit(0)
        # Ловим Ctrl+C
        except KeyboardInterrupt:
            print("\nПринудительный выход (Ctrl+C).")
            sys.exit(0)


def run_fibonacci() -> int:
    """Спрашивает n и выводит число Фибоначчи."""
    n = ask_n(min_value=0, max_value=5000, label="числа Фибоначчи")
    try:
        result = fibonacci(n)
        print(f"F({n}) = {result}")
    except Exception as e:
        print(f"Ошибка вычисления: {e}")
    return 0


def run_figurate() -> int:
    """Спрашивает n и выводит 20-угольное число."""
    n = ask_n(min_value=1, max_value=5000, label="20-угольного числа")
    try:
        result = twenty_gonal(n)
        print(f"P20({n}) = {result}")
    except Exception as e:
        print(f"Ошибка вычисления: {e}")
    return 0


def print_help() -> int:
    """Показывает справку."""
    print("Использование:")
    print("  py main.py fib   - вычислить число Фибоначчи F(n), n >= 0")
    print("  py main.py fig   - вычислить 20-угольное число P(n), n >= 1")
    print("  py main.py       - показать эту справку")
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
    try:
        sys.exit(main())
    except Exception as e:
        # Глобальная страховка
        print(f"\nКритическая ошибка: {e}")
        sys.exit(1)
