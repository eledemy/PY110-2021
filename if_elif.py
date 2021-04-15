from typing import Dict, Union, Tuple


def if_elif():

    S = float(input('Введите сумму выплат по депозиту на вклад:'))

    if S < 5000:
        p = 20
    elif 5000 <= S <10000:
        p = 22
    else:
        p = None
    print(p)

if __name__ == '__main__':
    if_elif()

# 2.Написать программу для определения времени суток по данному текущему времени и вывести сообщение
# (утро – с 6 до 12, день – с 12 до 18, вечер – с 18 до 24, ночь – с 0 до 6).

def curr_time():

    t = int(input('Введите время:'))

    if 6 <= t < 12:
        print('Утро')
    elif 12 <= t < 18:
        print('День')
    elif 18 <= t < 24:
        print('Вечер')
    elif 0 <= t < 6:
        print('Ночь')
    else:
        print('Повторите ввод')

if __name__ == '__main__':
    curr_time()


# решение той же задачи через словарь

h = float(input('Введите время:'))

d = {
     "утро": range(6, 12),   # диапазон
     "день": (12, 18),      # картеж
     "вечер": {
         "начало": 18,
         "конец": 24
     }
 }
if h in d["утро"]:
    print("утро")
elif d["день"][0] <= h < d["день"][1]:
     print("день")
elif d["вечер"]["начало"] <= h < d["вечер"]["конец"]:
    print("вечер")



# 3.Ввести с клавиатуры номер месяца. Определить сезон в зависимости от номера месяца и вывести сообщение
# (весна (3,4,5), лето (6,7,8), осень (9,10,11) зима (12,1,2)).

season = int(input('Введите число месяца:'))

if season == 3 or season == 4 or season == 5:
    print('Весна')
elif season == 6 or season == 7 or season == 8:
    print('Лето')
elif season == 9 or season == 10 or season == 11:
    print('Осень')
elif season == 12 or season == 1 or season == 2:
    print('Зима')
else:
    print('Введите заново номер месяца')

# другое решение задачи
months = int(input('Введите число месяца:'))
seasons = {
    "весна": (3, 4, 5),
    "лето": (6, 7, 8),
    "осень": (9, 10, 11),
    "зима": (12, 1, 2),
}
for season, month in seasons.items():
    if months in month:
        print(season)


# 4.Написать программу, которая в зависимости от характера ветра выдает сообщение о его скорости
# от 1до 4 м/с - слабый (1); от 5-10 м/c - умеренный (2); от 9-18 м/c - сильный (3);
# больше 19 м/c - ураганный (4).

v = float(input('Введите скорость ветра:'))

d = {
     "слабый": (1, 4),
     "умеренный": (5, 10),
     "сильный": (9, 18),
     "ураганный": v >= 19

 }
if d["слабый"][0] <= v < d["слабый"][1]:
    print("слабый")
elif d["умеренный"][0] <= v < d["умеренный"][1]:
     print("умеренный")
elif d["сильный"][0] <= h < d["сильный"][1]:
    print("сильный")
elif d["ураганный"][0] <= h < d["ураганный"][1]:
    print("ураганный")