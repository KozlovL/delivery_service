# ID посылки - 119527642
"""Оптимизация перевозки роботов.

Название файла:
    robot_transport.py

Описание:
    Данный скрипт решает задачу оптимального распределения роботов по
    транспортным платформам с ограниченной грузоподъёмностью.
    Каждый робот имеет определённый вес, и на одной платформе
    можно перевезти либо одного робота, либо двух,
    если их совокупный вес не превышает заданный лимит.
    Программа использует метод двух указателей для
    минимизации количества необходимых платформ.

Использование:
    python robot_transport.py

Входные данные:
    - Список целых чисел, представляющий веса роботов.
    - Одно целое число, представляющее грузоподъёмность одной платформы.

Выходные данные:
    - Одно целое число — минимальное количество транспортных платформ,
    необходимых для перевозки всех роботов.

Пример:
    Ввод:
        50 70 80 50
        100
    Вывод:
        3

Зависимости:
    Убедитесь, что все необходимые зависимости установлены.
    В данном случае используется стандартная библиотека Python.

Пример запуска:
    Для запуска программы используйте команду:
    python delivery_service.py
"""
from typing import List


def two_pointer_func(masses: List[int], limit: int) -> int:
    """Функция с двумя указателями.

    Функция для нахождения минимального количества транспортных платформ для
    перевозки роботов.

    Аргументы:
        masses (List[int]): Список весов роботов.
        limit (int): Грузоподъёмность одной транспортной платформы.

    Возвращает:
        int: Минимальное количество платформ, необходимых для
        перевозки всех роботов.
    """
    masses = sorted(masses)
    left_pointer = 0
    right_pointer = len(masses) - 1
    count = 0

    while right_pointer >= 0 and left_pointer <= right_pointer:
        if masses[left_pointer] + masses[right_pointer] <= limit:
            left_pointer += 1
        right_pointer -= 1
        count += 1

    return count


def main():
    """Главная функция для запуска программы.

    Ввод:
        - Список весов роботов (через пробел).
        - Грузоподъёмность одной платформы.

    Вывод:
        - Минимальное количество платформ, необходимых для
        перевозки всех роботов.
    """
    masses_array = [int(value) for value in input().split()]
    limit_value = int(input())
    result_number = two_pointer_func(masses_array, limit_value)
    print(result_number)


if __name__ == "__main__":
    main()
