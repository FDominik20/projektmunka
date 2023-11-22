# 5. Feladat
# Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.
szam = int(input("Adj meg egy páros számot. "))
while True:
    if szam % 2 == 0:
        print("Ok.")
        break
    else:
        szam = int(input("Adj meg egy páros számot. "))
        continue