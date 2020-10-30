# Otwieramy plik z danymi
file = open('liczby.txt')

# Wczytujemy wszystkie linijki z pliku
binary = file.read().split("\n")

# Zamykamy plik wejściowy
file.close()

# 1. result := 0
# 2. Dla każdej liczby binarnej b, wykonaj:
#   3. ones := 0
#   4. zeros := 0
#   5. Dla każdego znaku liczby b, wykonaj:
#      6. Jeżeli znak to 1, to:
#           7. ones := ones + 1
#      8. Jeżeli znak to 0, to:
#           9. zeros := zeros + 1
#   10. Jeżeli zeros > ones, to:
#      11. result := result + 1
# 12. Wypisz result

result = 0
for b in binary:
    ones = 0
    zeros = 0
    for digit in b:
        if digit == '1':
            ones += 1
        else:
            zeros += 1
    if zeros > ones:
        result += 1

print(result)
