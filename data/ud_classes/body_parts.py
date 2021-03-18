import pygame
from .objects import UnitStorage
from .methods import AdditionalMethods
from .rgb import Colors
from .values import Values


class Hand(UnitStorage):
    def __init__(self, name, capacity, units):
        super().__init__(name, capacity, units)
        self.area = AdditionalMethods.create_panel_area(Values.hand_panel_size)

    def render(self, screen, owner_position, position):
        self.area.fill(Colors.snow)
        self.area.set_alpha(200)
        try:
            AdditionalMethods.draw_image_on_area_centre(self.area, self.units[0].bitmap)
            AdditionalMethods.draw_surface_box(self.area, Colors.black)
        except:
            self.area.set_alpha(0)
        screen.blit(self.area, (owner_position[0] + position[0], owner_position[1] + position[1] + 5))


class Face:
    def __init__(self):
        self.area = AdditionalMethods.create_panel_area((1, 1))
        self.x = 0
        self.y = 0
        self.width = 1
        self.height = 1
        self.eye_width = 1
        self.eye_height = 1
        self.mouth_width = 1

    def adapt(self, unit_bitmap):
        self.width = unit_bitmap.get_width() // 5
        self.height = unit_bitmap.get_height() // 10
        self.x = (unit_bitmap.get_width() - self.width) // 2 + 4
        self.y = 10
        self.area = AdditionalMethods.create_panel_area((self.width, self.height))
        self.eye_width = self.width // 5
        self.eye_height = self.eye_width
        self.mouth_width = int(0.6 * self.width)

    def draw_eyes(self, color):
        pygame.draw.rect(self.area, color, (4, 4, self.eye_width, self.eye_height))
        pygame.draw.rect(self.area, color, (self.width - self.eye_width - 4, 4, self.eye_width, self.eye_height))

    def draw_mouth(self, color, mood):
        pi = 3.1415926
        if mood > 80:
            pygame.draw.arc(self.area, color, (3, 5, 23, 15), pi, 2 * pi, 1)
        elif 30 <= mood <= 80:
            pygame.draw.aaline(self.area, color, [0, 12], [self.width, 12])
        else:
            pygame.draw.arc(self.area, color, (3, 15, 23, 20), 0, pi)

    def draw_me(self, unit_bitmap, color, mood):
        self.area.fill(Colors.black)
        self.draw_eyes(color)
        self.draw_mouth(color, mood)
        unit_bitmap.blit(self.area, (self.x, self.y))


class Body:
    def __init__(self):
        self.area = AdditionalMethods.create_panel_area((1, 1))
        self.x = 0
        self.y = 0
        self.width = 1
        self.height = 1

    def adapt(self, unit):
        self.width = unit.bitmap.get_width()
        self.height = unit.bitmap.get_height() - unit.face.area.get_height()
        self.x = 0
        self.y = unit.face.area.get_height()
        self.area = AdditionalMethods.create_panel_area((self.width, self.height))