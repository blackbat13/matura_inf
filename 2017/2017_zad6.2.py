# Otwieramy plik
file = open("przyklad.txt")

# Wczytujemy wszystkie linijki z pliku
lines = file.read().split("\n")

# Tworzymy pustą listę do przechowywania danych
pixels = []

# Przechodzimy linia po lini
for l in lines:
    # Twrozymy listę liczb jako tekst
    num_text = l.split(" ")

    # Używamy funkcji map do konwersji tekstu na liczby i całość konwertujemy na listę
    num = list(map(int, num_text))

    # Do dwuwymiarowej listy pikseli dopisujemy kolejny wiersz
    pixels.append(num)

# print(pixels)

# Wypisujemy piksel z 6 wiersza i 20 kolumny
# print(pixels[5][19])

file.close()

# Zliczamy, ile wierszy trzeba usunąć
remove_count = 0

for row in pixels:
    row2 = list(reversed(row))
    if row != row2:
        remove_count += 1

print(remove_count)