import copy
from .subjects import Cat, Dog, Human
from .objects import Product, ProductShop, PetShop, Mall, UnitStorage, SeparateStorage, TechnoShop


class Subjects:
    # Creates pets
    # Creates cats
    sphinx = Cat('sphinx', 120, 'sphinx', 25)
    siberian = Cat('siberian', 100, 'siberian', 15)
    # Creates dogs
    pitbull = Dog('pit bull', 350, 'pit bull', 50)
    terrier = Dog('terrier', 120, 'terrier', 25)
    all_pets = [sphinx, siberian, pitbull, terrier]


class Objects:
    # Products
    bread = Product('bread', 25, 2.5, 'bakery')
    fish = Product('fish', 20, 1.5, 'sea-food')
    octopus = Product('octopus', 130, 10, 'sea-food')
    chicken = Product('chicken', 100, 8, 'meat')
    sausage = Product('sausage', 30, 2, 'meat')
    carrot = Product('carrot', 12, 1, 'vegetable')
    tomato = Product('tomato', 15, 1, 'vegetable')
    apple = Product('apple', 18, 1, 'fruit')
    beer = Product('beer', 12, 2, 'alcohol-drink')
    cola = Product('cola', 15, 2, 'sweet-drink')
    milk = Product('milk', 50, 3, 'natural-drink')
    water = Product('water', 10, 0.5, 'natural-drink')
    all_products = [bread, fish, octopus, chicken, sausage, carrot, tomato, apple, beer, cola, milk, water]
    # Storage
    saturn_refrigerator = SeparateStorage("saturn refrigerator", 15, 200, 'saturn', [])
    samsung_refrigerator = SeparateStorage("samsung refrigerator", 20, 350, 'samsung', [])
    refrigerators_corner = UnitStorage("refrigerators' storage", 2)

    dogs_corner = UnitStorage("dogs' corner", 2)
    cats_corner = UnitStorage("cats' corner", 3)

    all_techno = copy.deepcopy([saturn_refrigerator, samsung_refrigerator])
    # Shops
    shop_best_goods = ProductShop('Best-Goods', all_products)
    shop_simon_pets = PetShop("Simon's pets", Subjects.all_pets)
    shop_techno_fox = TechnoShop("Techno Fox", all_techno)
    all_shops = [shop_best_goods, shop_simon_pets, shop_techno_fox]
    mall_ocean_plaza = Mall("Ocean Plaza", all_shops)


class MainUnit:
    human = Human('no name', 'no gender', 1, Objects.refrigerators_corner, Objects.dogs_corner, Objects.cats_corner)

