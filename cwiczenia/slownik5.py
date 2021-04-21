# Znajdowanie w słowniku klucza z największą wartością

slownik = dict()
slownik["a"] = 50
slownik["b"] = 31
slownik["c"] = 68

max_wartosc = 0
max_litera = ""

for litera in slownik:
    if slownik[litera] > max_wartosc:
        max_wartosc = slownik[litera]
        max_litera = litera

print(max_litera, max_wartosc)
