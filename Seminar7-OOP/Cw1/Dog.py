from Animal import Animal


class Dog(Animal):
    hunger = 0

    def voice(self):
        print("vuf")

    def feed(self, food):
        if food == "meat":
            self.hunger -= 5
        else:
            print("vuf vuf")
