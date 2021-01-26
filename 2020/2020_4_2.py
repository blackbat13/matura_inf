# Otwieramy plik
file = open("pary.txt")

# Wczytujemy wszystkie linijki z pliku
lines = file.read().split("\n")

# Zamykamy plik
file.close()

# Tworzymy pustą listę do przechowywania danych
wyrazy = []

# Dla każdej linii w pliku wejściowym
for line in lines:
    # Dzielimy linię po znaku spacji, dostajemy listę wartości
    para = line.split(" ")

    # Przetwarzamy jako liczbę pierwszą wartość z pary
    tekst = para[1]

    # Dodajemy liczbę do listy liczb
    wyrazy.append(tekst)