
# Funkcja sprawdzajaca dla liczby n, czy jest ona liczba pierwsza
def is_prime(n):
    licznik = 0
    for liczba in range(2, n):
        if n % liczba == 0:
            licznik += 1
    if licznik == 0:
        return True # Liczba jest pierwsza
    else:
        return False # Liczba nie jest pierwsza


file = open("NAPIS.TXT")

words = file.read().split("\n")

file.close()

print(ord("A") + ord("B") + ord("B"))

wynik = 0
suma = 0
for w in words:
    suma = 0
    for znak in w:
        suma = suma + ord(znak)

    if is_prime(suma) == True:
        print(suma)
        wynik += 1

print("Wynik:", wynik)


# ABC: B>A, C>B
