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