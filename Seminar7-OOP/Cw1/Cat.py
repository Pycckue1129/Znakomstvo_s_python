from Animal import Animal


class Cat(Animal):
    hunger = 0

    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def voice(self):
        print("mew")

    def feed(self, food):
        if food == "meat":
            self.hunger -= 5
        else:
            print("mew mew")
