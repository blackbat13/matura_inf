# Otwieramy plik z danymi
file = open('dane4.txt')

# Wczytujemy wszystkie linijki z pliku
liczby = file.read().split("\n")

# Zamykamy plik wejściowy
file.close()

krotnosci = dict()

for i in range(len(liczby) - 1):  #Przechodzimy od pierwszego do przedostatniego elementu włącznie
    liczba1 = int(liczby[i])
    liczba2 = int(liczby[i+1])
    luka = abs(liczba2 - liczba1)
    if luka in krotnosci:
        krotnosci[luka] += 1
    else:
        krotnosci[luka] = 1


maksimum = 0
for luka in krotnosci:
    if krotnosci[luka] > maksimum:
        maksimum = krotnosci[luka]

print("Maksimum:", maksimum)

for luka in krotnosci:
    if krotnosci[luka] == maksimum:
        print(luka)