"""
szam1 = 10
szam2 = 2

print("A két szám összege "+str(szam1 + szam2))
print("A két szám különbsége "+str(szam1 - szam2))
print("A két szám szorzata "+str(szam1 * szam2))
print("A két szám hányadosa "+str(int(szam1 / szam2)))
print("A két szám hatványa "+str(szam1 ** szam2))

"""
import beolvas

szam1 = beolvas.tort_szam_beolvas()
szam2 = beolvas.tort_szam_beolvas()

# műveletek
osszeg = szam1 + szam2
kulonbseg = szam1 - szam2
szorzat = szam1 * szam2
hanyados = szam1 / szam2
maradek = szam1 % szam2
hatvany = szam1 ** szam2

# kiírás
print(osszeg)
print(kulonbseg)
print(szorzat)
print(hanyados)
print(maradek)
print(hatvany)
