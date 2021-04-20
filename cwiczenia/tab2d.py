
tab2d = [[1, 2, 3], [4, 5, 6], [20, 8, 9]]
n = 3

# Zadanie 1
# Policz w pętli sumę elementów na głównej przekątnej
suma = 0
i = 0
while n > i:
    suma = tab2d[i][i] + suma
    i = i + 1

print(suma)

# Zadanie 2
# Policz w pętli sumę elemnetów na drugiej przekątnej
suma = 0
i = 0
j = n-1
while n > i:
    suma = tab2d[j][i] + suma
    i = i + 1
    j = j - 1

print(suma)