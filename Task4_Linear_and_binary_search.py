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
    print("первое среднее значение", mid,listik[mid]) #1

    while left < right:
        mid = (left + right) // 2
        print('это mid', mid,listik[mid])
        schtchk += 1
        if listik[mid] == n:
            return f"binar_finder: число {n} было в вашем списке на позиции {mid} при сортировке списка по возрастанию.\nЧисло было найдено с {schtchk} попытки"
        if listik[mid] > n:
            right = mid
            print("new right",right)
            print('при новом right значение', listik[right])
        else:
            left = mid
            print("new left", left)
            print('при новом left значение', listik[left])





# 3. Сравните их производительность на отсортированном списке из 1000 элементов
# 4. Объясните, почему бинарный поиск работает быстрее


a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binar_finder(4, a))
