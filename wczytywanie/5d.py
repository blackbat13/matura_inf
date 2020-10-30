# Plik wejściowy: 5.txt
# Każda linijka pliku zawiera dwie liczby

# Otwieramy plik
plik = open('5.txt')

# Wczytujemy zawartość pliku, dzieląc go na osobne linie
liczby = list(map(int, plik.read().split()))

# Zamykamy plik
plik.close()

print(liczby)

for l in liczby:
    print(l)



