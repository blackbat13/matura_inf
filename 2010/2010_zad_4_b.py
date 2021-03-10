file = open("anagram.txt")

data = file.read().split("\n")

file.close()

#  print(data)

# Dla każdej linii/wiersza z pliku wejściowego
for line in data:
    # Tworzymy listę wyrazów z linii
    words = line.split(" ")
    word_sorted = sorted(words[0])  # Zapamiętujemy posortowaną reprezentację pierwszego wyrazu
    ok = True  # Zakładamy, że wszystko jest ok - anagramy
    for w in words:  # Przechodzimy przez wszystkie wyrazy w linii i szukamy kontrprzykładu
        if sorted(w) != word_sorted:
            ok = False
            break  # opcjonalnie

    if ok:  # Jeżeli jest ok - wszystkie wyrazy w wierszu są anagramami
        print(line)

