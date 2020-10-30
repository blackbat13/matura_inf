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
    # print(num_text)

    # Tworzymy pustą listę do przechowania liczb
    num = []

    # Dla każdej wartości w num_text
    for n in num_text:
        # Konwertujemy tekst na liczbę
        number = int(n)

        #Dopisujemy liczbę do tablicy
        num.append(number)

    # num zawiera cały wiersz liczb z pliku
    # Dodajemy nowy wiersz do naszych danych
    pixels.append(num)

print(pixels)

# Wypisujemy piksel z 6 wiersza i 20 kolumny
print(pixels[5][19])

file.close()