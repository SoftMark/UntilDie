from .units import Objects, MainUnit
from .subjects import Dog, Cat
from .storage import NamesStorage
from .colors import TColors
from .add_functions import AdditionalFunctions


class SubjectMethods:
    @classmethod
    def create_human(cls):
        player_name = input(TColors.blue + "-What is your name?\n" + TColors.end)
        while True:
            print(TColors.blue + '-What is your gender?' + TColors.end)
            print('(1)' + TColors.blue + 'Male' + TColors.end + '\n(2)' + TColors.blue + 'Female' + TColors.end + '\n')
            load_choice = input()
            if AdditionalFunctions.is_digital(load_choice):
                load_choice = int(load_choice)
                if load_choice == 1:
                    player_gender = 'male'
                    player_hp = 700
                    break
                elif load_choice == 2:
                    player_gender = 'female'
                    player_hp = 550
                    break
        player = MainUnit.human
        player.name = player_name
        player.gender = player_gender
        player.max_hp = player_hp
        player.hp = player_hp
        player.pets[NamesStorage.dogs].units = []
        player.pets[NamesStorage.cats].units = []
        player.gender_details()
        return player

    @classmethod
    def load_pets(cls, human_data):
        dogs = []
        for dog_data in human_data[NamesStorage.pets][NamesStorage.dogs]:
            dog = Dog(dog_data[NamesStorage.p_name], dog_data[NamesStorage.p_max_hp], dog_data[NamesStorage.p_breed],
                      dog_data[NamesStorage.p_price])
            dog.hp = dog_data[NamesStorage.p_hp]
            dogs.append(dog)
        cats = []
        for cat_data in human_data[NamesStorage.pets][NamesStorage.cats]:
            cat = Cat(cat_data[NamesStorage.p_name], cat_data[NamesStorage.p_max_hp], cat_data[NamesStorage.p_breed],
                      cat_data[NamesStorage.p_price])
            cat.hp = cat_data[NamesStorage.p_hp]
            cats.append(cat)
        pets_dict = {
            NamesStorage.dogs: dogs,
            NamesStorage.cats: cats
        }
        return pets_dict

    @classmethod
    def player_loader(cls, human_data):
        # Data
        player_name = human_data[NamesStorage.human_name]
        player_gender = human_data[NamesStorage.human_gender]
        player_hp = human_data[NamesStorage.human_hp]
        player_max_hp = human_data[NamesStorage.human_max_hp]
        player_salary = human_data[NamesStorage.salary]
        player_money = human_data[NamesStorage.money]
        player_products = ObjectMethods.load_products(human_data)
        player_pets = cls.load_pets(human_data)
        # Object
        player = MainUnit.human
        player.name = player_name
        player.gender = player_gender
        player.hp = player_hp
        player.max_hp = player_max_hp
        player.salary = player_salary
        player.money = player_money
        player.refrigerator.units = player_products
        player.pets[NamesStorage.dogs].units = player_pets[NamesStorage.dogs]
        player.pets[NamesStorage.cats].units = player_pets[NamesStorage.cats]
        player.gender_details()
        return player


class ObjectMethods:
    @classmethod
    def load_products(cls, human_data):
        player_products = []
        for product_name in human_data[NamesStorage.products_names]:
            for product in Objects.all_products:
                if product.name == product_name:
                    player_products.append(product)
        return player_products
