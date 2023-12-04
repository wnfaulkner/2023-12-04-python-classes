##### PYTHON CLASSES #####



# create a list
nums = [1, 2, 3]
# print the attributes & methods nums has
# print( dir(nums) )



# 3.  WRITING A BASIC PYTHON CLASS

class Dog():
  def __init__(self, name, age=0):
    self.name = name
    self.age = age

  def bark(self):
    print(f'{self.name} says woof!')

  def __str__(self):
    return f'Dog named {self.name} is {self.age} years old'

spot = Dog('Spot', 8)

# print(spot) # -> similar to <__main__.Dog object at 0x7f27bad2c208>


# print(spot.name, spot.age) #print the name and age attributes of the spot object


# spot.bark() #invoke the spot object's bark instance method



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

print(car.make, car.model)
print(car)
print(car.running)
car.start()
print(car.running)
car.stop()
print(car.running)