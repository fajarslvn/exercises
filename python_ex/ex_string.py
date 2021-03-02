# String Method
def username_generator(first_name, last_name):
  if len(first_name) < 3: # Jika panjang first_name kurang dr 3
      user_name = first_name 
  else: # lainnya
      user_name = first_name[0:3] # [0:3] 4 index huruf dari first_name
  if len(last_name) < 4: # Jika panjang first_name kurang dr 4
      # Tambahkan last_name di nilai user_name yg sdh ada
      user_name += last_name
  else: # lainnya 
      user_name += last_name[0:4] # [0:4] 5 index huruf dari last_name
  return user_name # Kembalikan hasil akhir ke function

user_name = username_generator("Abe", "Simpson")
print(user_name)

# Gunakan global variable user_name
def password_generator(user_name):
  password = "" # container kosong untuk menampung hasil baru
  #Check setiap huruf pada user_name dimulai dari huruf pertama (index[0])
  for word in range(0, len(user_name)):
    #cetak satu-persatu mulai dari huruf paling akhir (-1)
    password += user_name[word-1]
  return password #kembalikan hasil akhir kepada function

print(password_generator(user_name))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  uniques = 0 # Container kosong untuk menampung nilai/hasil baru
  for letter in letters: # Check setiap huruf di dalam list letters
    if letter in word: # Jika huruf di variable word ada di list letter
      uniques += 1 # Masukkan ke list uniques 1 per 1
  return uniques # Kembalikan hasil kpd function

print(unique_english_letters("mississippi"))

def count_char_x(word, x):
  total_letter = 0
  for letter in word:
    if x == letter:
      total_letter += 1
  return total_letter

print(count_char_x("mississippi", "s"))

def count_multi_char_x(word, x):
  splits = word.split(x)
  return (len(splits)-1)

print(count_multi_char_x("mississippi", "iss"))

def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind+1:end_ind])
  return word

print(substring_between_letters("apple", "p", "e"))

def x_length_words(sentence, x):
  list_sntc = sentence.split()
  for sntc in list_sntc:
    if len(sntc) >= x:
      return True
    else:
      return False

print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))

def check_for_name(sentence, name):
  if name.lower() in sentence.lower() or name.upper() in sentence.upper() or name.title() in sentence.title():
    return True
  else:
    return False

print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))

def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

print(every_other_letter("Codecademy"))

def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

print(reverse_string("Codecademy"))

def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

print(make_spoonerism("Codecademy", "Learn"))

def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

print(add_exclamation("Codecademy"))

# Project Example
#database
daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""


#Ganti (;,;) dengan (+)
daily_sales_replaced = daily_sales.replace(";,;","+")
# print(daily_sales_replaced)

#Pisahkan & groupkan data ('') yg berbatasan dgn koma (,)
daily_transactions = daily_sales_replaced.split(",")
# print(daily_transactions)


# List container kosong yg bertugas untuk menampung nilai baru
daily_transactions_split = []
# Masuk ke dlm data di dalam list & hilangkan semua tanda (+) dan group data menjadi list (list didalam list)
for transaction in daily_transactions:
  daily_transactions_split.append(transaction.split("+"))
# print(daily_transactions_split)


# List container kosong yg bertugas untuk menampung nilai baru
transactions_clean = []
# Bersihkan data dari tanda dan spasi yg tdk diperlukan. Harus melalui 2 buah loop.
# Pertama  masuk ke dalam list besar agar bisa masuk ke list kecil untuk memanipulasi data yg ada di list kecil
for trans in daily_transactions_split:
  # List container kosong yg bertugas untuk menampung nilai baru
  tc = []
  # Masuk kedalam setiap list kecil, ganti data yg ada tanda "\n" dgn kosong (hapus), lalu hilangkan setiap spasi
  for data_point in trans:
    tc.append(data_point.replace("\n", "").strip(" "))
    # print(data_point)
  transactions_clean.append(tc)
  # print(tc)
# print(transactions_clean)

  # CODE SALAH! Ingat, selalu check indentation. Dlm hal ini jika baris code sejajar dgn hasil dr for loop, maka hasil code di duplikasi hingga 4x mengikuti byknya data di dlm list. Tapi yg kita perlukan disini adalah tdk ada yg  di duplikasi -->
  # for data_point in trans:
  #   tc.append(data_point.replace("\n", "").strip(" "))
  #   transactions_clean.append(tc)


# Buat list kosong kategori untuk setiap data
customers = []
sales = []
thread_sold = []
the_date = []
# Masukan setiap data ke dalam masing2 kategori list
for transaction in transactions_clean:
  # [0], [1], [2] index letak posisi dari data tsb
  customers.append(transaction[0])
  sales.append(transaction[1])
  thread_sold.append(transaction[2])
  # print(transaction)

# print(customers)
# print(sales)
# print(thread_sold)


# Container kosong untuk total_sales
total_sales = 0
# Check setiap nilai dalam list sales satu persatu
for sale in sales:
  # Gabungkan (+=) semua nilai sale & pindahkan ke dlm total_sales. Hilangkan juga tanda ($)
  total_sales += float(sale.strip("$"))

# print(total_sales)
# print(thread_sold)


# List container kosong yg bertugas untuk menampung nilai baru
thread_sold_split = []
# Check setiap nilai dalam list thread_sold satu persatu
for sale in thread_sold:
  # Pisahkan setiap warna ke dlm variable "color"
  # Pisahkan juga warna yg ada tanda (&)
  for color in sale.split("&"):
    # Masukkan hasil loop (color) ke dlm list baru (thread_sold_split)
    thread_sold_split.append(color) 


# buat fungsi baru dgn 1 parameter
def color_count(color):
  # List container kosong yg bertugas untuk menampung nilai baru
  color_total = 0
  # Check setiap nilai dalam list thread_sold_split satu persatu
  for thread_color in thread_sold_split:
    # Jika color sesuai dgn warna yg ada di thread_color
    if color == thread_color:
      #  Jumlahkan banyaknya dan masukkan ke list color_total
      color_total += 1
  return color_total # Kembalikan hasil proses kpd function

# print(color_count('white'))

# List dari berabagai macam warna yg ada di data
colors = ['red','yellow','green','white','black','blue','purple']
# Untuk semua nilai/warna yg ada di dlm list colors, masukkan ke dlm variable color satu persatu untuk di proses
for color in colors:
  # Cetak string ini & sisipi nilai dari function color_count & variable color dgn bantuan function format
  print("Thread Shed sold {} threads of {} thread today.".format(color_count(color), color))

