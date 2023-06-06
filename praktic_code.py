import numpy as np

# запрашиваем у пользователя размерность матрицы
n = int(input("Введите размерность квадратной матрицы: "))

# запрашиваем у пользователя элементы матрицы
a = []
print("Введите элементы матрицы:")
for i in range(n):
    row = []
    for j in range(n):
        elem = float(input(f"Элемент [{i}, {j}]: "))
        row.append(elem)
    a.append(row)

# выводим исходную матрицу
print("Исходная матрица A:\n", np.array(a))

# вычисляем обратную матрицу
a_inv = np.linalg.inv(a)

# выводим результаты
print("Обратная матрица A:\n", a_inv)