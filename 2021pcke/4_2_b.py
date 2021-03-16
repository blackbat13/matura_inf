plik = open("galerie_przyklad.txt")

dane = plik.read().split("\n")

plik.close()

max_miasto = ""
max_powierzchnia = 0

min_miasto = ""
min_powierzchnia = 99999999999999

for linia in dane:
    galeria = linia.split(" ")
    miasto = galeria[1]
    powierzchnia = 0
    ilosc_lokali = 0
    for i in range(2, len(galeria), 2):
        dlugosc = int(galeria[i])
        szerokosc = int(galeria[i + 1])
        powierzchnia += dlugosc * szerokosc  # Dodajemy powierzchnię lokalu do sumy
        if dlugosc != 0 and szerokosc != 0:
            ilosc_lokali += 1

    if powierzchnia > max_powierzchnia:
        max_powierzchnia = powierzchnia
        max_miasto = miasto

    if powierzchnia < min_powierzchnia:
        min_powierzchnia = powierzchnia
        min_miasto = miasto

print(max_miasto, max_powierzchnia)
print(min_miasto, min_powierzchnia)
