from math import gcd  # Импорт функции НОД
from math import prod  # Импорт функции произведения итерируемых

n, s, m = int(input()), [], []  # Переменные: n, список "a + b = n", список для НОК,
for a in range(1, n):  # Вложенный цикл для определения и внесения возможных "n = a + b"
    for b in range(1, n):
        if a + b == n:
            s.append([])
            s[a - 1].append(a)
            s[a - 1].append(b)

for i in range(len(s)):  # Цикл, определяющий НОК
    m.append([])
    m[i] = prod(s[i]) / gcd(s[i][0], s[i][1])
print(*s[m.index(min(m))])  # По индексу списка m находим нужный нам минимальный НОК в списке s
