# Dane:
#   wyraz - ciąg małych liter alfabetu angielskiego
# Wynik:
#   Długość najdłuższego rosnącego spójnego podciągu tego wyrazu

#  Rosnący, tzn. kolejne litery nastepują po sobie w kolejności alfabetycznej

#  Przykład:
#    bagklomad - wynik: 5, podciąg: agklo
#            Inne podciągi rosnące (pełne): b, agklo, m, ad

# Pseudokod:
#  1. licznik := 1
#  2. maks := 1
#  3. Od i := 1 do len(wyraz) - 1, wykonuj:
#     4. Jeżeli wyraz[i] > wyraz[i-1], to:
#         5. licznik := licznik + 1
#     6. W przeciwnym przypadku:
#        7. licznik := 1
#     8. Jeżeli licznik > maks:
#        9. maks := licznik
# 10. Wypisz maks

word = "bagklomad"
counter = 1
max_length = 1
for i in range(1, len(word)):
    if word[i] > word[i-1]:
        counter += 1
    else:
        counter = 1

    if counter > max_length:
        max_length = counter

print(max_length)
