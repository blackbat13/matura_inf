# Plik wejściowy: 2.txt
# Każda linijka pliku zawiera jednbą liczbę całkowitą

# Otwieramy plik
plik = open('2.txt')

# Wczytujemy zawartość pliku, dzieląc go na osobne linie
liczby = list(map(int, plik.read().split("\n")))

# Zamykamy plik
plik.close()

print(liczby)

for l in liczby:
    print(l)