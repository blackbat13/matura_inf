def to_decimal(binary):
    decimal = 0  # Wartość w systemie 10
    power = 1  # Potęga 2
    # Idziemy pętlą od końca
    for i in range(len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * power  # Przemnażamy cyfrę przez potęgę dwójki
        power *= 2  # Zwiększamy potęgę dwójki

    return decimal


file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

max_length = 1  # Długość najdłuższego podciągu rosnącego
max_first_index = 0  # Indeks pierwszej wartości w najdłuższym podciągu rosnącym

current_length = 1  # Długość obecnie obliczanego ciągu
current_first_index = 0  # Indeks pierwszej wartości w obecnie obliczanym ciągu

for index in range(1, len(binary_numbers)):
    # Porównujemy obecną wartość z poprzednią
    if to_decimal(binary_numbers[index]) > to_decimal(binary_numbers[index - 1]):
        current_length += 1
    else:
        current_length = 1
        current_first_index = index

    if current_length > max_length:
        max_length = current_length
        max_first_index = current_first_index

print("Długość:", max_length)
print("Indeks pierwszego el.:", max_first_index)
print("Indeks ostatniego el.:", max_first_index + max_length - 1)
max_last_index = max_first_index + max_length
print(binary_numbers[max_first_index:max_last_index])

