plik = open("galerie_przyklad.txt")

dane = plik.read().split("\n")

plik.close()

for linia in dane:
    galeria = linia.split(" ")
    miasto = galeria[1]

    unikalne_lokale = set()

    for i in range(2, len(galeria), 2):
        dlugosc = int(galeria[i])
        szerokosc = int(galeria[i + 1])
        if dlugosc != 0 and szerokosc != 0:  # Jeżeli lokal istnieje
            unikalne_lokale.add(dlugosc * szerokosc)

    print(miasto, len(unikalne_lokale))
