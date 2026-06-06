class Animal:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def info(self):
        print("I'm an abstract animal and I don't know about myself.")

    def noise(self):
        print("I'm abstract and I don't make any noises.")


class Cat(Animal):
    def __init__(self, weight, color, breed):
        super().__init__(weight, color)
        self.breed = breed

    def info(self):
        print(f"I'm a cat, and I weigh {self.weight} kg I'm a {self.breed}.")

    def noise(self):
        print("Meow...")


animal = Animal(3, "brown")
cat = Cat(4, "Red", "Tabby")
cat.info()
cat.noise()

animal.info()
animal.noise()

print(animal.weight)
