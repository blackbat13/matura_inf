file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

set_counter = set()  # Zbiór unikalnych wartości

for binary in binary_numbers:
    set_counter.add(binary)  # Dodajemy liczbę binarną do zbioru

print(len(set_counter))