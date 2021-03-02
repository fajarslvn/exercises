# name = ''
# while True:
#   print('Type your name')
#   name = input()
#   if name == 'your name':
#     break
# print('Thank you!')

spam = 0
while spam < 5:
  spam += 1
  if spam == 3:
    continue # pass the 3
  print('spam is '+ str(spam))

print('my name is ')
#for i in range(5):
#for i in range(1, 11):
for i in range(11, -1, -1):
  print('Jay five time '+ str(i))

import random
from random import randint

print(random.randint(1, 10))
print(randint(1, 10))

x, y = '12'
y, z = '34'
print(x + y + z) # 134

x = True * False + 3 # True * False = 0 sisa 3
y = False * False + 9**2 # False * False = 0 sisa 81
print(x+y) # 3 + 81 = 84

# global var
x = 5
def add():
  x = 3
  x = x + 5 # 3 + 5
  print(x)

add() # 8
print(x) # 5

b = 50
def f(a, b=b):
  return a + b

b = 20
print(f(1)) # 51

for i in range(1, 2, 2):
  print(i)

# print('How many cats do you have?')

# cats = input()
# try:
#   if int(cats) >= 4:
#     print('Lot of cats!')
#   else:
#     print('Not so many!')
# except ValueError:
#   print('Please put some number.')

test = list(range(0, 6))
print(test)
del test[0]
print(test)
print(test[2:])
print(test[:2])

counting = list(range(1, 100, 4))
print(counting)

check = ['A', 'B', 'C', 'D', 'E']
for i in range(len(check)):
  print("Index " + str(i) + " from " + check[i])
'''
variabel i in range(len(check)) membaca urutan angka list, check[i] membaca isi dari list
immutable (tdk bisa dirubah datanya): string, tupple
mutable (bisa dirubah datanya): list
'''

# List comprehensions
alphabets = ['@A', 'B', '@C', 'D', '@E', 'F']
with_at = [i for i in alphabets if i[0] == '@']
print(with_at)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
up_to_5 = [num for num in nums if num > 5]
print(up_to_5)

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [cls * 9/5 + 32 for cls in celsius]
print(fahrenheit)

# *args example
from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  joined_string = args[0]
  for arg in args[1:]:
    joined_string += '/' + arg
  return joined_string

print(myjoin(path_segment_1, path_segment_2, path_segment_3))

# kwargs example
def create_product(name, price):
  return print(str(name)+' created, being sold for $'+str(price))

def create_products(**kwargs):
  for name, price in kwargs.items():
    create_product(name, price)

create_products(Baseball=3, Shirt=14,Guitar=70)

# alternate
new_product_dict = {
  'Apple': 1,
  'Ice Cream': 3,
  'Chocolate': 5,
}
create_products(**new_product_dict)

# Using both
def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()
  for arg in args:
    text = text.replace(arg, "")
  for kwarg, replacement in kwargs.items():
    text = text.replace(kwarg, replacement)
  return text

# print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))

# Returning functions from functions
def get_math(opr):
  def add(n1, n2):
    return n1 + n2
  def sub(n1, n2):
    return n1 - n2

  if opr == '+':
    return add
  elif opr == '-':
    return sub

add_func = get_math('+')
sub_func = get_math('-')
print(add_func(5,7))
print(sub_func(5,7))

# Decoraters
def title_decorater(print_name_func):
  def wrapper(*args, **kwargs):
    print('Doctor: ')
    print_name_func(*args, **kwargs)
  return wrapper

@title_decorater
def print_name(name, age):
  print(name + ' You are '+str(age))

print_name('Jay', 42)



