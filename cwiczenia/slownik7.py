# Znajdowanie w słowniku klucza z największą wartością

slownik = dict()
slownik["a"] = 50
slownik["b"] = 68
slownik["c"] = 31

max_litera = max(slownik, key=slownik.get)
max_wartosc = slownik[max_litera]

print(max_litera, max_wartosc)
