#2
A = 5
B = 10
cond_1 = (A %2 > 0)
cond_2 = (B % 2 ==1)
print (cond_1 and cond_2)


#3
A: int = 5
B = 10
C = 50
cond_1 = (A < 45) and (B >= 45) and (C >= 45)
cond_2 = (B < 45) and (A >= 45) and (C >= 45)
cond_3 = (C < 45) and (A >= 45) and (B >= 45)

print (cond_1 or cond_2 or cond_3)


#4
A = 10
cond_1 = A % 3 != 0
cond_2  = A % 3 > 0
cond_3 = A % 10 == 0
print (cond_1 and cond_2 and cond_3)

#5
A = 20
cond_1 = -10 < A < -1
cond_2 = 2 < A < 15

print (not (cond_1 or cond_2 ))

#6




