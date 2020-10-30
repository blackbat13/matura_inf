file = open('liczby.txt')

# Wczytujemy wszystkie linijki z pliku
binary = file.read().split("\n")

# 1. div_2 = 0
# 2. div_8 = 0
# 3. Dla każdej liczby binarnej b, wykonaj:
#   4. Jeżeli podzielna przez 2, to: div_2 := div_2 + 1
#   5. Jeżeli podzielna przez 8, to: div_8 := div_8 + 1
# 6. Wypisz div_2, div_8

div_2 = 0
div_8 = 0
for b in binary:
    liczba = b[-1]
    if liczba == "0":
        div_2 += 1
    if b[-1] == "0" and b[-2] == "0" and b[-3] == "0":
        div_8 += 1

file.close()

print("Podzielne przez 2:", div_2)
print("Podzielne przez 8:", div_8)
