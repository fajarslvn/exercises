import random as rd

# tanya nama user
print('Siapa nama kamu?')
nama = str(input())

# pertanyaan tebakan
angka_rahasia = rd.randint(1, 20)
print('Oke ' +nama+ ', Saya sedang memikirkan sebuah angka antara 1 hingga 20, Coba tebak, angka berapa yang sedang saya pikirkan?')

# jumlah menebak
for banyak_tebakan in range(1, 7):
  print('Coba tebak')
  tebakan = input()

  # kondisi jawaban (hint) 
  try:
    if int(tebakan) < angka_rahasia:
      print('Angkanya kekecilan ' +nama+ '!')
    elif int(tebakan) > angka_rahasia:
      print('Angkanya kebesaran ' +nama+ '!')
    else:
      break
  except ValueError:
    print(nama+ ' Masukkan angka, jangan masukkan teks!')

# jika pertanyaan betul atau salah
if int(tebakan) == angka_rahasia:
  print('Tebakan ' +nama+ ' BENAR..angka ' +str(angka_rahasia)+ ' ditebak dalam ' +str(banyak_tebakan)+ ' kali tebakan saja!')
else:
  print('Tebakan ' +nama+ ' SALAH! kamu gagal menebak angka ' +str(angka_rahasia))