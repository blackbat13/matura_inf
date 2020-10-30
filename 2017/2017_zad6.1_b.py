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

min = 255
max = 0

# Dla każdego wiersza
for row in pixels:
    # Dla każdej wartości w wierszu
    for val in row:
        # val - zawiera poszczególne wartości pikseli
        if val > max:
            max = val
        if val < min:
            min = val

print("Max:", max)
print("Min:", min)

# Przechodzimy przez numer wiersza
for i in range(200):
    # Przechodzimy przez numer kolumny
    for j in range(320):
        pix = pixels[i][j]
        
