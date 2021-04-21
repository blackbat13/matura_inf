file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

max_length = 1  # Długość najdłuższego podciągu rosnącego
max_first_index = 0  # Indeks pierwszej wartości w najdłuższym podciągu rosnącym

current_length = 1  # Długość obecnie obliczanego ciągu
current_first_index = 0  # Indeks pierwszej wartości w obecnie obliczanym ciągu

for index in range(1, len(binary_numbers)):
    # Porównujemy obecną wartość z poprzednią
    if int(binary_numbers[index], 2) > int(binary_numbers[index - 1], 2):
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

