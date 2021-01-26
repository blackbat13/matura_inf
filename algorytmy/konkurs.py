import random

wygrane = 0
n = 10

for i in range(n):
    nagroda = random.randint(1, 3)

    wybor = int(input("Podaj numer drzwi: "))

    # Dwa przypadki: 1. wybrano drzwi z nagrodą, 2. Wybrano drzwi bez nagrody

    do_zamiany = 0  # Będziemy pamiętać drzwi, na które może zmienić wybór uczestnik

    # Opcja 2.
    if wybor != nagroda:
        if wybor != 1 and nagroda != 1:
            print("Otwieramy drzwi numer 1")
            do_zamiany = nagroda
        if wybor != 2 and nagroda != 2:
            print("Otwieramy drzwi numer 2")
            do_zamiany = nagroda
        if wybor != 3 and nagroda != 3:
            print("Otwieramy drzwi numer 3")
            do_zamiany = nagroda

    if wybor == nagroda:
        if wybor == 1:
            do_zamiany = random.choice([2, 3])
            if do_zamiany == 2:
                print("Otwieramy drzwi numer 3")
            else:
                print("Otwieramy drzwi numer 2")
        if wybor == 2:
            do_zamiany = random.choice([1, 3])
            if do_zamiany == 1:
                print("Otwieramy drzwi numer 3")
            else:
                print("Otwieramy drzwi numer 1")
        if wybor == 3:
            do_zamiany = random.choice([1, 2])
            if do_zamiany == 1:
                print("Otwieramy drzwi numer 2")
            else:
                print("Otwieramy drzwi numer 1")

    czy_zmiana = input("Czy zmieniasz wybor? (t/n)")

    if czy_zmiana == "t":
        wybor = do_zamiany

    if wybor == nagroda:
        print("Wygrana!")
        wygrane += 1
    else:
        print("Przegrana!")


print("Wygrane:", wygrane)