# Квадраты всех четных натуральных чисел (используя map и filter)

from itertools import count

def pow_2(num):
    return num ** 2

def is_even(num):
    return (num % 2 == 0)

if __name__ == '__main__':

    iter_even_pow_2 = filter(is_even, count(1))
    iter_pow_2 = map(pow_2, iter_even_pow_2)

    iter_pow_2 = map(pow_2,
                     filter(is_even, count(1)))

    for _ in range(10):
        print(next(iter_pow_2))

# Из случайного списка  Найти все отрицательные числа кратные 3

import random

n = 100
random_list = [random.randint(-100, 100) for _ in range(n)]

def list_(num):
    return ((num % 3 == 0) and num < 0)

filter_ = list(filter(list_, random_list))


print(filter_)


# Дана входная строка и массив чисел, необходимо вернуть строку с теми буквами,
# которые стоят на указанных местах (два варианта, используя и не используя list comprehensions)

from itertools import repeat

def task_3(str_, list_index):
    result = "".join(map(get_char, repeat(str_), list_index))
    return result

def get_char(str_, index):
    return str_[index]

if __name__ == '__main__':
    example_str = "Всем привет"
    indexes = [1, 3, 5]


    print(task_3(example_str, indexes))


