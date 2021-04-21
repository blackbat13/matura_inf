file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

count = 0

for binary in binary_numbers:
    digit_counter = dict()  # Słownik do zliczania cyfr 0 i 1
    digit_counter["0"] = 0  # Inicjalizujemy liczniki zer i jedynek
    digit_counter["1"] = 0
    for digit in binary:  # Dla każdej cyfry w zapisie liczby binarnej
        digit_counter[digit] += 1   # Zwiększamy licznik dla danej cyfry

    if digit_counter["0"] > digit_counter["1"]:
        count += 1

print(count)