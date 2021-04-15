# Дан список точек, найти самую удаленную точку от начала координат

def get_distance(point):
    x = point[0]
    y = point[1]
    return (x ** 2 + y ** 2) ** 0.5

if __name__ == '__main__':
    pts = [
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    print(max(map(get_distance, pts)))

# Дан список чисел в различных форматах, привести их к типу int

num_list = [
    "12",
    "14",
    3.1415926,
    5,
    0xFF,
    0b1010101010
]
print(tuple(map(int, num_list)))

# Дан список чисел округлить их до 2 знаков после запятой

from itertools import repeat

def my_round(num):
    return round(num, 2)

if __name__ == '__main__':
    my_floats = [
        4.356345,
        6.0934,
        3.245235,
        9.77545,
        2.164234234,
        8.884234235,
        4.595235346645
    ]

    print(list(map(round, my_floats, (2, 2, 2))))

    print(list(map(round, my_floats, [2] * len(my_floats))))

    print(list(map(round, my_floats, repeat(2))))


# Найти длину самого длинного слова

if __name__ == '__main__':

    list_words = [
    "Goldenrod",
    "Purple",
     "Salmon",
     "Turquoise",
     "Cyan"
    ]

    print(max(map(len, list_words)))

# Перевести все слова в верхний регистр

if __name__ == '__main__':

    list_words = [
    "Goldenrod",
    "Purple",
     "Salmon",
     "Turquoise",
     "Cyan"
    ]

    iter_words = map(str.upper, list_words)
    for word in iter_words:
        print(word)

    for word in map(str.upper, list_words):
        print(word)

# Поэлементно сложить два списка

def my_sum(a, b):
    return a + b

if __name__ == '__main__':

    a = [1, 2, 3]
    b = [4, 5, 6]

    print(list(map(my_sum, a, b)))
