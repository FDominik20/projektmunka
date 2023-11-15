hany_sor=int(input("Hány sort szeretnél kiírni?"))
darab_karakter=1
sor=1
while sor <= hany_sor:
    oszlop=1
    while oszlop<=darab_karakter:
        print('o',end='')
        oszlop=oszlop+1
    print('')
    if hany_sor % 2 == 1:
        if sor < int(hany_sor/2 + 1):
            darab_karakter = darab_karakter + 1
        else:
            darab_karakter = darab_karakter -1
    elif hany_sor % 2 == 0:
        if sor < int(hany_sor/2):
            darab_karakter = darab_karakter + 1
        elif sor == int(hany_sor/2):
            darab_karakter = darab_karakter
        else:
            darab_karakter = darab_karakter -1
    sor = sor + 1