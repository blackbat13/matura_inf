file = open("anagram.txt")

data = file.read().split("\n")

file.close()

#  print(data)

# Dla każdej linii/wiersza z pliku wejściowego
for line in data:
    # Tworzymy listę wyrazów z linii
    words = line.split(" ")
    length = len(words[0])  # Przyjmujemy długość pierwszego wyrazu jako "właściwą"
    ok = True  # Zakładamy, że wszystko jest ok - takie same długości wyrazów
    for w in words:  # Przechodzimy przez wszystkie wyrazy w linii i szukamy kontrprzykładu
        if len(w) != length:
            ok = False
            break  # opcjonalnie

    if ok:  # Jeżeli jest ok - wszystkie wyrazy mają taką samą długość w wierszu
        print(line)

