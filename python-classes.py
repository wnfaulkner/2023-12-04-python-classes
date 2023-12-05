##### PYTHON CLASSES #####



# create a list
nums = [1, 2, 3]
# print the attributes & methods nums has
# print( dir(nums) )



# 3.  WRITING A BASIC PYTHON CLASS

class Dog():
  next_id = 1 # class attribute

  def __init__(self, name, age=0):
    self.name = name
    self.age = age
    self.id = Dog.next_id
    Dog.next_id += 1

  def bark(self):
    print(f'{self.name} says woof!')

  def __str__(self):
    return f'Dog ({self.id}) named {self.name} is {self.age} years old'
  
  @classmethod
  def get_total_dogs(cls): # cls represents the Dog class
    return cls.next_id - 1

# spot = Dog('Spot', 8)
# print(spot) # -> similar to <__main__.Dog object at 0x7f27bad2c208>
# # print(spot.name, spot.age) #print the name and age attributes of the spot object
# # spot.bark() #invoke the spot object's bark instance method

# pup = Dog('Lassie')
# print(pup)
# print(Dog.get_total_dogs())  # class methods are called on the class, not an instance



# 7. Inheritance, Subclasses & Superclasses

class ShowDog(Dog): # Pass in superclass as argument
  def __init__(self, name, age=0, total_earnings=0): # Add additional parameters AFTER those in the superclass
    Dog.__init__(self, name, age) # Always call the superclass's __init__ first
    self.total_earnings = total_earnings  # Now add any new attributes
  
  def add_prize_money(self, amount): # Add additional methods
    self.total_earnings += amount
    print(f'{self.name}\'s new total earnings are {self.total_earnings}')


# winky = ShowDog('Winky', 3, 1000)
# print(winky) # Yay, inherited the overridden __str__
# winky.bark() # Yay, inherited the bark method
# print(winky.total_earnings) # -> 1000
# winky.add_prize_money(500) # New method that 'Dogs' don't have
# print(winky.total_earnings) # -> 1500

#  PT 2 PRACTICE EXERCISE

class Vehicle():
  def __init__(self, make, model, running=False):
    self.make = make
    self.model = model
    self.running = running

  def start(self):
    self.running = True
    print("running...")

  def stop(self):
    self.running = False
    print("stopped...")

  def __str__(self):
    return f'Vehicle is a {self.make} model {self.model}'
  
car = Vehicle('Tesla', 'Model S')

# print(car.make, car.model)
# print(car)
# print(car.running)
# car.start()
# print(car.running)
# car.stop()
# print(car.running)


# 9. OPTIONAL PRACTICE EXERCISE

import random

class BankAccount():
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.account_no = random.randint(111111111, 999999999)
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

  def __str__(self):
    return f"Account #: {self.account_no} - Owner: {self.owner} - Balance: ${float(self.balance)}"

acct_a = BankAccount("Jerry")
print(acct_a)
acct_a.deposit(100)
acct_a.withdraw(25)
print(acct_a)

acct_b = BankAccount("Joanne")
print(acct_b)
acct_b.deposit(130)
acct_b.withdraw(52)
print(acct_b)
    