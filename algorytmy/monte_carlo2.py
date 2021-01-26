import random

n = 1000000
ile_kolo = 0

# [0, 1] - ? > [-1, 1]
# [0, 1] * 2 -> [0, 2]
# [0, 2] - 1 -> [-1, 1]

for i in range(n):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    if x * x + y * y <= 1:
        ile_kolo += 1

pi = (4 * ile_kolo) / n

print("Pi = ", pi)
