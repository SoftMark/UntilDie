from .colors import TColors
from .add_functions import AdditionalFunctions
from .storage import NamesStorage


class Product:
    def __init__(self, name, hp, price, kind):
        self.name = name
        self.hp = hp
        self.price = price
        self.kind = kind
        dict_for = {'human': True, 'dog': True, 'cat': True}
        if self.kind == 'sea-food':
            dict_for['dog'] = False
        elif self.kind in ['vegetable', 'fruit', 'alcohol-drink', 'sweet-drink']:
            dict_for['dog'] = False
            dict_for['cat'] = False
        self.for_human = dict_for['human']
        self.for_dog = dict_for['dog']
        self.for_cat = dict_for['cat']

    def get_product_hp(self):
        return self.hp


class Shop:
    def __init__(self, name, goods, good_kinds, stuff_kind):
        self.name = name
        self.goods = goods
        self.good_kinds = good_kinds
        self.stuff_kind = stuff_kind

    def get_in(self):
        print(TColors.blue + 'Welcome to ' + self.name + ' market!' + TColors.end)

    def print_goods(self):
        print('\nWhat would you like to buy?')
        i = 0
        for good_kind in self.good_kinds:
            print('\n' + TColors.blue + good_kind + 's' + TColors.end + ':')
            for good in self.goods:
                if good.kind == good_kind:
                    print('(' + str(i + 1) + ')' + TColors.pink + good.name + TColors.end + '(cost ' + TColors.blue +
                          str(good.price) + '$' + TColors.end + ').   ', end='')
                    i += 1
        print('\n\n(0)' + TColors.red + 'Exit\n' + TColors.end)

    def choose_goods(self):
        goods = []
        shop_run = True
        while shop_run:
            self.print_goods()
            goods_indexes_array = AdditionalFunctions.get_goods_indexes_array_to_buy()
            if goods_indexes_array:
                for good_index in goods_indexes_array:
                    if AdditionalFunctions.is_digital(good_index):
                        good_index = int(good_index)
                        if good_index <= len(self.goods):
                            if good_index == 0:
                                if len(goods_indexes_array) == 1:
                                    return 'Nothing chose'
                                else:
                                    continue
                            else:
                                goods.append(self.goods[good_index - 1])
                        else:
                            return 'Nothing chose'
                return goods


class Mall:
    def __init__(self, name, shops):
        self.name = name
        self.shops = shops

    def get_in(self):
        print(TColors.blue + 'Welcome to ' + self.name + ' mall!' + TColors.end)
        self.print_shops()

    def print_shops(self):
        shops_names = []
        for shop in self.shops:
            shops_names.append(shop.name)
        AdditionalFunctions.print_actions(shops_names)

    def choose_shop(self):
        while True:
            shop_choice = input()
            if AdditionalFunctions.is_digital(shop_choice):
                shop_choice = int(shop_choice)
                if shop_choice <= len(self.shops):
                    if shop_choice == 0:
                        return 'not found'
                    else:
                        return self.shops[shop_choice - 1]


class ProductShop(Shop):
    def __init__(self, name, goods):
        super().__init__(name, goods, good_kinds=NamesStorage.products_kinds, stuff_kind='products')


class PetShop(Shop):
    def __init__(self, name, goods):
        super().__init__(name, goods, good_kinds=NamesStorage.pet_kinds, stuff_kind='pets')


class TechnoShop(Shop):
    def __init__(self, name, goods):
        super().__init__(name, goods, good_kinds=NamesStorage.techno_kinds, stuff_kind='techno')


class UnitStorage:
    units = []

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


class SeparateStorage(UnitStorage):
    def __init__(self, name, capacity, price, kind, units):
        super().__init__(name, capacity)
        self.price = price
        self.kind = kind
        self.units = units
