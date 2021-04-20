def silnia_rek(n):
    if n == 1:
        return 1
    if n > 1:
        return n * silnia_rek(n-1)


def silnia_iter(n):
    if n == 1:
        return 1
    m = 1
    i = 1
    while n > i:
        m = m * i
        i = i + 1

    return m * n


number = int(input("Podaj liczbę: "))
result1 = silnia_rek(number)
result2 = silnia_iter(number)
print("Wynik rekurencyjny:", result1)
print("Wynik iteracyjny:", result2)
