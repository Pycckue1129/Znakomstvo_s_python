from Animal import Animal


class Salmon(Animal):
    hunger = 0

    def feed(self, food):
        if food == "bread":
            self.hunger -= 5
        else:
            print("bulk")

    def add_hunger(self, hunger):
        self.hunger += hunger

    def is_hungry(self):
        if self.hunger > 0:
            print("I'm hungry")
        else:
            print("I'm NOT hungry")
