tab = [5, 9, 10, 4, 2, 1]
#  Znajdowanie maksimum
m = max(tab)
# print(m)

# Znajdowanie indeksu wartości maksymalnej
ind = max(range(len(tab)), key=lambda i: tab[i])
print("Indeks:", ind, "Wartość:", tab[ind])

# Funkcja w jednej linijce - lambda
suma = lambda a, b: a + b
print("Suma:", suma(3, 5))

# Sortowanie słownika po wartościach, same klucze
sl = {"a": 10, "b": 3, "c": 5}
posortowane = sorted(sl.keys(), key=lambda el: sl[el])
print(posortowane)

# Sortowanie słownika po wartościach, pary (klucz, wartość)
posortowane = sorted(sl.items(), key=lambda el: el[1])
print(posortowane)

# Sortowanie słownika po wartościach bezwzględnych, pary (klucz, wartość)
sl = {"a": -10, "b": 3, "c": 5}
posortowane = sorted(sl.items(), key=lambda el: abs(el[1]))
print(posortowane)

# Sortowanie słownika po wartościach bezwzględnych, pary (klucz, wartość), odwrócony porządek
sl = {"a": -10, "b": 3, "c": 5}
posortowane = sorted(sl.items(), key=lambda el: abs(el[1]), reverse=True)
print(posortowane)

# Unikalne wartości z listy
tab = [5, 3, 2, 6, 7, 2, 3, 3, 1, 1, 3, 3]
s = set(tab)
tab = list(s)
print("Unikalne:", tab)

# łączenie ze sobą tekstów
teksty = ["ab", "cd", "efg"]
txt = "".join(teksty)
print("Połączony tekst:", txt)

txt = "-".join(teksty)
print("Połączony tekst z myślnikami:", txt)

# Zamiana wartości miejscami
a = 10
b = 5
a, b = b, a
print("a =", a, "b =", b)

# Szybka zamiana z binarnego na dziesiętne całej listy
binarne = ["101", "100", "1000", "1010"]
dziesietne = list(map(lambda el: int(el, 2), binarne))
print("Dziesietne:", dziesietne)

# Szybkie operacje arytmetyczne na elementach listy
tab = [1, 2, 3, 4, 5, 6]
potegi_dwojki = list(map(lambda el: 2 ** el, tab))
print("Potęgi dwójki:", potegi_dwojki)


# Szybkie filtrowanie listy - chcemy tylko wartości parzyste
def jest_parzysta(x):
    if x % 2 == 0:
        return True
    else:
        return False
    # return x % 2 == 0


tab = [2, 5, 7, 2, 34, 8, 10, 2, 17, 13]
parzyste = list(filter(jest_parzysta, tab))
print("Parzyste:", parzyste)

parzyste = list(filter(lambda x: x % 2 == 0, tab))
print("Parzyste:", parzyste)

# Filtrowanie - zostawiamy tylko liczby binarne podzielne przez 10
binarne = ["101", "100", "1000", "1010"]
podzielne = list(filter(lambda b: int(b, 2) % 10 == 0, binarne))
print("Binarne podzielne przez 10:", podzielne)

# Filtrowanie - zostawiamy tylko liczby binarne podzielne przez 2
binarne = ["101", "100", "1000", "1010"]
podzielne = list(filter(lambda b: b[-1] == "0", binarne))
print("Binarne podzielne przez 2:", podzielne)

# Suma wartości listy
tab = [1, 2, 3, 4, 5]
suma = sum(tab)
print("Suma:", suma)

# Wypisanie wszystkich "funkcji" dostępnych dla danego elementu/typu/biblioteki
print(dir(tab))

import math
print(dir(math))

# Wyrażenia regularne - dopasowywanie do wzorca
import re

tekst = "anastazja"
pasuje = re.match(".*a", tekst)
if pasuje is None:
    print(tekst, "Nie pasuje")
else:
    print(tekst, "Pasuje")

tekst = "bob"
pasuje = re.match(".*a", tekst)
if pasuje is None:
    print(tekst, "Nie pasuje")
else:
    print(tekst, "Pasuje")


# Filtrowanie + wyrażenia regularne - zostawiamy tylko liczby binarne podzielne przez 4 (czyli z "00" na końcu)
binarne = ["101", "100", "1000", "1010"]
podzielne = list(filter(lambda b: re.match(".*00", b), binarne))
print("Binarne podzielne przez 4:", podzielne)

# Filtrowanie + wyrażenia regularne - zostawiamy tylko liczby binarne które mają 1 w środku (nie tylko na początku)
binarne = ["101", "100", "1000", "1010"]
jedynka = list(filter(lambda b: re.match("1.*1.*", b), binarne))
print("Binarne z jedynką w środku:", jedynka)

# Filtrowanie + wyrażenia regularne - zostawiamy tylko liczby binarne które mają dwie 1 w środku (nie tylko na początku)
binarne = ["101", "100", "10101", "1010", "10110"]
jedynka = list(filter(lambda b: re.match("1.*1.*1.*", b), binarne))
print("Binarne z dwiema jedynkami w środku:", jedynka)
