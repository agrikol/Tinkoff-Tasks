s, x = [], 0 # Переменные: список, накопитель max
for i in range(int(input('Введите количество запросов: '))):
    a = int(input())
    if a not in s: # Проверка на множество (class 'set' не использован из-за свойства неупорядоченности)
        s.append(a)
    if len(s) > 1:
        for j in range(len(s)): # Цикл для поиска max xor
            for h in range(1, len(s)):
                if s[j] ^ s[h] >= x:
                    x = s[j] ^ s[h]
        print(x) # Вывод xor
    else:
        print(0)