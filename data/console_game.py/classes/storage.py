import json
from enum import Enum


class Loader:
    @classmethod
    def save_data(cls, data_to_save):
        save_file = open(NamesStorage.load_way, 'w+')
        save_file.seek(0)
        save_file.write(json.dumps(data_to_save))

    @classmethod
    def load_data(cls):
        load_file = open(NamesStorage.load_way, 'r+')
        loaded_data = json.loads(load_file.read())
        return loaded_data

    @classmethod
    def clear_data(cls):
        save_file = open(NamesStorage.load_way, 'w+')
        save_file.seek(0)


class NamesStorage:
    human_name = "name"
    human_hp = "hp"
    human_max_hp = 'max hp'
    human_gender = "human's gender"
    salary = 'current salary'
    money = 'current money'
    refrigerator_size = "refrigerator size"
    pets_place_size = "pets place size"
    # Pets
    pets = "pets"
    dogs = "dogs"
    cats = "cats"
    p_name = "pet name"
    p_hp = "pet hp"
    p_max_hp = "pet max hp"
    p_breed = "pet breed"
    p_price = "pet price"
    # Products
    products_names = "products' names array"
    # Links
    load_way = 'storage/storage.json'
    # Arrays
    products_kinds = ['bakery', 'sea-food', 'meat', 'vegetable', 'fruit',
                      'alcohol-drink', 'sweet-drink', 'natural-drink']
    pet_kinds = ['cat', 'dog']
    techno_kinds = ['saturn', 'samsung']
    main_actions = ['Work', 'Eat', 'Pets', 'Go to Mall', 'Save']



