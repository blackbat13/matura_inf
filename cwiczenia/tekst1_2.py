# Dane:
#   wyraz - ciąg małych liter alfabetu angielskiego
# Wynik:
#   Najdłuższy rosnącego spójnego podciągu tego wyrazu

#  Rosnący, tzn. kolejne litery nastepują po sobie w kolejności alfabetycznej

#  Przykład:
#    bagklomad - wynik: agklo
#            Inne podciągi rosnące (pełne): b, agklo, m, ad

word = "bagklomad"
counter = 1
max_length = 1
begin = 0  # Indeks obecnego analizowanego podciągu
max_begin = 0  # Indeks początkowy maksymalnego podciągu
for i in range(1, len(word)):
    if word[i] > word[i-1]:
        counter += 1
    else:
        counter = 1
        begin = i

    if counter > max_length:
        max_length = counter
        max_begin = begin


max_end = max_begin + max_length
print(word[max_begin:max_end])
