file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

# Pomysł: Zamieniamy liczbę na system 10 i sprawdzamy podzielność przez 10 za pomocą modulo
# Liczymy, ile jest takich liczb

count = 0  # Licznik liczb parzystych

for binary in binary_numbers:
    decimal = 0  # Wartość w systemie 10
    power = 1  # Potęga 2
    # Idziemy pętlą od końca
    for i in range(len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * power  # Przemnażamy cyfrę przez potęgę dwójki
        power *= 2  # Zwiększamy potęgę dwójki

    if decimal % 10 == 0:
        count += 1

print(count)