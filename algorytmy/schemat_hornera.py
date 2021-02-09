# Schemat Hornera
# Krótki opis: http://www.algorytm.edu.pl/algorytmy-maturalne/schemat-hornera.html

# Specyfikacja:
#  Dane:
#   n - stopień wielomianu, liczba naturalna, > 0
#   a_n, a_n-1, a_n-2, ..., a_1, a_0 - współczynniki wielomianu, liczby rzeczywiste
#        Podane w kolejności malejącej, od współczynnika przy najwyższej potędze
#   x - liczba rzeczywista
#  Wynik:
#   Wartość wielomianu

# Pseudokod/lista kroków:
# 1. Wczytujemy dane, współczynniki wczytujemy do listy wsp
# 2. wynik := wsp[0]
# 3. Dla każdego i od 1 do n, wykonuj:
#    4. wynik := wynik * x + wsp[i]
# 5. Wypisz wynik


n = int(input("Podaj stopień wielomianu: "))
x = float(input("Podaj x: "))

wsp = []
for i in range(n, -1, -1):
    # Wczytujemy kolejny współczynnik
    a = float(input("Podaj współczynnik przy potędze " + str(i)))
    # Dopisujemy go do listy współczynników
    wsp.append(a)

wynik = wsp[0]
for i in range(1, n+1):
    wynik = wynik * x + wsp[i]

print("Wartość wielomianu:", wynik)