file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

dict_counter = dict()

for binary in binary_numbers:
    dict_counter[binary] = 1   # Przypisujemy dowolną wartość, żeby dodać liczbę do słownika

print(len(dict_counter))