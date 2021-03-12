# Dane:
#  wyraz - ciąg znaków alfanumerycznych
# Wynik:
#  Ciąg utworzony z połączenia wyrazu i jego odwróconej wersji
#  Np. dla wyrazu "makota" wynik to "makotaatokam"

word = "makota"
# result = word + word[::-1]  # Szybka wersja

# Dłuższa wersja
result = word
for i in range(len(word) - 1, -1, -1):
    result += word[i]

print(result)