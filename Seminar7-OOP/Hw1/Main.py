from HotDrinkTemperature import HotDrinkTemperature
from HotDrink import HotDrink
from HotDrinkVendingmachine import HotDrinkVendingMachine
products = [HotDrinkTemperature("Tea", 150, 80), HotDrinkTemperature("Latte", 220, 85),
            HotDrinkTemperature("Cacao", 220, 75), HotDrinkTemperature("Chocolate", 200, 65), HotDrink("Sprite", 330),
            HotDrink("CocaCola", 500)]

machine = HotDrinkVendingMachine(products)

hot_drink = machine.get_product("Cacao", 200, 90)
if hot_drink is None:
    print("Ваш выбор отсутствует")

hot_drink = machine.get_product("Tea", 150, 80)
if hot_drink is None:
    print("Ваш выбор отсутствует")
