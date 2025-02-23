class Product:                  # Defines count logic
    def __init__(self):
        self._count = 0

    def increase_count(self):
        self._count += 1

    def get_count(self):
        return self._count

class Food(Product):            # Inherits everything from Product
    pass

class Fish(Food):               # Inherits everything from Product
    pass

class Clothes(Product):         # Inherits everything from Product
    pass

class Electronics(Product):     # Inherits everything from Product
    pass

food = Food()
food.increase_count()
print(food.get_count())         # Expected: 1

fish = Fish()
fish.increase_count()
print(fish.get_count())         # Expected: 1

clothes = Clothes()
clothes.increase_count()
clothes.increase_count()
print(clothes.get_count())      # Expected: 2

electronics = Electronics()
print(electronics.get_count())  # Expected: 0