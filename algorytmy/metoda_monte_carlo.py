# Metoda Monte Carlo obliczania wartości liczby PI
import random


bok = 2  # Bok kwadratu
promien = 1

n = 1000000  # Ilość punktów

ile_kolo = 0  # Ile punktów jest w kole

for i in range(n):
    # Losujemy nowy punkt
    x = (random.random() * 2) - 1
    y = (random.random() * 2) - 1
    if (x*x + y*y) <= 1:
        # Jeżeli punkt jest w kole
        ile_kolo += 1

pi = (4*ile_kolo) / n

print("n =", n)
print("PI ~=", pi)