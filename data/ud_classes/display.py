import pygame
from .values import Values
from .rgb import Colors
from .methods import AdditionalMethods
from .add_functions import AdditionalFunctions


class Display:
    @classmethod
    def create_window(cls):
        window = pygame.display.set_mode(Values.window_size)
        pygame.display.set_caption(Values.window_caption)
        return window


class Room:
    def __init__(self, name, door, objects, open_time, close_time):
        self.name = name
        # Details
        self.floor_area = AdditionalMethods.create_floor_area()
        self.roof_area = AdditionalMethods.create_roof_area()
        self.left_wall_area = AdditionalMethods.create_left_wall_area()
        self.right_wall_area = AdditionalMethods.create_right_wall_area()
        # Main block
        self.room_area = AdditionalMethods.create_room_area()
        self.door = door
        AdditionalMethods.collect_room(self.room_area, self.floor_area, self.roof_area,
                                       self.left_wall_area, self.right_wall_area)
        self.objects = objects
        self.open_time = open_time
        self.close_time = close_time

    def draw_me(self):
        AdditionalMethods.draw_room(self.room_area)

    def render(self, screen):
        screen.blit(self.room_area, (0, 0))

    def is_opened(self, clock):
        if self.open_time < self.close_time:
            if self.open_time <= clock.hours < self.close_time:
                return True
        else:
            if self.open_time <= clock.hours or clock.hours < self.close_time:
                return True
        return False


class World:
    def __init__(self, places):
        self.places = places
        self.area = AdditionalMethods.create_panel_area(Values.window_size)
        AdditionalMethods.add_places(self.area, places)
        self.sectors = AdditionalMethods.create_sectors_for_area(self.area, 4, 2)
        AdditionalMethods.compare_sectors_with_objects(self.sectors, self.places)

    def render(self, screen):
        AdditionalMethods.draw_sectors(self.area, self.sectors)
        screen.blit(self.area, (0, 0))


class ChoicePanel:
    def __init__(self, text, border_color, text_color, position):
        self.text = text
        self.font_size = Values.choice_panel_font_size
        self.border_color = border_color
        self.area = AdditionalMethods.draw_surface_box(AdditionalMethods.create_panel_area(Values.choice_panel_size),
                                                       self.border_color)
        self.text_color = text_color
        self.area = AdditionalMethods.put_text_to_box(self.area, self.text, self.font_size, self.text_color)
        self.x = position[0]
        self.y = position[1]

    def render(self, screen):
        screen.blit(self.area, (self.x, self.y))

    def change_text(self, text):
        self.text = text
        self.area.fill(Colors.snow)
        AdditionalMethods.draw_surface_box(self.area, Colors.black)
        AdditionalMethods.put_text_to_box(self.area, self.text, self.font_size, self.text_color)

    def invisible(self):
        self.area.set_alpha(0)

    def visible(self):
        self.area.set_alpha(200)

    def get_position(self):
        position = (self.x, self.y)
        return position


class TextPanel:
    def __init__(self, default_text, text_color, position):
        self.default_text = default_text
        self.area = AdditionalMethods.create_panel_area(Values.text_panel_size)
        self.text_color = text_color
        self.position = position
        self.x = position[0]
        self.y = position[1]

    def render(self, screen, add_text):
        self.area.fill(Colors.snow)
        screen.blit(self.area, (self.x, self.y))
        text_to_put = self.default_text
        text_to_put += add_text
        AdditionalMethods.put_text_to_box(self.area, text_to_put, 30, self.text_color)
        screen.blit(self.area, (self.x, self.y))

    def invisible(self):
        self.area.set_alpha(0)

    def visible(self):
        self.area.set_alpha(255)


class ImagesPanel:
    def __init__(self, images):
        self.area = AdditionalMethods.create_panel_area((100, 180))
        self.images = images
        self.area.fill(Colors.snow)
        #AdditionalMethods.draw_surface_box(self.area, Colors.black)

    def create_own_area(self, size):
        self.area = AdditionalMethods.create_panel_area(size)
        AdditionalMethods.draw_surface_box(self.area, Colors.black)

    def render(self, screen, position):
        screen.blit(self.area, position)

    def invisible(self):
        self.area.set_alpha(0)

    def visible(self):
        self.area.set_alpha(255)


class HPPanel:
    def __init__(self):
        self.area = AdditionalMethods.create_panel_area(Values.hp_panel_size)
        self.x = 0
        self.y = 0

    def adapt_for_unit(self, unit_area, width_k, height_k):
        unit_width = unit_area.get_width()
        unit_height = unit_area.get_height()
        #area_width = unit_width // 6
        #area_height = unit_height // 25
        #area_size = (area_width, area_height)
        self.area = AdditionalMethods.create_panel_area(Values.hp_panel_size)
        self.x = int(unit_width * width_k)
        self.y = int(unit_height * height_k)

    def get_position(self):
        return self.x, self.y

    def transparent(self):
        self.area.set_colorkey(Colors.black)

    def render(self, unit_area, unit_hp, unit_max_hp, fill_color):
        current_hp_color = AdditionalFunctions.get_current_hp_color(unit_hp, unit_max_hp)
        text_to_put = str(int(unit_hp))
        self.area.fill(fill_color)
        AdditionalMethods.put_text_to_box(self.area, text_to_put, 13, current_hp_color)
        AdditionalMethods.draw_surface_box(self.area, Colors.black)
        unit_area.blit(self.area, self.get_position())


class CashPanel:
    def __init__(self):
        self.area = AdditionalMethods.create_panel_area(Values.text_panel_size)
        self.x = 0
        self.y = 0

    def get_position(self):
        return self.x, self.y

    def adapt_for_unit(self, unit_area, width_k, height_k):
        unit_width = unit_area.get_width()
        unit_height = unit_area.get_height()
        area_width = unit_width // 4
        area_height = unit_height // 15
        area_size = (area_width, area_height)
        self.area = AdditionalMethods.create_panel_area(area_size)
        self.x = unit_width * width_k
        self.y = unit_height * height_k

    def render(self, unit_area, unit_money):
        text_to_put = str(unit_money)[0:4] + '$'
        self.area.fill(Colors.black)
        AdditionalMethods.put_text_to_box(self.area, text_to_put, 13, Colors.green)
        AdditionalMethods.draw_surface_box(self.area, Colors.black)
        unit_area.blit(self.area, self.get_position())


class ClockPanel:
    def __init__(self):
        self.width = 100
        self.height = self.width
        self.position = [Values.room_width // 2, Values.roof_height + self.height // 2]
        self.size = (self.width, self.height)
        self.area = AdditionalMethods.create_panel_area(self.size)
        self.day_area = AdditionalMethods.create_panel_area((self.width, self.height // 2))
        self.time_area = AdditionalMethods.create_panel_area((self.width, self.height // 2))
        self.seconds = 0
        self.minutes = 0
        self.hours = 9
        self.days = 0

    def go(self):
        if self.seconds < 59:
            self.seconds += 20
        else:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours < 24:
                    self.hours += 1
                else:
                    self.hours = 0
                    self.days += 1

    def render(self, screen):
        str_minutes = AdditionalFunctions.correct_str_time(self.minutes)
        dict_hours_ampm = AdditionalFunctions.correct_str_time_for_hours(self.hours)
        text_day = 'Day ' + str(self.days)
        text_time = dict_hours_ampm['hours'] + ':' + str_minutes + ' ' + dict_hours_ampm['am_or_pm']
        self.day_area.fill(Colors.snow)
        self.time_area.fill(Colors.snow)
        self.area.fill(Colors.snow)
        AdditionalMethods.put_text_to_box(self.day_area, text_day, 15, Colors.black)
        AdditionalMethods.put_text_to_box(self.time_area, text_time, 15, Colors.black)
        self.area.blit(self.day_area, (0, 5))
        self.area.blit(self.time_area, (0, self.height // 2 - 10))
        pygame.draw.circle(self.area, Colors.black, (self.width // 2, self.height // 2), self.height // 2, 3)
        self.area.set_alpha(230)
        screen.blit(self.area, self.position)


