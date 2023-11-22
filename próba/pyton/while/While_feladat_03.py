# 3. Feladat
# Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!
x = 11
while x > 1:
    x -= 1
    if x % 2 == 0:
        print(x)