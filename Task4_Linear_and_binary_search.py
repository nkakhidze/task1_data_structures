# Реализуйте:
# 1. Функцию линейного поиска
def linear_finder(n: int, listik: list):
    listik = sorted(listik)
    schtchk = 0
    for i in range(len(listik)):
        schtchk += 1
        if n == listik[i]:
            return f"linear_finder: число {n} было в вашем списке на позиции {i} при сортировке списка по возрастанию.\nЧисло было найдено с {schtchk} попытки"
        schtchk += 1

    return f"linear_finder: числа {n} не было в вашем списке"

# 2. Функцию бинарного поиска
def binar_finder(n: int, listik: list):
    schtchk = 0
    left = 0
    right = len(listik) - 1
    mid = (left + right) // 2
    while left < right:
        schtchk += 1
        if listik[mid] == n:
            return f"linear_finder: число {n} было в вашем списке на позиции {i} при сортировке списка по возрастанию.\nЧисло было найдено с {schtchk} попытки"




# 3. Сравните их производительность на отсортированном списке из 1000 элементов
# 4. Объясните, почему бинарный поиск работает быстрее


print("сортировке списка по возрастанию. \n Число было найдено с {schtchk} попытки")

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
print(binar_finder(17, a))
