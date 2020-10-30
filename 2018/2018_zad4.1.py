# Otwieramy plik
file = open("sygnaly.txt")

# Wczytujemy wszystkie linijki z pliku
lines = file.read().split("\n")

number = 0
# Dla każdej linijki, wypisujemy ją
for l in lines:
    number += 1
    if number % 40 == 0:
        print(l[9])
    # number - numer obecnej linii
    # Wykonujemy operacje na linii z pliku
    # l - zawiera linię z pliku, np. tekst "AZ"
    # print(l)
    # print(l[9]) - wypisanie 10 znaku tekstu

# Zamykamy
file.close()
