class OldShopWindow(UnitStorage, Talker):
    def __init__(self, name, capacity, units, position, sounds):
        UnitStorage.__init__(self, name, capacity, units)
        Talker.__init__(self, sounds)
        self.area = AdditionalMethods.create_panel_area((150, 140))
        self.name = name
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.sectors = AdditionalMethods.create_sectors_for_area(self.area, self.capacity, 3)
        AdditionalMethods.compare_sectors_with_objects(self.sectors, self.units)

    def render(self, screen):
        AdditionalMethods.clear_area(self.area)
        AdditionalMethods.draw_sectors(self.area, self.sectors)
        AdditionalMethods.draw_surface_box(self.area, Colors.black)
        screen.blit(self.area, self.position)

    def response(self):
        AdditionalMethods.check_sectors_response(self.sectors, self.position)

    def sleep(self):
        AdditionalMethods.check_sectors_response(self.sectors, self.position)

    def get_stuff(self):
        index = AdditionalMethods.get_chose_object_index(self.sectors, self.position)
        stuff = self.units[index]
        self.talk(self.sounds.pik)
        return stuff
