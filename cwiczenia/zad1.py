# Napisz program, który wczyta liczby z pliku in.txt,
# a następnie obliczy i wypisze ich minimum, maksimum, średnią i sumę.

# Otwieramy plik
file = open("in.txt")

# Wczytujemy wszystkie linie z pliku
lines = file.read().split("\n")

maks = 1
min = 1000
suma = 0
srednia = 0

# Przechodzimy przez wszystkie linie z pliku
for l in lines:
    # Zamieniamy na liczbę
    # int - całkowite
    # float - rzeczywiste
    number = int(l)
    if number > maks:
        maks = number

    if number < min:
        min = number

    suma = number + suma

srednia = suma / 500
print("Minimum wynosi:", min)
print("Maksimum wynosi:", maks)
print("Suma wynosi:", suma)
print("Średnia wynosi:", srednia)

# Zamykamy plik
file.close()