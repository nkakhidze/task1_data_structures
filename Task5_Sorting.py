# Реализуйте:
# 1. Пузырьковую сортировку
def sort_bubbling(massiv:list):
    for iteraczia in range(len(massiv)-1):
        schtchk = 0
        for i in range(len(massiv) - 1 - iteraczia):
            if massiv[i] > massiv[i + 1]:
                massiv[i], massiv[i + 1] = massiv[i + 1], massiv[i]
                schtchk += 1
            i+= 1
        if schtchk == 0:
            return massiv
    return massiv



# 2. Сортировку вставками
def sort_pasting(massiv:list):
    for i in range(1, len(massiv)):
        while (massiv[i] < massiv[i - 1]) and (i > 0):
            massiv[i - 1], massiv[i] = massiv[i], massiv[i - 1]
            i -= 1
    return massiv





# 3. Сравните их с встроенной функцией sorted()
# 4. Измерьте время выполнения для разных размеров входных данных

a = [1, 0, 24, 2, 5, 0, 12]
print(sort_pasting(a))