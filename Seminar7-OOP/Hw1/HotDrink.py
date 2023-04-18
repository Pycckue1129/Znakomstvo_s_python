class HotDrink:
    name = ""
    volume = 0

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
