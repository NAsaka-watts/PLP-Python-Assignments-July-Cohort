# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")


# Derived class (Inheritance + Encapsulation example)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.__cooling_system = cooling_system  # private attribute

    def info(self):
        super().info()
        print(f"Cooling system: {self.__cooling_system}")

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model}...")

# Testing Assignment 1
phone1 = Smartphone("Apple", "iPhone 14", 128)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "Advanced Liquid Cooling")

phone1.info()
phone1.call("123-456-7890")

print("\nGaming Phone:")
phone2.info()
phone2.play_game("Genshin Impact")
