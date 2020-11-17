# Obliczanie wartości wyrażenia zapisanego w ONP - Odwrotnej Notacji Polskiej
# Specyfikacja:
#  Dane: onp - wyrażenie onp w postaci ciągu znaków
#  Wynik: wartość wyrażenia onp
# Przykład:
#  Dane: 2 3 + 5 *
#  Wynik: 25

# Wczytujemy wyrażenie w postaci str
dane = input("Podaj wyrażenie onp: ")

# Konwertujemy wyrażenie na listę
onp = dane.split()

# 1. Tworzymy stos st - jako zwykła lista w pythonie
st = []

# 2. Dla każdego elementu wyrażenia onp, wykonuj:
for element in onp:
    # Sprawdzenie czy liczba - funkcja isnumeric
    # if element.isnumeric()
    # 3. Sprawdzamy, czy element jest operatorem
    # Dozwolone operatory: + - * /
    if element == "*":
        # Pobieramy ostatni element ze stosu i go usuwamy
        b = st.pop()
        # Pobieramy ostatni element ze stosu i go usuwamy
        a = st.pop()
        wynik = a * b
        # Wrzucamy wynik na stos
        st.append(wynik)
    elif element == "/":
        b = st.pop()
        a = st.pop()
        wynik = a / b
        st.append(wynik)
    elif element == "+":
        b = st.pop()
        a = st.pop()
        wynik = a + b
        st.append(wynik)
    elif element == "-":
        b = st.pop()
        a = st.pop()
        wynik = a - b
        st.append(wynik)
    else:
        # Jeżeli to nie był żaden operator, to musi być liczba
        # Konwertujemy na liczbę
        liczba = int(element)
        # I wrzucamy na stos
        st.append(liczba)

if len(st) != 1:
    print("Błąd!")
else:
    print("Wynik: ", st.pop())