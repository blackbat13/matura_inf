# Algorytm Euklidesa obliczania NWD
# Specyfikacja:
#  Dane:
#    a, b - liczby całkowite, dodatnie
#  Wynik:
#    NWD(a,b) - największy wspólny dzielnik liczb a i b

# Wersja iteracyjna
# NWD_iter(a,b):
#  1. Dopóki b != 0, wykonuj:
#    2. nowe_a := b
#    3. nowe_b := a mod b
#    4. a := nowe_a
#    5. b := nowe_b
#  6. Zwróć a

def nwd_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Wersja rekurencyjna
# NWD_rek(a,b):
#  1. Jeżeli b == 0, to:
#    2. Zwróć a i zakończ
#  3. Zwróć NWD_rek(b, a mod b)


def nwd_rek(a, b):
    if b == 0:
        return a
    return nwd_rek(b, a % b)


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

wynik_iter = nwd_iter(a, b)
wynik_rek = nwd_rek(a, b)
print("Wynik iteracyjny:", wynik_iter)
print("Wynik rekurencyjny:", wynik_rek)