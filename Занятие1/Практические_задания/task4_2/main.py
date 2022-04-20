from itertools import count


def task():
    iterator_numbers = count(1, 1)
    numbers = list(map(lambda num: num**2, filter(lambda num: num % 2 == 0, iterator_numbers)))  # TODO заменить на map и filter

    for num in range(10):  # TODO напечатать первые 10 чисел
        print(next(iterator_numbers))  # TODO с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
