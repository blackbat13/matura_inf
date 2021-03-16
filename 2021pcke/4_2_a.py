plik = open("galerie_przyklad.txt")

dane = plik.read().split("\n")

plik.close()


for linia in dane:
    galeria = linia.split(" ")
    miasto = galeria[1]
    powierzchnia = 0
    ilosc_lokali = 0
    for i in range(2, len(galeria), 2):
        dlugosc = int(galeria[i])
        szerokosc = int(galeria[i+1])
        powierzchnia += dlugosc * szerokosc  # Dodajemy powierzchnię lokalu do sumy
        if dlugosc!=0 and szerokosc!=0:
            ilosc_lokali += 1

    print(miasto, powierzchnia, ilosc_lokali)
