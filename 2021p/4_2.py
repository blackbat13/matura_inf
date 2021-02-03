plik = open("znajomi_2.txt")

dane = plik.read().split("\n")

plik.close()

# Wczytujemy ilość znajomych z pierwszego wiersza
n = int(dane[0])

# Tworzymy listę w której zliczamy, ile osób zna daną osobę
# Na początku lista jest wypełniona zerami
ile_zna = []
for i in range(0, n):
    ile_zna.append(0)

for i in range(1, len(dane)):
    # Bierzemy tekstową listę znajomych z i-tego wiersza
    znajomi_txt = dane[i]
    # Dzielimy tekst znajomych po spacji na listę
    znajomi_lista = znajomi_txt.split(" ")
    for j in range(1, len(znajomi_lista)):
        # Bierzemy kolejnego znajomego z listy
        # Przetwarzamy tekst na liczbę
        znajomy = int(znajomi_lista[j])

        # Zwiększamy licznik przypisany do tego znajomego
        ile_zna[znajomy] += 1

# for i in range(0, n):
#     print("Osobę", i, "zna", ile_zna[i], "osób")

# Wypisanie wyniku
for i in range(0, n):
    # Jeżeli osobę o numerze i zna zero osób, to ją wypisz
    if ile_zna[i] == 0:
        print(i)
