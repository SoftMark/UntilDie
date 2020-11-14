from .colors import TColors
from .storage import Loader, NamesStorage
import os
import re


class AdditionalFunctions:
    @classmethod
    def is_digital(cls, var):
        try:
            float(var)
            bul = True
        except ValueError:
            bul = False
        return bul

    @classmethod
    def ask_to_save(cls, data_to_save):
        while True:
            print(TColors.blue + '-Do you want to save?' + TColors.end)
            print('(1)' + TColors.green + 'Yes' + TColors.end + '\n(2)' + TColors.red + 'Delete the save' + TColors.end
                  + '\n\n' + '(0)' + TColors.blue + "Exit")
            save_choice = input()
            if cls.is_digital(save_choice):
                save_choice = int(save_choice)
                if save_choice == 2:
                    Loader.clear_data()
                    print(TColors.red + 'Saves have been deleted' + TColors.end)
                elif save_choice == 1:
                    Loader.save_data(data_to_save)
                    print(TColors.green + 'Game saved' + TColors.end)
                break

    @classmethod
    def exit_game(cls, human, day):
        print(TColors.blue + '-Are you sure?' + TColors.end)
        print('(1)' + TColors.green + 'Yes' + TColors.end + '\n(2)' + TColors.red + 'No' + TColors.end + '\n')
        exit_choice = input()
        if cls.is_digital(exit_choice):
            exit_choice = int(exit_choice)
            if exit_choice == 1:
                data_to_save = cls.data_collector(human, day)
                cls.ask_to_save(data_to_save)
                print(TColors.red + 'Game over.' + TColors.end)
                return False
        return True

    @classmethod
    def ask_to_continue(cls):
        if os.path.isfile(NamesStorage.load_way) and os.stat(NamesStorage.load_way).st_size != 0:
            while True:
                print(TColors.blue + '-Do you want to continue?' + TColors.end)
                print('(1)' + TColors.green + 'Yes' + TColors.end + '\n(2)' + TColors.red + 'No' + TColors.end + '\n')
                load_choice = input()
                if cls.is_digital(load_choice):
                    load_choice = int(load_choice)
                    if load_choice == 2:
                        return False
                    elif load_choice == 1:
                        return True
        return False

    @classmethod
    def data_collector(cls, human, day):
        # Collects pets data
        dogs_data = cls.collect_pets_data(human, NamesStorage.dogs)
        cats_data = cls.collect_pets_data(human, NamesStorage.cats)
        # Collects product names array
        products_data = cls.collects_product_names(human)
        # Creates dict of data to save
        data_to_save ={
            'day': day,
            'human':
                {
                    NamesStorage.human_name: human.name,
                    NamesStorage.human_gender: human.gender,
                    NamesStorage.human_hp: human.hp,
                    NamesStorage.human_max_hp: human.max_hp,
                    NamesStorage.salary: human.salary,
                    NamesStorage.money: human.money,
                    NamesStorage.pets:
                        {
                            NamesStorage.dogs: dogs_data,
                            NamesStorage.cats: cats_data,
                        },
                    NamesStorage.products_names: products_data

                }
        }
        return data_to_save

    @classmethod
    def collect_pets_data(cls, human, pet_kind):
        pets_data = []
        for pet in human.pets[pet_kind].units:
            pet_data = {
                NamesStorage.p_name: pet.name,
                NamesStorage.p_hp: pet.hp,
                NamesStorage.p_max_hp: pet.max_hp,
                NamesStorage.p_breed: pet.breed,
                NamesStorage.p_price: pet.price
            }
            pets_data.append(pet_data)
        return pets_data

    @classmethod
    def collects_product_names(cls, human):
        products_names = []
        for product in human.refrigerator.units:
            products_names.append(product.name)
        return products_names

    @classmethod
    def print_day(cls, day):
        print(TColors.bold + TColors.pink + "---------" + TColors.end)
        print(TColors.pink + "| " + TColors.bold + "Day " + str(day) + TColors.end + TColors.pink + " |" + TColors.end)
        print(TColors.bold + TColors.pink + "---------" + TColors.end)

    @classmethod
    def replace_parts_in_string(cls, to_del, to_put, string):
        return re.sub(to_del, to_put, string)

    @classmethod
    def get_goods_indexes_array_to_buy(cls):
        goods_indexes_array = []
        str_goods_indexes_array = (cls.replace_parts_in_string('[^0-9]', ' ', input())).split()
        for str_good_index in str_goods_indexes_array:
            goods_indexes_array.append(int(str_good_index))
        return goods_indexes_array

    @classmethod
    def get_goods_indexes_array_to_eat(cls):
        goods_indexes_array = []
        str_goods_indexes_array = (cls.replace_parts_in_string('[^0-9]', ' ', input())).split()
        for str_good_index in str_goods_indexes_array:
            goods_indexes_array.append(int(str_good_index))
        goods_indexes_set = set(goods_indexes_array)
        goods_indexes_array = cls.array_from_set(goods_indexes_set)
        return goods_indexes_array

    @classmethod
    def del_array_elements_by_indexes(cls, array, indexes):
        new_array = []
        i = 0
        for el in array:
            if i + 1 in indexes:
                i += 1
                continue
            new_array.append(el)
            i += 1
        return new_array

    @classmethod
    def print_actions(cls, actions):
        print('Choose action:')
        i = 1
        for action in actions:
            print('(' + str(i) + ')' + TColors.blue + action + TColors.end)
            i += 1
        print("\n(0)" + TColors.red + "Back" + TColors.end)

    @classmethod
    def print_hp_bar(cls, hp, max_hp, current_hp_color):
        hp_bar_len = 20
        hp_bar = ''
        # print('_' * (hp_bar_len + 2) + '\n|', end='')
        print('|', end='')
        hp_bar_points = int(hp / max_hp * hp_bar_len)
        while hp_bar_points > 0:
            hp_bar += current_hp_color + '█' + TColors.end
            hp_bar_points -= 1
        while len(hp_bar) / 10 < hp_bar_len:  # 10 because of TColors
            hp_bar += current_hp_color + '░' + TColors.end
        print(hp_bar + '|\n')

    @classmethod
    def get_current_hp_color(cls, hp, max_hp):
        if hp >= 0.8 * max_hp:
            current_hp_color = TColors.green
        elif 0.3 * max_hp < hp < 0.8 * max_hp:
            current_hp_color = TColors.yellow
        # elif self.hp <= 0.3 * self.max_hp:
        else:
            current_hp_color = TColors.red
        return current_hp_color

    @classmethod
    def print_rip(cls, name, kind):
        print(TColors.bold + TColors.red + "---------" +
              len(kind) * "-" + len(name) * "-" + TColors.end)
        print(TColors.red + "| " + TColors.bold + "RIP " + kind, name + TColors.end + TColors.red
              + " |" + TColors.end)
        print(TColors.bold + TColors.red + "---------" +
              len(kind) * "-" + len(name) * "-" + TColors.end)

    @classmethod
    def array_from_set(cls, set):
        array = []
        for set_val in set:
            array.append(set_val)
        return  array

