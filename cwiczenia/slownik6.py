# Znajdowanie w słowniku klucza z największą wartością

slownik = dict()
slownik["a"] = 50
slownik["b"] = 68
slownik["c"] = 31

posortowane = sorted(slownik, key=slownik.get)
max_litera = posortowane[-1]
max_wartosc = slownik[max_litera]

print(max_litera, max_wartosc)
