# Plik wejściowy: 3.txt
# Każda linijka pliku zawiera jednbą liczbę rzeczywistą

# Otwieramy plik
plik = open('3.txt')

# Wczytujemy zawartość pliku, dzieląc go na osobne linie
liczby = list(map(float, plik.read().split("\n")))

# Zamykamy plik
plik.close()

print(liczby)

for l in liczby:
    print(l)