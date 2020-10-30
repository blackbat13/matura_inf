# Plik wejściowy: 3.txt
# Każda linijka pliku zawiera jednbą liczbę rzeczywistą

# Otwieramy plik
plik = open('3.txt')

# Wczytujemy zawartość pliku, dzieląc go na osobne linie
wyrazy = plik.read().split("\n")

# Zamykamy plik
plik.close()

# Tworzymy pustą listę liczb
liczby = []

for w in wyrazy:
    # Dopisujemy do listy liczb kolejne wartości z pliku przetworzone na liczbę rzeczywistą
    liczby.append(float(w))

print(liczby)

for l in liczby:
    print(l)