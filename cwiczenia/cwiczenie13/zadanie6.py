file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

min_dec = 10000000000000
min_bin = ""

max_dec = 0
max_bin = ""

for binary in binary_numbers:
    decimal = 0  # Wartość w systemie 10
    power = 1  # Potęga 2
    # Idziemy pętlą od końca
    for i in range(len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * power  # Przemnażamy cyfrę przez potęgę dwójki
        power *= 2  # Zwiększamy potęgę dwójki

    if decimal < min_dec:
        min_dec = decimal
        min_bin = binary

    if decimal > max_dec:
        max_dec = decimal
        max_bin = binary

print("Największa:", max_bin)
print("Najmniejsza:", min_bin)