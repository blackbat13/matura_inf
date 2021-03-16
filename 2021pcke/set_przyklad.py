plik = open("galerie_przyklad.txt")

dane = plik.read().split("\n")

plik.close()

unikalne_miasta = set()

for linia in dane:
    galeria = linia.split(" ")
    miasto = galeria[1]
    unikalne_miasta.add(miasto)  # Dodajemy miasto do zbioru

for unik_miasto in unikalne_miasta:
    licznik = 0
    for linia in dane:
        galeria = linia.split(" ")
        miasto = galeria[1]
        if miasto == unik_miasto:
            licznik += 1
    print(unik_miasto, licznik)