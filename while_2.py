# •Возвести числа A в целую степень N

def pow_n(a, n):
    result = 1
    i = 0
    while i != n:
        result *= a
        i += 1
    print(result)

if __name__ == '__main__':
    pow_n(2, 5)



# •Является ли заданное натуральное число степенью двойки?

def is_pow_n(a, n=2):

    is_pow = False   # завели флаг, предположили ,что число не является степенью 2

    while True:
        over = a % n
        if over != 0:
            break
        a = a // n
        if a == 1:
            is_pow = True
            break

    return is_pow



if __name__ == '__main__':
    print(is_pow_n(32, n=2))

# •Ежемесячная стипендия студента составляет А грн., а расходы на проживание превышают ее и составляют B грн. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%. Определить, какую нужно иметь сумму денег, чтобы прожить учебный год
# (10 месяцев), используя только эти деньги и стипендию.

A = 1000
B = 2000

k = 0
s = 0
s_1 = A + B + B*0.03
while k != 10:
    s += s_1
    k += 1
print(s)




