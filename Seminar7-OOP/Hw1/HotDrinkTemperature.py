from HotDrink import HotDrink


class HotDrinkTemperature(HotDrink):
    temperature = 0

    def __init__(self, name, volume, temperature):
        super().__init__(name, volume)
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
