with open('vas.txt', 'r', encoding = 'utf8') as f:
    lista = [sor.strip().replace('-','') for sor in f]
# 2.feladat

print(f'2. Feladat: Adatok beolvasása, tárolása')
# def CdvE(szemszam):
#     k = (10*int(szemszam[0])) + (9*int(szemszam[1])) + (8*int(szemszam[2])) + (7*int(szemszam[3])) + (6*int(szemszam[4])) + (5*int(szemszam[5])) +(4*int(szemszam[6])) + (3*int(szemszam[7])) +(2*int(szemszam[8])) + (1*int(szemszam[9]))  
#     ell = k%11
#     if(int(szemszam[10]) == ell):
#         return True
#     else:
#         return False
    
def CdvE11(szemszam):
    k = 0
    for i in range(10):
        k += (10 - i) * int(szemszam[i])
    return int(szemszam[10]) == k%11
        
        
# 4.feladat
print( f'4. Feladat: Ellenörzés')
[print(f'        Hibas a {sor[0]}-{sor[1:6]}-{sor[7:]} személyi azonosító!') for sor in lista if not CdvE11(sor)]
lista_tiszta = [sor for sor in lista if CdvE11(sor)]

# 5.feladat

print( f'5. Feladat: Vas megyében a vizsgált id ő alatt {len(lista_tiszta)} csecsemő született!')


# 6.feladat
fiuk = sum([1 for sor in lista_tiszta if sor[0] == '1' or sor[0] == '3'])
print( f'6. Feladat: Fiúk száma: {fiuk}')

# 6.feladat
#    ha személyi szám első száma 1 vagy 2 akkor biztos 2000 előtti tehát 1900 plusz evszám
#    ha személyi szám első száma 3 vagy 4 akkor biztos 2000 utáni tehát 2000 plusz evszám
evek =  [(1900 + int(sor[1:3]) if sor[0] == '1' or sor[0] == '2' else 2000 + int(sor[1:3]) ,sor)for sor in lista_tiszta ]

print( f'6. Feladat: Vizsgált időszak: {min(evek)[0]} - {max(evek)[0]}')

# 7.feladat
jelzo = False
for i in evek:
    if (i[0]%4 == 0):
        if(i[1][3:7] == '0224'):
            print( f'7. Feladat: Szökőnapon született baba!')
            jelzo = True
            break
if not jelzo:
    print( f'7. Feladat: Szökőnapon nem született baba!')  

# 8.feladat
szotar = {sor[0] : 0 for sor in evek}
for ev,sor in evek:
    szotar[ev] += 1
    
for i,db in szotar.items():
    print(f'        {i} - {db} fő')






