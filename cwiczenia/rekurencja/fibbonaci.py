def fib_rek(n):
    if n <= 2:
        return 1

    if n > 2:
        return fib_rek(n - 1) + fib_rek(n - 2)


def fib_iter(n):
    i = 3
    tab = [0, 1, 1]

    while i <= n:
        tab.append(tab[i-1] + tab[i-2])
        i += 1

    return tab[n]


number = int(input("Podaj liczbę: "))
result = fib_rek(number)
print("Wynik rekurencyjny:", result)
result2 = fib_iter(number)
print("Wynik iteracyjny:", result2)
