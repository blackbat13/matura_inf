# Specyfikacja:
#  Dane:
#    n - liczba naturalna
#    tab[n] - tablica n liczb całkowitych
#  Wynik:
#    Posortowana tablica tab

# Algorytm sortowania przez wybieranie
# 1. Od i := 0, do n-1, wykonuj:
#   2. min_ind := i
#   3. min := tab[i]
#   4. Dla j := i+1 do n-1, wykonuj:
#       5. Jeżeli tab[j] < min, to:
#           6. min := tab[j]
#           7. min_ind := j
#       8. Zamień miejscami tab[i], tab[min_ind]
# 9. Wypisz tab

n = 10
tab = [5, 9, 3, 0, 12, 6, 8, 9, 11, 2]
for i in range(0, n):
    min_ind = i
    min = tab[i]
    for j in range(i+1, n):
        if tab[j] < min:
            min = tab[j]
            min_ind = j
    tab[i], tab[min_ind] = tab[min_ind], tab[i]

print(tab)
