# поиск суммы элементов в списке
start = 1
stop = 100

sum_ = 0  # заводим переменную для суммы

i: int
for i in range(start, stop + 1):
    sum_ += i

print(sum_)

# поиск произведения элементов в списке
start = 1
stop = 100

mul = 1  # заводим переменную для суммы

for i in range(start, stop + 1):
    mul *= i

print(mul)

# поиск максимального и минимального значения
start = 1
stop = 5

list_num = list(range(start, stop))
print(list_num)
# предположим, что наш минимум стоит на первом месте в списке
max_ = list_num[0]
for num in list_num:
    if num > max_:
        max_ = num
print(max_)

# последнее нечетное число
start = 1
stop = 10

list_num = list(range(start, stop))
odd = None  # предполагаемое последнее нечное число

max_ = list_num[0]
for num in list_num:
    # остаток от деления на 2 дает в остатке 1, провод длиной 3 метра намотать на бобину диамером 2 метра,
    # остался 1 метр провода
    if num % 2 == 1:
        odd = num
print(odd)

# найти последнее отрицательное число
start = -10
stop = 10

list_num = list(range(start, stop))
odd = None    # предполагаемое последнее отрицательное число

for num in list_num:
        if num < 0:
            odd = num
print(odd)

# найти первое отрицательное число
start = -10
stop = 10

list_num = list(range(start, stop))
odd = None    # предполагаемое первое отрицательное число
is_find = False    #число найдено?
for num in list_num:
        if num < 0 and not is_find:
            odd = num
            is_find = True
print(odd)

