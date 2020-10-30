# Plik wejściowy: 4.txt
# Każda linijka pliku zawiera dwa wyrazy - ciąg znaków

# Otwieramy plik
plik = open('4.txt')

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

for wiersz in wyrazy:
    print(wiersz[0], wiersz[1])

# Wypisujemy drugi wyraz z trzeciego wiersza:
# print(wyrazy[2][1])