from Animal import Animal
from Salmon import Salmon


class Owl(Animal):
    hunger = 0

    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def add_hunger(self, hunger):
        self.hunger += hunger

    def feed(self, hunger, food):
        if isinstance(food, Salmon):
            self.hunger -= hunger
        else:
            print("boo")

    def is_hungry(self):
        if self.hunger > 0:
            print("I'm hungry")
        else:
            print("I'm NOT hungry")
