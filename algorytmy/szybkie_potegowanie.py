# Specyfikacja:
#  Dane:
#   a - liczba naturalna
#   n - liczba naturalna
#  Wynik:
#    a^n - a podniesione do potęgi n

# Funkcja potega(a, n):
#   Jeżeli n < 2, to:
#      Zwróć a
#   Jeżeli n % 2 == 0, to:
#      n = n // 2
#      Zwróć potega(a,n)**2
#   W przeciwnym przypadku:
#      n = n // 2
#      Zwróc potega(a,n)**2 * a
#   Zwróć potega(a,n)

def potega(a, n):
    if n < 2:
        return a
    if n % 2 == 0:
        n //= 2
        return potega(a, n)**2
    else:
        n //= 2
        return potega(a, n)**2 * a

# potega(a, n) = {  a   dla n == 1
#                {  potega(a, n div 2)^2   dla n mod 2 == 0
#                {  potega(a, n div 2)^2 * a   dla n mod 2 != 0

print(potega(2, 5))