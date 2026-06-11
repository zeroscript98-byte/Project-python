teks = """
Bakemonogatari (2009)
Nisemonogatari (2012)
Nekomonogatari (Black) (2012)
Kizumonogatari I: Tekketsu-hen
Kizumonogatari II: Nekketsu-hen
Kizumonogatari III: Reiketsu-hen
Monogatari Series: Second Season
Hanamonogatari
Tsukimonogatari
Owarimonogatari
Koyomimonogatari
Owarimonogatari
Zoku Owarimonogatari
Monogatari Series: Off & Monster Season (2024–present)
"""
teks = teks.lower()
for tanda in ".,!?;:()\"'":
    teks = teks.replace(tanda,"")
kata = teks.split()
jumlah_karakter = len(teks)
jumlah_kata = len(kata)
frekuensi = {}
for k in kata:
    if k in frekuensi:
        frekuensi[k] += 1
    else:
        frekuensi[k] = 1
print("Jumlah karakter:", jumlah_karakter)
print("Jumlah kata:", jumlah_kata)
print("\nFrekuensi kata: \n \n")
index=0
for k in frekuensi:
  index += 1
  print(index,".",k, ":", frekuensi[k])