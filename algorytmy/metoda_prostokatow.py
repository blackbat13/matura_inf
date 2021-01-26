def f(x):
    return x


a = 0
b = 5

krok = 0.01  # Szerokość prostokąta

pole = 0
x = a + krok  # Zaczynamy od początku przedziału

while x <= b:
    y = f(x)  # Wysokość prostokąta
    pole += krok * y
    x += krok  # Przechodzimy do kolejnego punktu

print("Pole: ", pole)
