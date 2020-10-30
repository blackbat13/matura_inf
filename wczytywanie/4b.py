# Plik wejściowy: 4.txt
# Każda linijka pliku zawiera dwa wyrazy - ciąg znaków

# Otwieramy plik
plik = open('4.txt')

# Wczytujemy zawartość pliku, dzieląc go na osobne linie
wyrazy = plik.read().split()

# Zamykamy plik
plik.close()

# wyrazy - lista zawierająca wszystkie wyrazy z pliku wejściowego
print(wyrazy)