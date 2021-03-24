# Otwieramy plik z danymi
file = open('dane4.txt')

# Wczytujemy wszystkie linijki z pliku
liczby = file.read().split("\n")

# Zamykamy plik wejściowy
file.close()

minimum = 9999999999
maksimum = 0

for i in range(len(liczby) - 1):  #Przechodzimy od pierwszego do przedostatniego elementu włącznie
    liczba1 = int(liczby[i])
    liczba2 = int(liczby[i+1])
    luka = liczba2 - liczba1
    if luka < 0:
        luka *= -1

    if luka < minimum:
        minimum = luka

    if luka > maksimum:
        maksimum = luka

print("Minimum:", minimum)
print("Maksimum:", maksimum)