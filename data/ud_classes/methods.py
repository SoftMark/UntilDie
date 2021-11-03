import pygame
from .rgb import Colors
from .values import Values
from .storage import NamesStorage
# from .display import Sector
from pygame.locals import *
from .sounds import SectorsSounds


class Sector:
    def __init__(self, sector_size, sector_position, obj, name):
        self.sector_size = sector_size
        self.position = sector_position
        self.obj = obj
        self.area = AdditionalMethods.create_panel_area(self.sector_size)
        self.name = name
        self.condition = 'sleep'

    def draw_my_obj(self):
        AdditionalMethods.draw_image_on_area_centre(self.area, self.obj.bitmap)

    def render(self, area):
        if self.condition == 'sleep':
            self.sleep()
        elif self.condition == 'response':
            self.response()
        if self.obj is not None:
            self.draw_my_obj()
        else:
            self.area.fill(Colors.snow)
        area.blit(self.area, self.position)

    def response(self):
        AdditionalMethods.draw_surface_box(self.area, Colors.black)

    def sleep(self):
        AdditionalMethods.draw_surface_box(self.area, Colors.snow)


class AdditionalMethods:
    @classmethod
    def create_room_area(cls):
        room_area = pygame.Surface(Values.room_size)
        room_area.fill(Colors.snow)
        return room_area

    @classmethod
    def create_floor_area(cls):
        floor_area = pygame.Surface(Values.floor_size)
        floor_area.fill(Colors.snow)
        floor_area.set_alpha(0)
        return floor_area

    @classmethod
    def create_roof_area(cls):
        roof_area = pygame.Surface(Values.roof_size)
        roof_area.fill(Colors.snow)
        roof_area.set_alpha(0)
        return roof_area

    @classmethod
    def create_left_wall_area(cls):
        left_wall_area = pygame.Surface(Values.wall_size)
        left_wall_area.fill(Colors.snow)
        left_wall_area.set_alpha(0)
        return left_wall_area

    @classmethod
    def create_right_wall_area(cls):
        right_wall_area = pygame.Surface(Values.wall_size)
        right_wall_area.fill(Colors.snow)
        right_wall_area.set_alpha(0)
        return right_wall_area

    @classmethod
    def create_panel_area(cls, panel_size):
        choice_panel_area = pygame.Surface(panel_size)
        choice_panel_area.fill(Colors.snow)
        return choice_panel_area

    @classmethod
    def draw_surface_box(cls, surface, color):
        pygame.draw.aaline(surface, color, [0, 0],
                           [surface.get_width(), 0])
        pygame.draw.aaline(surface, color, [0, 0],
                           [0, surface.get_height()])
        pygame.draw.aaline(surface, color, [0, surface.get_height() - 1],
                           [surface.get_width(), surface.get_height() - 1])
        pygame.draw.aaline(surface, color, [0, surface.get_height() - 1],
                           [surface.get_width(), surface.get_height() - 1])
        pygame.draw.aaline(surface, color, [surface.get_width() - 1, 0],
                           [surface.get_width() - 1, surface.get_height() - 1])

        return surface

    @classmethod
    def put_text_to_box(cls, panel, text, font_size, color):
        pygame.init()
        text_space = pygame.font.Font('fonts/freesansbold.ttf', font_size)
        text_area = text_space.render(text, 1, color)
        panel.blit(text_area, ((panel.get_width() - text_area.get_width()) // 2,
                               (panel.get_height() - text_area.get_height()) // 2 + 1))
        return panel

    @classmethod
    def draw_room(cls, room_area):
        # Horizontals - -
        pygame.draw.aaline(room_area, Colors.black, [Values.wall_width, Values.roof_height],
                           [Values.room_width - Values.wall_width, Values.roof_height])
        pygame.draw.aaline(room_area, Colors.black, [Values.wall_width, Values.room_height - Values.floor_height],
                           [Values.room_width - Values.wall_width, Values.room_height - Values.floor_height])
        # Verticals | |
        pygame.draw.aaline(room_area, Colors.black, [Values.wall_width, Values.roof_height],
                           [Values.wall_width, Values.room_height - Values.floor_height])
        pygame.draw.aaline(room_area, Colors.black, [Values.room_width - Values.wall_width, Values.roof_height],
                           [Values.room_width - Values.wall_width, Values.room_height - Values.floor_height])
        # Diagonals / / \ \
        pygame.draw.aaline(room_area, Colors.black, [0, 0],
                           [Values.wall_width, Values.roof_height])
        pygame.draw.aaline(room_area, Colors.black,
                           [Values.room_width - Values.wall_width, Values.room_height - Values.floor_height],
                           [Values.room_width, Values.room_height])
        pygame.draw.aaline(room_area, Colors.black,
                           [Values.room_width - Values.wall_width, Values.roof_height],
                           [Values.room_width, 0])
        pygame.draw.aaline(room_area, Colors.black,
                           [Values.wall_width, Values.room_height - Values.floor_height],
                           [0, Values.room_height])

    @classmethod
    def collect_room(cls, room_area, floor_area, roof_area, left_wall_area, right_wall_area):
        room_area.blit(left_wall_area, Values.left_wall_position)
        room_area.blit(right_wall_area, Values.right_wall_position)
        room_area.blit(roof_area, Values.roof_position)
        room_area.blit(floor_area, Values.floor_position)

    @classmethod
    def draw_border(cls, surface, color):
        pygame.draw.aaline(surface, color, [0, 0],
                           [surface.get_width(), 0])
        pygame.draw.aaline(surface, color, [0, 0],
                           [0, surface.get_height()])
        pygame.draw.aaline(surface, color, [0, surface.get_height() - 1],
                           [surface.get_width(), surface.get_height() - 1])
        pygame.draw.aaline(surface, color, [0, surface.get_height() - 1],
                           [surface.get_width(), surface.get_height() - 1])
        pygame.draw.aaline(surface, color, [surface.get_width() - 1, 0],
                           [surface.get_width() - 1, surface.get_height() - 1])

    @classmethod
    def add_objects_images_to_panel_area(cls, panel_area, objects, capacity, img_in_line):
        panel_area.fill(Colors.snow)
        if len(objects) > 0:
            images = cls.get_images_array_from_objects(objects)
            lines = capacity // img_in_line
            columns = img_in_line
            step_x = images[0].get_width() // 2
            step_y = images[0].get_height() // 2
            padding_x = (panel_area.get_width() - columns * (images[0].get_width() + step_x)) // 2
            padding_y = (panel_area.get_height() - lines * (images[0].get_height() + step_y)) // 4
            x = padding_x
            y = padding_y
            i = 1
            for obj in objects:
                obj.render(panel_area, (x, y))
                x += obj.bitmap.get_width() + step_x
                if i % columns == 0:
                    y += obj.bitmap.get_height() + step_y
                    x = padding_x
                    # pygame.draw.aaline(panel_area, Colors.black, [0, y], [panel_area.get_width() - 1, y])
                i += 1

    @classmethod
    def get_images_array_from_objects(cls, objects):
        images = []
        for obj in objects:
            images.append(obj.bitmap)
        return images

    @classmethod
    def draw_horizontals(cls, area, horizontals_capacity):
        y_step = area.get_height() // horizontals_capacity
        y = y_step
        for horizontal in range(0, horizontals_capacity):
            pygame.draw.aaline(area, Colors.black, [0, y], [area.get_width() - 1, y])
            y += y_step

    @classmethod
    def is_mouse_pos_in_area(cls, area, area_pos):
        pos = pygame.mouse.get_pos()
        if area_pos[0] < pos[0] < area_pos[0] + area.get_width():
            if area_pos[1] < pos[1] < area_pos[1] + area.get_height():
                return True
        else:
            return False

    @classmethod
    def is_mouse_pos_in_unit_area(cls, unit):
        if cls.is_mouse_pos_in_area(unit.area, unit.get_position()):
            return True
        else:
            return False

    @classmethod
    def is_mouse_pos_in_top_panel_area(cls, top_panel_carrier):
        if cls.is_mouse_pos_in_area(top_panel_carrier.top_panel.area, top_panel_carrier.top_panel.get_position()):
            return True
        else:
            return False

    @classmethod
    def action_with_unit(cls, player, unit):
        if cls.is_in_response_range(player, unit):
            if cls.is_mouse_pos_in_top_panel_area(unit):
                return True
        return False

    @classmethod
    def add_places(cls, area, places):
        cls.add_objects_images_to_panel_area(area, places, 4, 2)

    @classmethod
    def create_sectors_for_area(cls, area, sectors_quantity, in_a_raw):
        sectors = []
        sectors_in_a_raw = in_a_raw
        columns = sectors_in_a_raw
        strings = sectors_quantity // sectors_in_a_raw
        if strings == 0:
            strings = 1
        sector_width = area.get_width() // sectors_in_a_raw
        sector_height = area.get_height() // strings
        sector_size = (sector_width, sector_height)

        x_start = 0
        y_start = 0
        x_step = area.get_width() // columns
        y_step = area.get_height() // strings

        x = x_start
        y = y_start
        for string in range(strings):
            for column in range(columns):
                new_sector = Sector(sector_size, (x, y), None, 'sector')
                sectors.append(new_sector)
                x += x_step
            x = x_start
            y += y_step
        return sectors

    @classmethod
    def draw_sectors(cls, area, sectors):
        for sector in sectors:
            sector.area.fill(Colors.snow)
            sector.render(area)

    @classmethod
    def compare_sectors_with_objects(cls, sectors, objects):
        i = 0
        for sector in sectors:
            try:
                sector.obj = objects[i]
                sector.name = objects[i].name
            except:
                sector.obj = None
                sector.name = 'sector'
            i += 1

    @classmethod
    def draw_image_on_area_centre(cls, area, img):
        x = (area.get_width() - img.get_width()) // 2
        y = (area.get_height() - img.get_height()) // 2
        pos = (x, y)
        area.blit(img, pos)

    @classmethod
    def check_sectors_response(cls, sectors, area_position):
        for sector in sectors:
            x = area_position[0] + sector.position[0]
            y = area_position[1] + sector.position[1]
            if AdditionalMethods.is_mouse_pos_in_area(sector.area, (x, y)):
                if sector.condition == 'sleep' and sector.obj is not None:
                    SectorsSounds.select.play()
                sector.condition = 'response'
            else:
                sector.condition = 'sleep'

    @classmethod
    def get_chose_object_index(cls, sectors, area_position):
        i = 0
        for sector in sectors:
            x = area_position[0] + sector.position[0]
            y = area_position[1] + sector.position[1]
            if AdditionalMethods.is_mouse_pos_in_area(sector.area, (x, y)):
                return i
            i += 1

    @classmethod
    def invisible_area(cls, area):
        area.set_alpha(0)

    @classmethod
    def visible_area(cls, area):
        area.set_alpha(200)

    @classmethod
    def put_on_area(cls, area, *to_put):
        for put in to_put:
            area.blit(put, (0, 0))

    @classmethod
    def clear_area(cls, area):
        area.fill(Colors.snow)

    @classmethod
    def is_in_response_range(cls, player, responser):
        if responser.x - Values.response_range <= player.x + player.bitmap.get_width()//2 \
                <= responser.x + responser.bitmap.get_width() + Values.response_range:
            return True
        else:
            return False


class MainMethods:
    @classmethod
    def render_pets(cls, screen, pets):
        for pet in pets.units:
            pet.make_a_random_step(screen)

    # Objects responses
    @classmethod
    def check_objects_responses(cls, player, *objects):
        for obj in objects:
            if type(obj) == list:
                for sobj in obj:
                    check_object = sobj
                    cls.check_objects_responses(player, check_object)
            else:
                check_object = obj
                cls.check_object_response(player, check_object)

    @classmethod
    def check_object_response(cls, player, obj):
        if AdditionalMethods.is_in_response_range(player, obj):
            # print('it responses')
            obj.response()
        else:
            obj.sleep()

    # Objects render
    '''''
    @classmethod
    def render_objects(cls, screen, *objects):
        for obj in objects:
            if type(obj) == list:
                for sobj in obj:
                    sobj.render(screen)

            else:
                obj.render(screen)
    '''

    @classmethod
    def render_objects(cls, screen, *objects):
        for obj in objects:
            if type(obj) == list:
                array = obj
                for ob in array:
                    cls.render_objects(screen, ob)
            else:
                obj.render(screen)

    @classmethod
    def check_own_pets_responses(cls, owner):
        for pet in owner.pets:
            if AdditionalMethods.is_in_response_range(pet, owner) and pet.hp < pet.max_hp * 0.8 \
                    and not owner.is_hands_empty():
                pet.response()
            else:
                pet.sleep()

    @classmethod
    def check_pets_responses(cls, player, pets):
        for pet in pets:
            if AdditionalMethods.is_in_response_range(player, pet):
                pet.response()
            else:
                pet.sleep()

    @classmethod
    def need_to_get_out(cls, player, room):
        if AdditionalMethods.is_in_response_range(player, room.door):
            if AdditionalMethods.is_mouse_pos_in_area(room.door.top_panel.area,
                                                      room.door.top_panel.position):
                room.door.talk(room.door.sounds.open)
                return True

