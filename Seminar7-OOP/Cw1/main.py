from Cat import Cat
from Owl import Owl
from Salmon import Salmon
from Dog import Dog

cat = Cat("cat1", 5)
cat.voice()
print(cat.get_age())

dog = Dog("dog", 10)
dog.voice()
salmon = Salmon("sal", 20)
salmon.add_hunger(5)
salmon.feed("eggs")
salmon.is_hungry()
salmon.feed("bread")
salmon.is_hungry()

owl = Owl("owl1", 6)
owl.add_hunger(5)
owl.add_hunger(5)
owl.is_hungry()
owl.feed(4, dog)
owl.is_hungry()
owl.feed(4, cat)
owl.is_hungry()
owl.feed(16, salmon)
owl.is_hungry()
