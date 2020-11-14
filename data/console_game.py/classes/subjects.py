import random
import copy
from .colors import TColors
from .add_functions import AdditionalFunctions
from .storage import NamesStorage



class Animal:
    def __init__(self, name, hp, kind):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.kind = kind

    def print_total_hp(self):
        if self.hp > 0:
            print(self.kind + ' ' + self.name + "'s hp: ", end='')
            current_hp_color = AdditionalFunctions.get_current_hp_color(self.hp, self.max_hp)
            print(current_hp_color + str(self.hp) + TColors.end + '/' + TColors.green + str(
                self.max_hp) + TColors.end + ' ')
            AdditionalFunctions.print_hp_bar(self.hp, self.max_hp, current_hp_color)
        else:
            AdditionalFunctions.print_rip(self.name, self.kind)

    def print_name(self):
        print('This is ' + self.kind + ' ' + TColors.blue + self.name + TColors.end + '.')

    def generate_hunger_dmg(self):
        hunger_dmg = random.randrange(int(self.max_hp * 0.1), int(self.max_hp * 0.2))
        return int(hunger_dmg)

    def get_hunger_dmg(self):
        self.hp -= self.generate_hunger_dmg()
        if self.hp <= 0:
            self.hp = 0

    def is_food_for_animal(self, food):
        if self.kind == 'human':
            food_for_animal = food.for_human
        elif self.kind == 'dog':
            food_for_animal = food.for_dog
        else:
            food_for_animal = food.for_cat
        return food_for_animal

    @classmethod
    def to_eat_or_to_drink(cls, food):
        if 'drink' in food.kind:
            yum = 'drunk'
        else:
            yum = 'ate'
        return yum

    def eat(self, food):
        if self.is_food_for_animal(food):
            self.hp += food.hp
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            yum = self.to_eat_or_to_drink(food)
            print(TColors.blue + self.name + ' ' + yum + ' ' + food.name + TColors.end + TColors.green +
                  ' +' + str(food.hp) + 'hp' + TColors.end)
        else:
            print(TColors.blue + "Bruh, " + self.kind + " can't eat that." + TColors.end)
            print(TColors.red + 'You just lost ' + food.name + '.' + TColors.end)

    def eat_more(self, products):
        for product in products:
            # I am full hp baby
            if self.hp == self.max_hp:
                print(TColors.red + self.name + " does not want to eat, just lost " + product.name + TColors.end)
                break
            self.eat(product)


class Human(Animal):
    he_she = 'It'
    his_her = 'Its'
    salary = 5.25
    max_salary = 12
    money = 700

    def __init__(self, name, gender, hp, refrigerators_corner, dogs_corner, cats_corner):
        super().__init__(name, hp, kind='human')
        # Gender things
        self.gender = gender
        # Storage
        self.refrigerators_corner = refrigerators_corner
        self.pets = {
            NamesStorage.dogs: dogs_corner,
            NamesStorage.cats: cats_corner
        }

    def gender_details(self):
        if self.gender == 'male':
            self.he_she = 'He'
            self.his_her = 'His'
        elif self.gender == 'female':
            self.he_she = 'She'
            self.his_her = 'Her'
        else:
            self.he_she = 'It'
            self.his_her = 'Its'

    # Pets

    def check_pets(self):
        pet_kinds = [NamesStorage.dogs, NamesStorage.cats]
        for pet_kind in pet_kinds:
            for pet in self.pets[pet_kind].units:
                if AdditionalFunctions.get_current_hp_color(pet.hp, pet.max_hp) == TColors.red:
                    # Pet is hungry
                    if pet.hp > 0:
                        print(TColors.red + self.name + ' has to feed that ' + pet.kind + '!' + TColors.end)
                        pet.print_total_hp()
                    # Pet is dead
                    else:
                        pet.print_total_hp()
                else:
                    # It's ok
                    pass

    def actions_with_pets(self):
        while True:
            pet_kind = self.choose_pet_kind()
            if pet_kind == 'exit':
                break
            elif pet_kind in [NamesStorage.dogs, NamesStorage.cats]:
                pet = self.choose_pet(pet_kind)
                if type(pet) in [Cat, Dog]:
                    self.actions_with_pet(pet)
                continue

    def actions_with_pet(self, pet):
        while True:
            actions = self.get_actions_with_pet(pet)
            act_choice = input()
            if AdditionalFunctions.is_digital(act_choice):
                act_choice = int(act_choice)
                if 0 <= act_choice <= len(actions):
                    if act_choice == 0:
                        break
                    elif act_choice == 1:
                        self.feed_pet(pet)
                    elif act_choice == 2:
                        self.rename_pet(pet)
                    elif act_choice == 3:
                        self.bury_pet(pet)
                        break

    def choose_pet(self, pet_kind):
        # Array of that pet kind units empty
        if len(self.pets[pet_kind].units) == 0:
            print(TColors.red + self.name + " does not have any " + pet_kind + TColors.end)
            input(TColors.blue + 'Press enter to continue' + TColors.end)
            return 'pet not found'
        # Choosing pet
        else:
            while True:
                self.print_pets_info(pet_kind)
                pet_choice = input()
                # Is chose input correct
                if AdditionalFunctions.is_digital(pet_choice):
                    pet_choice = int(pet_choice)
                    if 0 <= pet_choice <= len(self.pets[pet_kind].units):
                        if pet_choice == 0:
                            break
                        else:
                            # Chose pet
                            return self.pets[pet_kind].units[pet_choice - 1]

    def print_pets_info(self, pet_kind):
        print('\n\n\n\n' + self.name + "'s " + TColors.pink + pet_kind + ":\n" + TColors.end)
        for pet in self.pets[pet_kind].units:
            pet.print_info()
            print()
        i = 1
        for pet in self.pets[pet_kind].units:
            print('(' + str(i) + ')' + TColors.blue + 'Choose ' + pet.name + TColors.end)
            i += 1
        print("\n(0)" + TColors.red + "Back" + TColors.end)

    def feed_pet(self, pet):
        # Actually if pet dead, it's unable to feed it
        if pet.hp == 0:
            print(TColors.red + self.name + " can't feed dead pet." + TColors.end)
        else:
            # Lets see what we have in our refrigerator
            food = self.get_products_to_eat(self.choose_refrigerator())
            if food != "not found":
                for product in food:
                    # Take it my little mfk
                    pet.eat(product)

    def bury_pet(self, pet):
        # Lets put that mfk into the grave(Just del from its array)
        self.pets[pet.kind + 's'].units.remove(pet)
        print(TColors.blue + self.name + ' just bury ' + pet.name + TColors.end)

    @classmethod
    def rename_pet(cls, pet):
        # I decide what is your name mfk
        print(TColors.blue + 'Which name would you like?' + TColors.end)
        pet.name = str(input())

    @classmethod
    def choose_pet_kind(cls):
        actions = [NamesStorage.dogs, NamesStorage.cats]
        while True:
            AdditionalFunctions.print_actions(actions)
            pet_choice = input()
            if AdditionalFunctions.is_digital(pet_choice):
                pet_choice = int(pet_choice)
                if 0 <= pet_choice <= len(actions):
                    print(pet_choice)
                    # Don't need to choose pet anymore
                    if pet_choice == 0:
                        return 'exit'
                    else:
                        # Dogs chose
                        if pet_choice == 1:
                            pet_kind = actions[pet_choice - 1]
                        # Cats chose
                        else:
                            pet_kind = actions[pet_choice - 1]
                        return pet_kind

    @classmethod
    def get_actions_with_pet(cls, pet):
        # Lets see our mfk
        pet.print_info()
        actions = ['Feed', 'Rename']
        # Damn I guess it's dead
        if pet.hp == 0:
            actions.append('Bury')
        # Lets see what can we do
        AdditionalFunctions.print_actions(actions)
        return actions

    # Refrigerator

    def go_to_refrigerators_corner(self):
        while True:
            if self.check_refrigerators_corner() == "no refrigerators":
                break
            else:
                self.print_total_hp()
                refrigerator = self.choose_refrigerator()
                if refrigerator == 'exit':
                    break
                self.print_total_hp()
                # Hmm, to eat or not to eat, that is the question!
                products_to_eat = self.get_products_to_eat(refrigerator)
                # Nuh..
                if products_to_eat in ["nuh", "refrigerator is empty"]:
                    break
                # Come here yummy thing
                else:
                    self.eat_more(products_to_eat)

    def print_own_refrigerators(self):
        own_refrigerator_names = []
        # Getting refrigerator names
        for refrigerator in self.refrigerators_corner.units:
            own_refrigerator_names.append(refrigerator.name)
        AdditionalFunctions.print_actions(own_refrigerator_names)

    @classmethod
    def check_refrigerator(cls, refrigerator):
        if len(refrigerator.units) == 0:
            return "empty"
        else:
            return "not empty"

    def check_refrigerators_corner(self):
        if len(self.refrigerators_corner.units) == 0:
            print(TColors.red + self.name + " does not have any refrigerators" + TColors.end)
            input(TColors.blue + "Press Enter to continue" + TColors.end)
            return "no refrigerators"
        else:
            return "refrigerators founded"

    def choose_refrigerator(self):
        while True:
            self.print_own_refrigerators()
            ref_choice = input()
            if AdditionalFunctions.is_digital(ref_choice):
                ref_choice = int(ref_choice)
                if 0 <= ref_choice <= len(self.refrigerators_corner.units):
                    # Don't need to choose refrigerator anymore
                    if ref_choice == 0:
                        return 'exit'
                    return self.refrigerators_corner.units[ref_choice - 1]

    def get_products_to_eat(self, refrigerator):
        if self.check_refrigerator(refrigerator) == "not empty":
            while True:
                self.print_ref_products(refrigerator)
                print("(0)" + TColors.red + "Back" + TColors.end)
                products_indexes_array = AdditionalFunctions.get_goods_indexes_array_to_eat()
                # Close refrigerator
                if products_indexes_array == [0]:
                    return "nuh"
                else:
                    products_to_eat = self.get_products_and_indexes(products_indexes_array, refrigerator)["products"]
                    products_indexes_array = self.get_products_and_indexes(products_indexes_array, refrigerator)[
                        "indexes"]
                    # Delete
                    refrigerator.units = AdditionalFunctions.del_array_elements_by_indexes(refrigerator.units,
                                                                                           products_indexes_array)
                    print('\n\n')
                    return products_to_eat
        else:
            # Damn, it's empty
            print(TColors.red + refrigerator.name + ' is empty.' + TColors.end)
            input(TColors.blue + 'Press enter to continue' + TColors.end)
            return "refrigerator is empty"

    @classmethod
    def get_products_and_indexes(cls, products_indexes_array, refrigerator):
        products_to_eat = []
        for product_index in products_indexes_array:
            if product_index <= len(refrigerator.units):
                # Zero is not a correct index
                if product_index == 0:
                    del product_index
                    continue
                # It's ok
                else:
                    product_to_eat = refrigerator.units[product_index - 1]
                    products_to_eat.append(product_to_eat)
        return {
            "products": products_to_eat,
            "indexes": products_indexes_array
        }

    @classmethod
    def print_ref_products(cls, refrigerator):
        print(TColors.blue + refrigerator.name + ':' + TColors.end)
        if len(refrigerator.units) == 0:
            print(TColors.red + 'Refrigerator is empty!' + TColors.end)
        else:
            i = 1
            for product in refrigerator.units:
                if i % 6 == 0:
                    print()
                print('(' + str(i) + ')' + TColors.pink + product.name + '  ' + TColors.end, end='')
                i += 1
        print()

    def print_own_products(self):
        if len(self.refrigerators_corner.units) == 0:
            print(TColors.red + self.name + " does not have any refrigerators" + TColors.end)
        else:
            print(self.his_her + ' products:')
            for refrigerator in self.refrigerators_corner.units:
                self.print_ref_products(refrigerator)

    # Print

    def print_info(self):
        self.print_name()
        self.print_money()
        print()
        self.print_total_hp()
        self.check_pets()
        self.print_own_products()
        print('\n')

    def say_own_name(self):
        print('My name is ' + self.name)

    def print_money(self):
        print(self.name + ' earned ' + TColors.blue + str(self.salary - 0.25) + '$' + TColors.end + ' last day.')
        print(self.he_she + ' has ' + TColors.blue + str(self.money) + '$.' + TColors.end)

    def print_total_cash(self):
        print('Total cash ' + TColors.blue + str(self.money) + '$' + TColors.end)

    # Actions

    def work(self):
        self.money += self.salary
        if self.salary < 12:
            self.salary += 0.25
        self.get_hunger_dmg()
        for dog in self.pets[NamesStorage.dogs].units:
            dog.get_hunger_dmg()
        for cat in self.pets[NamesStorage.cats].units:
            cat.get_hunger_dmg()

    def go_to_mall(self, mall):
        mall.get_in()
        shop = mall.choose_shop()
        if shop == 'not found':
            return "exit mall"
        else:
            self.go_to_market(shop)

    def go_to_market(self, market):
        market.get_in()
        shop_run = True
        while shop_run:
            self.print_total_cash()
            shop_stuff = market.choose_goods()
            if shop_stuff == 'Nothing chose':
                break
            place_to_put = self.determine_place_to_put(shop_stuff)
            if place_to_put != 'not found':
                if self.check_place_to_put(place_to_put, len(shop_stuff)) == 'not enough place':
                    continue
                else:
                    bought_stuff = self.buy(shop_stuff)
                    self.put_goods_to_place(place_to_put, bought_stuff)

    def determine_place_to_put(self, shop_stuff):
        shop_stuff_example = shop_stuff[0]
        if shop_stuff_example.kind in NamesStorage.products_kinds:
            if self.check_refrigerators_corner() == "no refrigerators":
                put_to = 'not found'
            else:
                refrigerator = self.choose_refrigerator()
                if refrigerator == 'exit':
                    put_to = 'not found'
                else:
                    put_to = refrigerator
        elif shop_stuff_example.kind in NamesStorage.techno_kinds:
            put_to = self.refrigerators_corner
        elif shop_stuff_example.kind in NamesStorage.pet_kinds:
            put_to = self.pets[shop_stuff_example.kind + 's']
        else:
            put_to = 'not found'
        return put_to

    @classmethod
    def check_place_to_put(cls, place_to_put, stuff_quantity):
        if len(place_to_put.units) + stuff_quantity > place_to_put.capacity:
            check = 'not enough place'
            print(TColors.red + "It's not enough place in " + place_to_put.name + '.' + TColors.end)
        else:
            check = 'enough place'
        return check

    def buy(self, shop_stuff):
        bought_stuff = []
        spent_money = 0
        for stuff in shop_stuff:
            if stuff.price > self.money:
                print(TColors.red + self.name + ' does not  have enough money for ' + stuff.name + TColors.end)
                break
            else:
                bought_stuff.append(copy.deepcopy(stuff))
                self.money -= stuff.price
                spent_money += stuff.price
        self.print_bought_stuff(bought_stuff, spent_money)
        return bought_stuff

    def print_bought_stuff(self, bought_stuff, spent_money):
        print(TColors.blue + self.name + ' just bought:' + TColors.end)
        i = 1
        for stuff in bought_stuff:
            if i % 6 == 0:
                print()
            print(TColors.pink + stuff.name + TColors.end, end=' and ')
            i += 1
        print("spent " + TColors.red + str(spent_money) + '$' + TColors.end)

    @classmethod
    def put_goods_to_place(cls, place_to_put, bought_stuff):
        for stuff in bought_stuff:
            print(TColors.underline + 'put ' + stuff.name + ' to ' + place_to_put.name + TColors.end)
            place_to_put.units.append(stuff)


class Pet(Animal):
    def __init__(self, name, hp, breed, price):
        super().__init__(name, hp, kind='pet')
        self.breed = breed
        self.price = price

    def print_breed(self):
        print('Its breed is ' + TColors.pink + self.breed + TColors.end + '.')

    def print_info(self):
        self.print_name()
        self.print_breed()
        self.print_total_hp()


class Dog(Pet):
    def __init__(self, name, hp, breed, price):
        super().__init__(name, hp, breed, price)
        self.kind = 'dog'


class Cat(Pet):
    def __init__(self, name, hp, breed, price):
        super().__init__(name, hp, breed, price)
        self.kind = 'cat'
