class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = diameter * 0.5
  
  def circumference(self):
    return 2 * self.pi * self.radius
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))

# Project
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address
  
  def available_menus(self, time):
    availables = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        availables.append(menu)
    return availables
    
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + ' - ' + str(self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill
  
brunch_items = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
}
brunch = Menu('Brunch', brunch_items, 1100, 1600)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

early_bird_items = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00,
}
early_bird = Menu('Early Bird', early_bird_items, 1500, 1800)
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

dinner_items = {
  'crostini with eggplant caponata': 13.00, 
  'ceaser salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
}
dinner = Menu('Dinner', dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}
kids = Menu('Kids', kids_items, 1100, 2100)

menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise('1232 West End Road', menus)

new_installment = Franchise('12 East Mulberry Street', menus)

print(flagship_store)
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# arepas
arepas_items = {
  'arepa pabellon': 7.00, 
  'pernil arepa': 8.50, 
  'guayanes arepa': 8.00, 
  'jamon arepa': 7.50
}

arepas_menu = Menu('Arepas', arepas_items, 1000, 2000)

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

arepas = Business("Take a' Arepa", [arepas_place])
print(arepas.franchises[0].menus[0])