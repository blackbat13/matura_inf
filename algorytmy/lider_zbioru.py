# Znajdowanie lidera zbioru
# Specyfikacja:
#  Dane:
#   n - ilosc elementow
#   tab[n] - tablica n liczb naturalnych
# Wynik:
#  lider - wartość lidera zbioru, lub -1 jeżeli nie istnieje


def szukaj_lidera(tab, n):
    kandydat = tab[0]
    ilosc = 1
    for i in range(1, n):
        if ilosc == 0:
            kandydat = tab[i]
            ilosc = 1
        else:
            if tab[i] == kandydat:
                ilosc += 1
            else:
                ilosc -= 1

    if ilosc != 0:
        ilosc = 0
        for el in tab:
            if kandydat == el:
                ilosc += 1

        if ilosc > n/2:
            return kandydat

    return -1


n = 10
tab = [2, 2, 5, 5, 5, 1, 3, 5, 5, 5]
lider = -1

lider = szukaj_lidera(tab, n)

if lider == -1:
    print("Brak lidera w zbiorze")
else:
    print("Lider zbioru:", lider)


# Przykład:
#  n = 10
#  tab = [5, 5, 1, 6, 5, 5, 7, 5, 5, 1]
#  lider = 5 (Wartość 5 występuje 6 razy)

# Przykład 2:
#  n = 10
#  tab = [1, 5, 1, 6, 5, 5, 7, 5, 5, 1]
#  lider = -1 (Najczęstsza wartość to 5, ale występuje 5 razy)


# Pomysł 1:
# Sortujemy listę elementów
# Bierzemy wartość środkowego elementu jako kandydat na lidera
# Przechodzimy przez wszystkie elmenty tablicy i sprawdzamy, ile razy ten kandydat występuje
# Sprawdzamy, czy występuje więcej niż n/2 razy

# Lista kroków/pseudokod
# 1. Posortuj tab
# 2. kandydat := tab[n//2]
# 3. ilosc_wystapien := 0
# 4. Dla i od 0 do n-1, wykonuj:
#   5. Jeżeli tab[i] == kandydat, to:
#     6. ilosc_wystapien := ilosc_wystapien + 1
# 7. Jeżeli ilosc_wystapien > n/2, to:
#    8. Wypisz kandydat
# 9. W przeciwnym przypadku:
#   10. Wypisz -1

# Analiza złożoności:
# 1. Posortuj tab - O(n log n)
# 2. kandydat := tab[n//2]   - 1 operacja
# 3. ilosc_wystapien := 0   - 1 operacja
# 4. Dla i od 0 do n-1, wykonuj: - O(n)
#   5. Jeżeli tab[i] == kandydat, to: - 1 operacja
#     6. ilosc_wystapien := ilosc_wystapien + 1  - 2 operacje
# 7. Jeżeli ilosc_wystapien > n/2, to:  - 1 operacja
#    8. Wypisz kandydat - 1 operacja
# 9. W przeciwnym przypadku: - 1 operacja
#   10. Wypisz -1 - 1 operacja

# Złożoność: O(n + n log n) ~ O(n log n)

# Algorytm optymalny
# 1. kandydat := tab[0]
# 2. ilosc := 1
# 3. Dla i = 1 do n-1, wykonuj:
#    4. Jeżeli ilosc == 0, to:
#       5. kandydat := tab[i]
#       6. ilosc := 1
#    7. w.p.p jeżeli tab[i] == kandydat:
#       8. ilosc := ilosc + 1
#    9. w.p.p jeżeli tab[i] != kandydat:
#       10. ilosc := ilosc - 1
# 11. Zliczamy ilość wystąpień kandydata w tablicy
# 12. Wypisujemy stosowny komunikat

# Złożoność: O(2n) ~ O(n)