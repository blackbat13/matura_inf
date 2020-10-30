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

liczby = []

for wp in wyrazy_podwojne:
    liczby.append(list(map(int, wp.split(" "))))

print(liczby)



