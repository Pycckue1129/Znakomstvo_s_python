from HotDrinkTemperature import HotDrinkTemperature


class HotDrinkVendingMachine:
    products = []

    def __init__(self, products):
        self.products = products

    def get_product(self, name, volume, temperature):
        for product in self.products:
            if product.get_name() == name \
                    and product.get_volume() == volume \
                    and isinstance(product, HotDrinkTemperature) \
                    and product.get_temperature() == temperature:
                print(f"Возьмите {name}")
                return product
        return None
