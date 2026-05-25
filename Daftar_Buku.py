list_buku=[]
while True:
    print("MASUKKAN DATA BUKU")
    judul=input("Masukkan judul buku\t:")
    penulis=input("Masukkan nama penulis\t:")
    buku=[judul,penulis]
    list_buku.append(buku)
    print("="*30)
    for index,i in enumerate(list_buku):
      print(f"{index+1}.Judul\t:{i[0]}\t\tPenulis\t:{i[1]}")
    print("="*30)
    isbreak=False
    while True:
      val=input("Apakah ingin menambahkan buku(y/n"')')
      if val == "n":
         break
      elif val == "y":
         break
      else:
        print(f'"{val}"\tinput ini tidak valid!')
    if val == "n":
      break
