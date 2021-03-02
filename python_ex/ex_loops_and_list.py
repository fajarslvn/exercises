# Return the count of how many numbers in the list are divisible by 10.
def divisible_by_ten(nums):
  count = 0 #container kosong
  for number in nums:
    #jika angka bisa habis (nol) dibagi 10, simpan
    if (number % 10 == 0):
      count += 1 #bergerak & check ke angka selanjutnya temukan & simpan
  return count #kembalikan hasil for loop ke function

print(divisible_by_ten([20, 25, 30, 35, 40]))
# permintaannya ada berapa angka yg bisa habis dibagi 10


# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list. Return the new list containing the greetings.
def add_greetings(names):
  greetings = [] #container untuk menampung hasil
  #jika ingin memanipulasi isi list hrs menggunakan range(len(list))
  for name in range(len(names)):
    #menambahkan nilai baru dari hasil for loop, kedlm container kosong
    greetings.append("Hello, "+str(names[name]))
  return greetings #mengembalikan nilai ke function, melalui container kosong yg sdh di isi dgn value yg baru

print(add_greetings(["Owen", "Max", "Sophie"]))

'''
The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
'''
def delete_starting_evens(lst): #hapus angka genap
  #jika jumlah angka (len) di dalam list lebih besar dari 0 dan angka dpt dibagi habis dgn 2
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:] #sisa hasil loop dijadikan angka pertama dlm list
  return lst #kembalikan hasil ke function

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
def odd_indices(lst):
  new_lst = [] # list kosong untuk menampung nilai baru
  # Hitungan dimulai dr nilai pertama longkap setiap nilai kedua
  for i in range(1, len(lst), 2):
    # Masukkan nilai dr list lama ke list baru
    new_lst.append(lst[i])
  # Kembalikan nilai list baru yg di modifikasi ke function
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

'''
Return a new list containing every number in bases raised to every number in powers.
example: exponents([2, 3, 4], [1, 2, 3])
the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.
'''
def exponents(bases, powers):
  new_lst = [] #list kosong untuk menampung nilai baru
  for base in bases:# nilai index di dlm list bases
    for power in powers:# nilai index di dlm list powers
      # kalikan 1 per 1 nilai di dlm list secara berurutan, lalu masukkan hasil ke list baru ((2**1, 2**2, 2**3),(3**1, 3**2, dst))
      new_lst.append(base ** power)
  return new_lst#kembalikan hasil nilai yg baru kpd function

print(exponents([2, 3, 4], [1, 2, 3]))


# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
def larger_sum(lst1, lst2):
  if sum(lst1) >= sum(lst2):
    return lst1
  return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

'''
The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
the following code should return  9020.
'''
def over_nine_thousand(lst):
  sum = 0# cointainer kosong untuk menampung hasil baru
  for number in lst:
    # Tambahkan 1 per 1 nilai yg ada di dlm list
    sum += number
    # Jika total nilainya lebih dari 9000, berhenti
    if (sum > 9000):
      break
  return sum # Kembalikan nilai hasil akhir perhitungan ke function

print(over_nine_thousand([8000, 900, 120, 5000]))


# The function should return the largest number in nums
def max_num(nums):
  # urutkan nilai di dlm list dr yg terendah, ambil nilai yg terakhir
  return sorted(nums) [-1]

print(max_num([50, -10, 0, 75, 20]))

'''
The function should return a list of the indices where the values were equal in lst1 and lst2.
the following code should return [0, 2, 3]'''
def same_values(lst1, lst2):
  equal = [] # List kosong untuk menampung hasil baru
  for i in range(len(lst1)): # i menampung index nilai di dlm lst1
    if lst1[i] == lst2[i]: # Jika index di lst1 ada yg sama dgn lst2
      equal.append(i)# Masukkan nilai index yg yg ditampung i ke equal
  return equal # Kembalikan hasil baru ke function

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.
def reversed_list(lst1, lst2):
  # buat list baru dgn berisikan lst2 yg ditulis dr belakang
  reverse = lst2[::-1]
  # Jika isi dr reverse tdk sama dgn isi lst1
  if reverse != lst1:
    return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# while loop adalah loop yg tak berakhir. Jika hasil belum tercapai maka while loop akan terus-menerus berputar.
dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]

students_in_poetry = []
while len(students_in_poetry) < 6:
  print(students_in_poetry)
  student = all_students.pop()
  students_in_poetry.append(student)


# Mencari huruf yg sama di dlm sebuah string
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(common_letters("banana", "crane"))

def common_nums(nums_one, nums_two):
  common = []
  for num in nums_one:
    if (num in nums_two) and not (num in common):
      common.append(num)
  return common

print(common_nums([1,2,3,4], [1,3,4,5]))

