data=[]
print("MASUKKAN ANGKA BERAPA PUN UNTUK AI PELAJARI (Odd or Even)")
while True:
  inp=int(input('Angka : '))
  if inp not in data:
    print('Belum tahu son😭🙏')
    data.append(inp)
  elif inp%2 == 0:
    print(f"{inp} adalah angka genap")
  else:
    print(f"{inp} adalah angka ganjil")