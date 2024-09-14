# 1,a feladat
egeszSzam = 6

# 1,a feladat ellenőrzése
print(egeszSzam)
print(type(egeszSzam))
print("Egész szám: "+str(egeszSzam)+".")

# 1,b feladat
tortSzam = 2.5

# 1,b feladat ellenőrzése
print(tortSzam)
print(type(tortSzam))
print("Tört szám: "+str(tortSzam)+".")

# 1,c feladat
szin = "kék"  # kedvenc színem
print(szin)
print(type(szin))
print("Kedvenc színem a(z) ", szin, ".")  # ide tesz szóközt a pont után
print("Kedvenc színem a(z) "+szin+".")  # ide nem tesz szóközt a pont után

# 1,d feladat
betu = "a"
print(betu)
print(type(betu))
print("Az ABC első betűje: "+betu+".")

# 1,e feladat
szunet_van_e = True
print(szunet_van_e)
print(type(szunet_van_e))

# 1,f feladat
szunet_van_e = False
print(szunet_van_e)
print(type(szunet_van_e))

# 2 feladat
szam = 4
fele = int(szam/2)
print("A(z) "+str(szam)+" szám fele "+str(fele)+".")

# 3 feladat
szam1 = int(input("Adj meg egy egész számot! "))
print(type(szam1))
szam2 = int(input("Adj meg egy másik egész számot! "))
szam3 = int(input("Adj meg egy harmadik egész számot! "))
print("1. szám: "+str(szam1)+"\n2. szám: "+str(szam2)+"\n3. szám: "+str(szam3))

# 4 feladat
# első megoldás
print("1. szám: "+str(szam1)+"2. szám: "+str(szam2)+"3. szám: "+str(szam3))

# második megoldás
print("1. szám: "+str(szam1), end="")
print("2. szám: "+str(szam2), end="")
print("3. szám: "+str(szam3), end="")
