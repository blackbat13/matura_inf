# Otwieramy plik z danymi
file = open('dane4.txt')

# Wczytujemy wszystkie linijki z pliku
liczby = file.read().split("\n")

# Zamykamy plik wejściowy
file.close()

luki = []

for i in range(len(liczby) - 1):  # Przechodzimy od pierwszego do przedostatniego elementu włącznie
    liczba1 = int(liczby[i])
    liczba2 = int(liczby[i + 1])
    luka = abs(liczba2 - liczba1)
    luki.append(luka)

print("Minimum:", min(luki))
print("Maksimum:", max(luki))
