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
print(table)