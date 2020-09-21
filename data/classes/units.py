from .subjects import Dog, Cat, Human, AnimalSeller, Pet, Cashier, Bitch
from .values import Values
from .objects import Product, Window, Place, Door, Refrigerator, WorkDesk, ShopWindow, RootObject, Bar, DollarGun, CoffeeMachine, FootballTable, Armchair
from .display import ChoicePanel, TextPanel, ImagesPanel, ClockPanel, World, Room
from .rgb import Colors
from .sounds import HumanSounds, RefrigeratorSounds, CatSounds, DoorSounds, ShopSounds, AutomaticDoorSounds, SoundExemplars, CoffeeMachineSounds, TableFootballSounds, BitchSounds
from .sprites import HumanSprites, CatSprites, DogSprites, WomanSprites, RipSprite, CashierSprites

import copy


class Products:
    bread = Product('bread', 70, 2.5, 'bakery', 'images/products/bread.png')
    cake = Product('cake', 100, 5, 'bakery', 'images/products/cake.png')
    pizza = Product('pizza', 80, 3.5, 'bakery', 'images/products/pizza.png')
    fish = Product('fish', 30, 1.5, 'sea-food', 'images/products/fish.png')
    octopus = Product('octopus', 130, 10, 'sea-food', 'images/products/octopus.png')
    lobster = Product('lobster', 300, 20, 'sea-food', 'images/products/lobster.png')
    chicken = Product('chicken', 100, 8, 'meat', 'images/products/chicken.png')
    sausage = Product('sausage', 35, 2, 'meat', 'images/products/sausage.png')
    steak = Product('steak', 180, 10, 'meat', 'images/products/steak.png')
    carrot = Product('carrot', 20, 1, 'vegetable', 'images/products/carrot.png')
    tomato = Product('tomato', 20, 1, 'vegetable', 'images/products/tomato.png')
    apple = Product('apple', 20, 1, 'fruit', 'images/products/apple.png')
    beer = Product('beer', 30, 2, 'alcohol-drink', 'images/products/beer.png')
    cola = Product('cola', 35, 2, 'sweet-drink', 'images/products/cola.png')
    milk = Product('milk', 50, 3, 'natural-drink', 'images/products/milk.png')
    #water = Product('water', 10, 0.5, 'natural-drink')
    all_products = [bread, pizza, cake, fish, octopus, lobster, chicken, steak, sausage, carrot, tomato, apple, beer, cola, milk]
    # cocktails
    mockito = Product('mockito', 50, 5, 'alcohol-drink', 'images/products/mockito.png')
    long_island = Product('long_island', 50, 5, 'alcohol-drink', 'images/products/long_island.png')
    whiskey = Product('whiskey', 50, 5, 'alcohol-drink', 'images/products/whiskey.png')
    margarita = Product('margarita', 50, 5, 'alcohol-drink', 'images/products/margarita.png')
    all_cocktails = [long_island, whiskey, mockito, margarita]


class Panels:
    game_over_panel = TextPanel('Game over', Colors.black, (0, 0))
    products_panel = ImagesPanel('Products')
    clock_panel = ClockPanel()


class Doors:
    exit_door = Door('wooden', 'images/door.png', 'Exit', 100, 'kind', DoorSounds)
    automatic_door = Door('automatic', 'images/automatic_doors.png', "Exit", 100, 'automatic', AutomaticDoorSounds)


class Refrigerators:
    saturn = Refrigerator("Saturn", 20, 200, 'cheap', [], 'images/refrigerator.png', "Open",
                          RefrigeratorSounds)


class Dogs:
    ralf = Dog('Ralf', 301, 'dog', 'terrier', 50, Values.wall_width, Values.room_height - Values.floor_height, 12,
               DogSprites, SoundExemplars.dog_sounds)


class Cats:
    tom = Cat('Tom', 101, 'cat', 'sphinx', 30, 2 * Values.wall_width, Values.room_height - Values.floor_height, 8,
              CatSprites, SoundExemplars.cat_sounds)


class Places:
    # World
    home = Place('home', 'images/places/home.png')
    work = Place('work', 'images/places/work.png')
    mall = Place('mall', 'images/places/mall.png')
    club = Place('club', 'images/places/club.png')
    world_places = [home, work, mall, club]
    world = World(world_places)
    # Mall
    products_shop = Place('Best-goods', 'images/places/products_shop.png')
    pets_shop = Place("Susan's pets", 'images/places/pets_shop.png')
    clothes_shop = Place("Soft_clothes", 'images/places/clothes_shop.png')
    exit = Place("exit", 'images/places/exit.png')
    mall_places = [products_shop, pets_shop, clothes_shop, exit]
    mall_world = World(mall_places)


class AdditionalObjects:
    # Home
    kitchen_table = RootObject('kitchen table', 'images/kitchen_table.png')
    armchair = Armchair('armchair', 'images/armchair.png', 'Lounge')
    old_armchair = RootObject('armchair', 'images/armchair.png')

    # Work
    work_desk = WorkDesk('work desk', 'images/work_desk.png', "Working")
    dollar_gun = DollarGun()
    coffee_machine = CoffeeMachine("Aroma", 'images/barista.png', 'Coffee', CoffeeMachineSounds)
    football_table = FootballTable('FingerBall', 'images/football_table.png', 'play', TableFootballSounds)

    # Mall
    food_stand = ShopWindow("goods_stand", 15, Products.all_products, "images/stand.png", 'Price', ShopSounds)
    shopping_basket = RootObject('shopping_basket', 'images/shopping_basket.png')
    shopping_truck = RootObject('shopping_truck', 'images/shopping_truck.png')

    # Club
    bar = Bar('Kamikaze', 'images/bar.png', 'Cocktail', Products.all_cocktails)
    disco_ball = RootObject('disco_ball', 'images/disco_ball.png')
    left_speaker = RootObject('left_speaker', 'images/speaker.png')
    right_speaker = RootObject('right_speaker', 'images/speaker.png')
    adam = RootObject('Adam', 'images/human/bitmap.png')
    eva = RootObject('Eva', 'images/human/woman.png')
    bitch = Bitch('bitch', 300, 'drink_to_fuck', 0.1 * Values.wall_width, Values.roof_height * 3, WomanSprites, BitchSounds)

    # Window
    window = Window()

    # Pets shop
    pets_house = RootObject('pets house', 'images/pets_house.png')
    cat_house = RootObject('cat_house', 'images/cat_house.png')
    dog_house = RootObject('dog_house', 'images/dog_house.png')


class Player:
    player = Human('Mike', 'male', 'human', 501, 5 * Values.wall_width, 3 * Values.floor_height, HumanSprites, HumanSounds)


class MPC:
    sphinx = Cat('sphinx', 100, 'cat', 'sphinx', 30, 2 * Values.wall_width, Values.room_height - Values.floor_height, 8,
                 CatSprites, SoundExemplars.cat_sounds)

    pit_bull = Dog('pit-bull', 300, 'dog', 'pit-bull', 50, Values.wall_width, Values.room_height - Values.floor_height, 12,
                   DogSprites, SoundExemplars.dog_sounds)

    rip = Pet('dead', 0, 'dead', 'dead', 0, 0, 0, 0, RipSprite, None)

    susan = AnimalSeller('Susan', 320, 'woman', 6 * Values.wall_width, 3 * Values.floor_height, WomanSprites, 'no voice', [pit_bull, sphinx])

    bob = Cashier('Bob', 450, 'man', Values.wall_width * 5.5, 360, CashierSprites, 'no voice', [AdditionalObjects.food_stand])


class Rooms:
    flat_room = Room('Flat room', Doors.exit_door, {'window': AdditionalObjects.window, 'armchair': AdditionalObjects.armchair,
                                                    'table': AdditionalObjects.kitchen_table}, -1, 25)

    office = Room('office', Doors.exit_door, {'desk': AdditionalObjects.work_desk, 'coffee_machine': AdditionalObjects.coffee_machine,
                                              'football_table': AdditionalObjects.football_table}, 9, 18)

    products_shop_room = Room('Best-goods', Doors.automatic_door, {'cashier': MPC.bob,
                                                                   'shopping_basket': AdditionalObjects.shopping_basket,
                                                                   'shopping_truck': AdditionalObjects.shopping_truck}, 7, 23)

    pets_shop_room = Room("Susan's pets", Doors.exit_door, {'animal_seller': MPC.susan, 'pets_house': AdditionalObjects.pets_house,
                                                            'window': AdditionalObjects.window,
                                                            'cat_house': AdditionalObjects.cat_house,
                                                            'dog_house': AdditionalObjects.dog_house}, 9, 20)
    club_room = Room('Yes only', Doors.automatic_door, {'disco_ball': AdditionalObjects.disco_ball,
                                                        'bar': AdditionalObjects.bar,
                                                        'left_speaker': AdditionalObjects.left_speaker,
                                                        'right_speaker': AdditionalObjects.right_speaker,
                                                        'adam': AdditionalObjects.adam,
                                                        'eva': AdditionalObjects.eva,
                                                        'bitch': AdditionalObjects.bitch}, 20, 4)