# Реализуйте:
# 1. Пузырьковую сортировку

def sort_bubbling(massiv:list):
    for iteraczia in range(len(massiv)-1):
        schtchk = 0
        i0 = 0
        i1 = 1
        for i in range(len(massiv)-1 - iteraczia):
            if massiv[i0] > massiv[i1]:
                massiv[i0], massiv[i1] = massiv[i1], massiv[i0]
                schtchk += 1
            i0 += 1
            i1 += 1
        if schtchk == 0:
            return massiv
    return massiv



# 2. Сортировку вставками
# 3. Сравните их с встроенной функцией sorted()
# 4. Измерьте время выполнения для разных размеров входных данных

a = [1, 0, 2, 5, 0, 12]
print(sort_bubbling(a))