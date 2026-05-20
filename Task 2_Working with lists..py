# Задание 2: Работа со списками.
# Создайте программу, которая:
# 1. Создает список из 10 чисел
import random
import time

def rand_10x():
    a = []
    for i in range(10):
        a.append(random.randint(0,100))
    return a

a = rand_10x()

# 2. Находит максимальное и минимальное значение
a_min = min(a)
a_max = max(a)

# 3. Сортирует список двумя разными способами
sorted_fast_time_start = time.perf_counter()
print(sorted_fast_time_start)
a_sorted_fast = sorted(a)
sorted_fast_time_stop = time.perf_counter()
print(sorted_fast_time_stop)
print((sorted_fast_time_stop - sorted_fast_time_start) * 1000)


b = [9, 1, 5, 10]

for i in range(len(b)):
    print('i =', b[i])
    for j in range(1, len(b)):
        if b[i] > b[j]:
            b[i], b[j] = b[j], b[i]
        print('j =', b[j], end=' ')
    print()

print(b)


# 4. Измеряет время выполнения каждой операции сортировки
