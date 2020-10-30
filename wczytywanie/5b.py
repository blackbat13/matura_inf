# Plik wejściowy: 5.txt
# Każda linijka pliku zawiera dwie liczby

# Otwieramy plik
plik = open('5.txt')

# Wczytujemy zawartość pliku, dzieląc go na osobne linie
wyrazy_podwojne = plik.read().split("\n")

# Zamykamy plik
plik.close()

# wyrazy_podwojne - lista zawierająca wszystkie linijki z pliku wejściowego
print(wyrazy_podwojne)

wyrazy = []

for wp in wyrazy_podwojne:
    wyrazy.append(wp.split(" "))

print(wyrazy)

liczby = []

for wiersz in wyrazy:
    # Dodajemy pusty wiersz do listy liczb
    liczby.append([])

    # Dla każdego wyrazu w wierszu
    for w in wiersz:
        # Do ostatniego wiersza listy liczby dodajemy wyraz przetworzony na liczbę
        liczby[-1].append(int(w))

print(liczby)
