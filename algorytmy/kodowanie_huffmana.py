# Kodowanie Huffmana
# Specyfikacja:
#  Dane:
#   tekst - ciąg małych liter
#  Wynik:
#   Kody każdej z liter występującej w tekście
#   Zakodowany tekst wejściowy
#   Stopień kompresji

# Ogólny schemat algorytmu:
# 1. Tworzymy pary: (znak, ilość wystąpień)
# 2. Budujemy drzewko kodowania: zaczynamy od łączenia najrzadziej występujących znaków
# 3. Odczytujemy kody z drzewa: idąc w lewo przypisujemy 0, idąc w prawo przypisujemy 1
# 4. Wykorzystujemy kody do zakodowania tekstu

class Wezel:
    znak = ""
    czestosc = 0
    lewy = None
    prawy = None

    def __init__(self, znak, czestosc, lewy, prawy):
        self.znak = znak
        self.czestosc = czestosc
        self.lewy = lewy
        self.prawy = prawy

    def wypisz(self, kod):
        if self.lewy is None:
            print(self.znak, kod)
            return

        self.lewy.wypisz(kod + "0")
        self.prawy.wypisz(kod + "1")


def sort_wezel(wezel):
    return wezel.czestosc

tekst = "aaaabbaabbaaacccaaaabbaaaaccdddaaaaaaeee"

czestosci = dict()

for znak in tekst:
    # Jeżeli znak jest już w słowniku
    if znak in czestosci:
        czestosci[znak] += 1
    else:
        czestosci[znak] = 1

# Lista do przechowywania węzłów drzewa
elementy = []

for znak in czestosci:
    w = Wezel(znak, czestosci[znak], None, None)
    elementy.append(w)

elementy.sort(key=sort_wezel)

# for el in elementy:
#     print(el.znak, el.czestosc)

while len(elementy) > 1:
    w1 = elementy[0]
    w2 = elementy[1]
    # Usuwamy dwa pierwsze elementy
    elementy.pop(0)
    elementy.pop(0)
    w3 = Wezel("", w1.czestosc + w2.czestosc, w2, w1)
    elementy.append(w3)
    elementy.sort(key=sort_wezel)

korzen = elementy[0]
korzen.wypisz("")