# Mamy podany ciąg znaków - tekst
# Celem jest podanie długości najdłuższego podciągu
# złożonego z tych samych znaków

# np. aabbaaabaaaabbb
# Odpowiedź: 4

# np. 1000111001011111
# Odpowiedź: 5

# 1. Wczytujemy ciąg str
# 2. wynik := 1
# 3. obecna_dl := 1
# 4. Od i := 1 do długości - 1, wykonuj:
    # 5. Jeżeli i-ty znak == (i-1) znakowi, to:
    #    Czyli obecny znak jest taki sam jak poprzedni, to:
    #    6. obecna_dl += 1
    #    7. Jeżeli obecna_dl > wynik, to wynik := obecna_dl
    # 8. W przeciwnym wypadku:
    #    9. obecna_dl := 1

str = "aabbaaabaaaabbb"
wynik = 1
obecna_dl = 1
for i in range(1, len(str)):
    if str[i] == str[i-1]:
        obecna_dl += 1
        if obecna_dl > wynik:
            wynik = obecna_dl
    else:
        obecna_dl = 1

print(wynik)
