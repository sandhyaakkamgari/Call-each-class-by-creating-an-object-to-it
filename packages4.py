class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print(f"{self.name} says Woof!")
    
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")

print(dog1.name)
print(dog2.breed)

dog1.bark()
dog2.bark()