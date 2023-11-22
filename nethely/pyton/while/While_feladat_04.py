# 4. Feladat
# Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!
x = 1
bekert = input("Bekért szöveg, adj meg valamit. ")
hanyszorlegyenkiirvaabekertszoveg = int(input("Hányszor legyen kiírva a bekért szöveg? "))

while x <= hanyszorlegyenkiirvaabekertszoveg:
    x += 1
    print(bekert)