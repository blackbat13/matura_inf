# Dane:
#  wyraz - ciąg znaków alfanumerycznych
# Wynik:
#  Ciąg znaków taki jak zadany, tylko że bez znaków spacji

word = "ala ma kota"
result = ""

for letter in word:
    if letter != " ":
        result += letter

print(result)