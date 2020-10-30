# Otwieramy plik
file = open("sygnaly.txt")

# Wczytujemy wszystkie linijki z pliku
lines = file.read().split("\n")

# Początkowe maximum, jak najmniejsze
mx = 0
mx_line = ""

# Dla każdej linijki, wypisujemy ją
for l in lines:
    # Tworzymy unikalny zbiór liter z linii
    unique = set(l)
    # Wypisujemy linię i ilość unikalnych znaków
    print(l, len(unique))

    # Ilość unikalnych znaków w linii
    counter = len(unique)

    # Jeżeli nowa ilość unikalnych znaków jest większa od maksimum, to zmieniamy maksimum
    if counter > mx:
        mx = counter
        mx_line = l

    # print(l)
    # number - numer obecnej linii
    # Wykonujemy operacje na linii z pliku
    # l - zawiera linię z pliku, np. tekst "AZ"
    # print(l)
    # print(l[9]) - wypisanie 10 znaku tekstu

# Po wyjściu z pętli, wypisujemy maksimum
print(mx, mx_line)

# Zamykamy
file.close()
