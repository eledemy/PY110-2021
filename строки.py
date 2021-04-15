# Даны две строки. Если они начинаются с одинаковых символов, то напечатать «ДА», иначе – «НЕТ».

def task_1(str_1, str_2, k):  # k - это количество похожих символов
    result = str_1[:k] == str_2[:k]  # [:k] срезы, от начала строки (0) до k-того символа

    answer = "Да" if result else "Нет"  # тернарный оператор
    print(answer)


if __name__ == '__main__':
    s1 = "abcd"
    s2 = "abc"
    task_1(s1, s2, 2)


# Заменить все вхождения подстроки str1 на подстроку str2. Если нужно просто проверить вхождение подстроки в строку,
# то можно воспользоваться оператором in.

def task_2(str_, src, dst):  # str_ - исходная строка, src - то, что ищу; dst - на что нужно поменять src.
    str_ = str_.replace(src, dst)
    print(str_)


if __name__ == '__main__':
    s0 = 'abcdef'
    s1 = 'ab'
    s2 = '12'
    task_2(s0, s1, s2)


# поиск наличия в исходной строке подстроки, которую хочет заменить пользователь

def task_2(str_, src, dst):  # str_ - исходная строка, src - то, что ищу; dst - на что нужно поменять src.
    if src in str_:
        str_ = str_.replace(src, dst)
        print(str_)
    else:
        print('Замены не произошло')


if __name__ == '__main__':  # обозначает некую отладочную информацию, которая не импортируется в другие файлы
    s0 = 'abcdef'
    s1 = 'az'
    s2 = '12'
    task_2(s0, s1, s2)

# Дана последовательность слов (предложение). Напечатать все слова в алфавитном порядке. Итак, дано некое предложение

"""
Данное предложение будет разбиваться на отдельные слова. 
В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""


def task_3():
     print()

if __name__ == '__main__':
    main_str = """
Данное предложение будет разбиваться на отдельные слова. 
В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
    list_words = main_str.split()  # получаем список слов, разбивает строки на слова
    replace_punctuation = '.,!'    # объявляю все знаки препинания

    for i, word in enumerate(list_words):
        for punc in replace_punctuation:
            word = word.replace(punc, '')
            list_words[i] = word
    print(list_words)


# Удалить в строке все лишние пробелы. Лишними считаются пробелы, следующие непосредственно за пробелами.
# Т.е. между словами всегда должен находиться один пробел.

str_with_space = "    123.    test   print test11    "  # исходная строка
split_str = str_with_space.split(" ")   # Чтобы удалить все лишние пробелы разобьём строку по пробелам
print(split_str)

split_str = [word for word in split_str if word != ""]
join_str = "|".join(split_str)
print(join_str)

str_with_space = "    123.    test   print test11    "
list_str = str_with_space.split("|")
def my_join(list_str, sep):
    join_result = ""
    for word in list_str[:-1]:
        join_result += word
        join_result += sep

    last_word = list_str[-1]
    join_result += last_word

    return join_result

if __name__ == '__main__':
    str_with_space = "    123.    test   print test11    "
    list_str = str_with_space.split("|")


    print(my_join)