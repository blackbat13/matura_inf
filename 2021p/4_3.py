plik = open("znajomi_2.txt")

dane = plik.read().split("\n")

plik.close()

# Wczytujemy ilość znajomych z pierwszego wiersza
n = int(dane[0])

# Tworzymy pustą listę, w której będziemy zapisywać listy znajomych
znajomi = []

for i in range(1, len(dane)):
    # Bierzemy tekstową listę znajomych z i-tego wiersza
    znajomi_txt = dane[i]
    # Dzielimy tekst znajomych po spacji na listę
    znajomi_lista = znajomi_txt.split(" ")

    # Zapamiętujemy obecnych znajomych
    obecni_znajomi = []
    for j in range(1, len(znajomi_lista)):
        zn = int(znajomi_lista[j])
        obecni_znajomi.append(zn)

    znajomi.append(obecni_znajomi)

for i in range(0, n):
    print("Znajomi osoby", i, ":", znajomi[i])

print("")
print("Pary znajomych:")
# Dla każdego znajomego
for i in range(0, n):
    # i - numer obecnego znajomego
    # Dla każdej osoby, którą zna osoba i
    for j in range(0, len(znajomi[i])):
        # zn - kolejna osoba, którą zna i
        zn = znajomi[i][j]

        # Teraz sprawdzamy, czy zn także zna i
        # Zakładamy, że nie zna
        ok = False

        # Przechodzimy przez kolejnych znajomych zn
        for k in range(0, len(znajomi[zn])):
            # nowy_zn - kolejna osoba, którą zna zn
            nowy_zn = znajomi[zn][k]

            # Sprawdzamy, czy któryś ze znajomych to i
            if nowy_zn == i:
                # Jeżeli tak, to zapamiętujemy to
                ok = True

        # Jak już przeszliśmy przez wszystkich znajomych zn
        # Jeżeli znaleźliśmy i na liście znajomych zn
        if ok:
            # Wypisujemy parę znajomych: i zn
            # Wypisujemy parę tylko wtedy, gdy jest w kolejności rosnącej
            if zn > i:
                print(i, zn)

