import random

n = 100  # Ilosc testow
do_50 = 0   # Zliczamy wystąpienie powtózenia wśród pierwszych 50 osób

for test in range(n):
    # Losujemy i zapamiętujemy dni urodzin dla 365 osób
    # Następnie zliczamy, czy dni powtórzyły się dla pierwszych 50 osób
    # Zapamiętujemy, ile razy wystąpiło takie powtórzenie

    # Tworzymy listę do zapamiętywania dnia urodzin
    urodziny = []
    for i in range(365):
        dzien = random.randint(1, 365)  #Losujemy numer dnia w roku
        urodziny.append(dzien)

    dni_zliczanie = []   # Dla każdego dnia zliczamy, ile razy wystąpił
    for i in range(366):
        dni_zliczanie.append(0)   # Wypełniamy listę zerami

    for i in range(50):  # Przechodzimy przez pierwszych 50 urodzin
        dzien = urodziny[i]   # Pobieramy z listy dzien urodzin
        dni_zliczanie[dzien] += 1   # Zwiększamy licznik dla danego dnia

    # dni_zliczanie.insert(4, 10)  # Pod indeks 4 dopisz wartość 10

    powtorzenie = False  # Zapamiętujemy, czy nastąpiło powtórzenie
    for i in range(366):
        if dni_zliczanie[i] > 1:  # Jeżeli dzień się powtórzył, to
            powtorzenie = True

    if powtorzenie == True:
        do_50 += 1


print("Powtórzenie wśród pierwszych 50 osób wystąpiło:", do_50, "razy")