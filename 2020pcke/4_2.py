# Otwieramy plik z danymi
file = open('dane4.txt')

# Wczytujemy wszystkie linijki z pliku
liczby = file.read().split("\n")

# Zamykamy plik wejściowy
file.close()

maksimum_dlugosc = 2
maksimum_poczatek = 0

obecna_dlugosc = 2
obecna_poczatek = 0
obecna_luka = -1

for i in range(len(liczby) - 1):  #Przechodzimy od pierwszego do przedostatniego elementu włącznie
    liczba1 = int(liczby[i])
    liczba2 = int(liczby[i+1])
    luka = abs(liczba2 - liczba1)

    if luka == obecna_luka:
        obecna_dlugosc += 1
        if maksimum_dlugosc < obecna_dlugosc:
            maksimum_dlugosc = obecna_dlugosc
            maksimum_poczatek = obecna_poczatek
    else:
        obecna_luka = luka
        obecna_dlugosc = 2
        obecna_poczatek = i

print("Długość:", maksimum_dlugosc)
print("Początek:", liczby[maksimum_poczatek])
print("Koniec:", liczby[maksimum_poczatek + maksimum_dlugosc - 1])


