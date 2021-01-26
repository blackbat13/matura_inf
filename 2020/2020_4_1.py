# Otwieramy plik
file = open("pary.txt")

# Wczytujemy wszystkie linijki z pliku
lines = file.read().split("\n")

# Zamykamy plik
file.close()

# Tworzymy pustą listę do przechowywania danych
liczby = []

# Dla każdej linii w pliku wejściowym
for line in lines:
    # Dzielimy linię po znaku spacji, dostajemy listę wartości
    para = line.split(" ")

    # Przetwarzamy jako liczbę pierwszą wartość z pary
    liczba = int(para[0])

    # Dodajemy liczbę do listy liczb
    liczby.append(liczba)


# Rozwiązanie zadania
# 1. Dla każdej liczby, wykonuj:
#   2. Jeżeli liczba jest parzysta, to:
#      3. Dla i := 2 do naszej liczby, wykonuj:
#           4. Jeżeli i jest pierwsza, to:
#               5. b := liczba - i
#               6. Jeżeli b jest pierwsza, to:
#                  7. Wypisz liczba i b

# Sprawdzamy, czy liczba jest pierwsza
def czy_pierwsza(n):
    # Liczby mniejsze od 2 nie są pierwsze
    if n <= 1:
        return False

    # Sprawdzamy, czy n ma jakiś dzielnik różny od 1 i n
    for i in range(2, n):
        # Jeżeli liczba jest podzielna przez i, to nie jest pierwsza
        if n % i == 0:
            return False

    # Nie znaleźliśmy dzielnika, więc liczba jest pierwsza
    return True


for liczba in liczby:
    # Jeżeli liczba jest parzysta
    if liczba % 2 == 0:
        for i in range(2, liczba):
            # Jeżeli i jest liczbą pierwszą
            if czy_pierwsza(i):
                # Obliczamy drugi składnik sumy
                b = liczba - i
                # Jeżeli b jest pierwsza
                if czy_pierwsza(b):
                    print(liczba, i, b)
                    # Kończymy przetwarzanie danej liczby i idziemy do następnej
                    break