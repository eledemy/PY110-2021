def print_matrix(matrix, length=3):
    """
    Функция печатает отформатированную матрицу

    Parameters:
    matrix: список списков
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    length: ширина столбца

    Returns:
        None
 """
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print("{:{}}".format(matrix[row][col], length), end=" ")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()  # переход на новую строчку с 123 на 456

matrix = [...]

table = []
N = 3  # строки
M = 3  # столбцы
a = 0

for i in range(N):  # по строкам
    row = []
    for j in range(M):
        row.append(a)
        a += 1
    table.append(row)
print_matrix(table)

# таблица умножения 9*9
table = []
N = 9  # строки
M = 9  # столбцы
a = 1

for i in range(1, N + 1):  # по строкам
    row = []
    for j in range(1, M + 1):
        ceil = i * j
        row.append(ceil)
    table.append(row)
print_matrix(table)

# сумма всех элементов в матрице
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s = 0  # счетчик суммы
N = len(matrix)  # количество строк в таблице
M = len(matrix[0])  # количество столбцов
for i in range(N):
    for j in range(M):
        ceil = matrix[i][j]
        s += ceil
print(s)

# сумма всех элементов в строке в матрице
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

N = len(matrix)  # количество строк в таблице
M = len(matrix[0])  # количество столбцов
sum_row = []
for i in range(N):
    s = 0
    for j in range(M):
            ceil = matrix[i][j]
            s += ceil
    sum_row.append(s)
print(sum_row)

# СПИСКОВЫЕ ВЛОЖЕНИЯ

# заполнить список квадратами чисел от 1 до 9

list_ = []
for i in range(1, 10):
    list_.append(i**2)
print(list_)

# заполнить список квадратами четных чисел от 1 до 9

list_ = [i ** 2 for i in range(10) if i % 2 == 0]  # тернарный оператор
print(list_)

list_ = [i ** 2 if i % 2 == 0 else -i for i in range(10)]
print(list_)

# 1.Создать список, заполненый целыми числами от N, M с шагом STEP при помощи функции range

list_ = [i for i in range(1, 14, 2)]
print(list_)

# 2.Создать список квадратов целых чисел от n до m

list_ = [i**2 for i in range(1, 14)]
print(list_)

# 3.Создать список квадратов нечетных целых чисел от n до m

list_ = [i**2 for i in range(1, 14) if i % 2 == 1]
print(list_)

# 4.Даны два целых числа A и B (A < B). Найти все целые числа, расположенные между данными числами (включая сами эти
# числа), в порядке их возрастания, а также количество N этих чисел.

list_ = [i for i in range(1, 14)]
a = len(list_ )
print(list_)
print(a)

# 5.Ввести массив, состоящий из 14 элементов целого типа. Найти количество элементов четных по значению.

list_ = [i for i in range(1, 15)]
list_2 = [i for i in range(1, 15) if i % 2 == 0]
a = len(list_2)
print(list_)
print(a)

# 6.Ввести массив, состоящий из 12 элементов целого типа. Получить новый массив, заменив значение
# пятого элемента среднеарифметическим исходного массива.

list_ = list(range(12))
mean_list = sum(list_) / (len(list_))
print(mean_list)
list_[4] = mean_list
print(list_)

# 7.Задан целочисленный массив, состоящий из 11 элементов. Найти количество элементов,
# абсолютное значение которых больше среднего арифметического.

list_1 = list(range(11))
mean = sum(list_1) / len(list_1)
list_great_mean = [num for num in list_1 if num > mean ]
print(list_great_mean)

# 10.Задан массив, состоящий из 15 элементов вещественного типа. Определить количество элементов,
# значения которых больше первого элемента.

list_1 = [float(num) for num in list_1]
print(list_1)

# 13.Дан список целых чисел. Вернуть новый списов в котором все не отрицательные элементы возвведены в куб,
# в противном случае равны нулю

list_1 = [i ** 3 if i > 0 else 0 for i in range(-5, 10)]
print(list_1)

# импорт функций


