# Dane:
#  wyraz - ciąg znaków alfanumerycznych
# Wynik:
#  Ciąg znaków taki jak zadany, tylko że wszystkie znaki są podwojone
#  Np. dla ciągu "abc" wynik to "aabbcc"

word = "ala ma kota"
result = ""

for letter in word:
    result += letter + letter

print(result)