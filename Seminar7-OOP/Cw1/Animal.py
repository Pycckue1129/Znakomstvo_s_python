from abc import abstractmethod


class Animal:
    age = 0
    name = ""

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def voice(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass
