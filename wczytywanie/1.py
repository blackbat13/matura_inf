# Plik wejściowy: 1.txt
# Każda linijka pliku zawiera jeden wyraz - ciąg znaków

# Otwieramy plik
plik = open('1.txt')

# Wczytujemy zawartość pliku, dzieląc go na osobne linie
wyrazy = plik.read().split("\n")

# Zamykamy plik
plik.close()

# wyrazy - lista zawierająca wszystkie wyrazy z pliku wejściowego
print(wyrazy)

# Wypisujemy wszystkie wyrazy, linijka po linijce
for w in wyrazy:
    print(w)
