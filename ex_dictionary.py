# The function should return the sum of the values of the dictionary
def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total

print(sum_values({"milk":5, "eggs":2, "flour":3}))
print(sum_values({10:1, 100:2, 1000:3}))# .keys() bisa di jumlahkan disini 
# Create a counter variable and start it at 0. Loop through all of the elements of my_dictionary.values() and add each value to your counter variable.

# This function should return the sum of the values of all even keys.
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      total += my_dictionary[key]
  return total

print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))
# Create a counter variable and start it at 0. Loop through all of the elements of the keys of the dictionary by using my_dictionary.keys(). If the key is even (which you can check by using key % 2 == 0), add the corresponding value to the counter.

# The function should add 10 to every value in my_dictionary and return my_dictionary
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))
# Loop through every key in the dictionary and add 10 to the value by using my_dictionary[key] += 10.

# This function should return a list of all values in the dictionary that are also keys.
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      value_keys.append(value)
  return value_keys

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# Loop through all values in the dictionary by using for value in my_dictionary.values(). Check to see if value is in my_dictionary.keys() and if so, append it to a list.

# The function should return the key associated with the largest value in the dictionary.
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))
'''Begin by creating two variables named largest_key and largest_value. Initialize largest_value to be the smallest number possible (you can use float("-inf"). Initialize largest_key to be an empty string.

Loop through all keys/value pair in the dictionary. Any time you find a value larger than what is currently stored in largest_value, replace largest_value with that new value. Similarly, replace largest_key with the key associated with the new largest value.

After looping through all key/value pairs, return largest_key.'''

# The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))
# First create an empty dictionary named something like word_lengths. Loop through every word in words and add a new key using word_lengths[word] = len(word)

# The function should return a dictionary containing the frequency of each element in words.
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
    	freqs[word] = 0
    freqs[word] += 1
  return freqs

print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))
# First, create a new empty dictionary. Then, loop through every word in words. If word is not a key in the dictionary, make word a key with a value of 1. If word was already a key, increase the value associated with word by 1.

# The function should return the number of unique values in the dictionary.
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# Begin by creating a new empty list named seen_values. Loop through all of the values of my_dictionary. For every value, check to see if that value is in seen_values. If it is, continue to the next value. If it is not, add it to seen_values. After looping through all values, return the length of seen_values.

'''names should be a dictionary where the key is a last name and the value is a list of first names. 
The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.'''
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
'''Begin by creating an empty dictionary named something like letters. Loop through the keys of names and access the first letter of each the key using key[0].
If that letter is not a key in letters, create a new key/value pair where the key is key[0] and the value is the length of names[key].
If that letter is a key in letters, simply add the length of names[key] to value associated with key[0] in letters.'''

# Project
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [letter.lower() for letter in letters]
points *= 2

letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points[" "] = 0
print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {
  "player1":["BLUE", "TENNIS", "EXIT"], 
  "wordNerd":["EARTH", "EYES", "MACHINE"], 
  "Lexi Con":["ERASER", "BELLY", "HUSKY"], 
  "Prof Reader":["ZAP", "COMA", "PERIOD"]
  }

player_to_points = {}
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points

update_point_totals()
print(player_to_points)

def play_word(player, word):
  player_to_words[player].append(word)
  update_point_totals()

play_word("player1", "CODE")
print(player_to_words)
print(player_to_points)
