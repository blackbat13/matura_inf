# Napisz program, który wczyta liczby z pliku in.txt,
# posortuje je rosnąco i zapisze do pliku out2.txt.

# Otwieramy plik
file = open("in.txt")

# Wczytujemy wszystkie linie z pliku
lines = file.read().split("\n")

liczby = []

# Przechodzimy przez wszystkie linie z pliku
for l in lines:
    # Zamieniamy na liczbę
    # int - całkowite
    # float - rzeczywiste
    number = int(l)

    # Dopisujemy liczbę do listy
    liczby.append(number)

# liczby - lista zawierająca liczby z pliku
posortowana = sorted(liczby, reverse=True)
print(posortowana)

file_out = open("out.txt", "w")
for l in posortowana:
    # Zamieniamy liczbę na tekst poleceniem str i zapisujemy do pliku
    file_out.write(str(l))
    # Zapisujemy znak nowej linii do pliku
    file_out.write("\n")

# Zamykamy pliki
file.close()
file_out.close()