a = list(map(int,input("Введите элементы через пробел: ").split()))
min_value = a[0]
min_index = 0
for i in range(1,len(a)):
    if a[i]<min_value:
        min_value = a[i]
        min_index = i
print("Минимальное значение: ", min_value)
print("Индекс минимального значения: ", min_index)
