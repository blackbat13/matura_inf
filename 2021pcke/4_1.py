plik = open("galerie_przyklad.txt")

dane = plik.read().split("\n")

plik.close()

# Tworzymy pusty słownik
wynik = dict()

for linia in dane:
    galeria = linia.split(" ")
    kod = galeria[0]

    # Jeżeli kod państwa jest już w wyniku
    if kod in wynik:
        wynik[kod] += 1  # To zwiększamy licznik wystąpień dla tego kodu o1
    else:
        wynik[kod] = 1  # A jeżeli nie, to inicjalizujemy nowy licznik

for kod in wynik:
    print(kod, wynik[kod])

# Gdyby była potrzeba posortowania po kodzie (kluczu)
# for kod in sorted(wynik):
#     print(kod, wynik[kod])