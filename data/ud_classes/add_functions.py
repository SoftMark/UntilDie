from .storage import NamesStorage
from .values import Values
from .rgb import Colors
from .sprites import RipSprite
from .sounds import MainSounds
import random


class AdditionalFunctions:
    @classmethod
    def names_collector(cls, objects_array):
        names_array = []
        for obj in objects_array:
            names_array.append(obj.name)
        return names_array

    @classmethod
    def make_list(cls, names_array):
        list_text = ''
        i = 1
        for name in names_array:
            list_text += '\n' + str(i) + '.' + name
            i += 1
        return list_text

    @classmethod
    def hunger_damage(cls, player, FPS):
        hunger_damage = 1 / FPS * 2 / 500
        player.hp -= player.max_hp * hunger_damage
        player.mood -= 1 / FPS * 2 / 500
        if player.hp < 0:
            player.hp = 0
        for pet in player.pets.units:
            pet.hp -= pet.max_hp * hunger_damage
            if pet.hp < 0:
                pet.hp = 0
                cls.kill(pet)

    @classmethod
    def kill(cls, unit):
        if unit.bitmap != RipSprite.bitmap:
            unit.bitmap = RipSprite.bitmap
            unit.top_panel.change_text('Bury')
            unit.step = 0
            #MainSounds.rip_bell.play()

    @classmethod
    def rand_bool(cls, percentege=50):
        if int(percentege) == percentege:
            floating_count = 0
        else:
            floating_count = len(str(percentege).split(".")[-1])
            
        return random.randrange(1, 100 * 10 ** floating_count) <= percentege * 10 ** floating_count

    @classmethod
    def put_unit_to_place_holder(cls, unit, place_holder):
        if not cls.is_place_holder_full(place_holder):
            place_holder.units.append(unit)

    @classmethod
    def is_place_holder_empty(cls, place_holder):
        if len(place_holder.units) == 0:
            return True
        else:
            return False

    @classmethod
    def is_place_holder_full(cls, place_holder):
        if len(place_holder.units) == place_holder.capacity:
            return True
        else:
            return False

    @classmethod
    def get_current_hp_color(cls, hp, max_hp):
        if hp >= 0.8 * max_hp:
            current_hp_color = Colors.blue
        elif 0.3 * max_hp < hp < 0.8 * max_hp:
            current_hp_color = Colors.yellow
        # elif self.hp <= 0.3 * self.max_hp:
        else:
            current_hp_color = Colors.red
        return current_hp_color

    @classmethod
    def correct_str_time(cls, time):
        if time < 10:
            return "0" + str(time)
        else:
            return str(time)

    @classmethod
    def correct_str_time_for_hours(cls, hours):
        time_dict = {
            'hours': None,
            'am_or_pm': None
        }
        if hours < 13:
            time_dict['am_or_pm'] = 'am'
        else:
            time_dict['am_or_pm'] = 'pm'
            hours -= 12
        time_dict['hours'] = cls.correct_str_time(hours)
        return time_dict

    @classmethod
    def is_units_holder_full(cls, units_holder):
        if len(units_holder.units) == units_holder.capacity:
            answer = True
        else:
            answer = False
        return answer

    @classmethod
    def minus_half(cls, bigger, smaller):
        return (bigger - smaller) // 2

    @classmethod
    def are_they_closed(cls, they):
        answer = True
        for it in they:
            if it.condition is not NamesStorage.closed:
                answer = False
        return answer

    @classmethod
    def is_food_for_animal(cls, animal, food):
        if animal.kind == 'human':
            food_for_animal = food.for_human
        elif animal.kind == 'dog':
            food_for_animal = food.for_dog
        else:
            food_for_animal = food.for_cat
        return food_for_animal

