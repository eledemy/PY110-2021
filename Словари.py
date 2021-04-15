empty_dict = {}  # пустой словарь

dict_1 = {'a': 1,
          'b': 2,
          'c': 3}

dict_2 = dict(a=1,
              b=2,
              c=3)

gen_dict = {i: i**2 for i in range(5)}  # генератор словарей

empty_dict['new'] = 1
dict_1[(1, 2)] = 12
gen_dict[5] = 25

print(empty_dict)
print(dict_1)
print(gen_dict)

prices = {'apple': 80,
          'orange': 65,
          'banana': 40}

for fruit in prices:  # итерируемся по ключам
    print(fruit)

for fruit in prices:
    print(prices[fruit])

for item in prices.items():
    print(item)

# Определить, как часто встречается определенный символ в строке.
# Создадим словарь, в который в качестве ключа
# будет использоваться символ, а в качестве значения, количество раз, сколько этот элемент встречался в строке.
# Создадим функцию, которая будет принимать строку, а возвращать словарь с частотой каждого символа.
# Чтобы не считать символы разного регистра два раза, с помощью метода строки lower переведем строку в нижний регистр

def task_6():
    print()

if __name__ == '__main__':
    main_str = """
Данное предложение будет разбиваться на отдельные слова. 
В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
    dict_char = {}
    for char in main_str:
        if char.isalpha():                     # проверяет, принадлежит ли символ букве
           if char not in dict_char:           # проверяются в словаре только ключи
              dict_char[char] = 1
           else:
              dict_char[char] += 1

    for symbol, count in dict_char.items():    # У словаря есть метод items, который за один раз возвращает
                                               # кортеж состоящий из пары ключ-значение
        print(symbol, count)

print("ABC.".lower())

# 1.Получить список цифр числа N

N = 123456
str_ = str(N)
list_ = list(str_)
print(str_)
print(list_)
print(type(list_))

# найти сумму чисел

list_digit = [int(d) for d in str(N)]      #приведение строк в списке к int
print(list_digit)

sum_ = sum(list_digit)
print(sum_)

# найти сумму всех четных чисел
sum_2 = sum([d for d in list_digit if d % 2 == 0])
print(sum_2)

# 4.Найти количество цифр

len_ = len(list_digit)
print(len_)

# 6.Получить список всех цифр стоящих на нечетных (четных) местах. Например, 12345 -> [1, 3, 5]

list_even = list_digit[::2]
print(list_even)

# является ли число паллиндромом

str(N) == str (N){}



