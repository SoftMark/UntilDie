'''
class Cementary:
    def print_pets_menu(self):
        print('\nChoose pet:')
        i = 0
        for pet_kind in NamesStorage.pet_kinds:
            print('\n\n' + TColors.blue + pet_kind + 's' + TColors.end + ':')
            for pet in self.pets[pet_kind + 's'].units:
                print('(' + str(i + 1) + ')' + TColors.blue + pet.name + TColors.end + '(' + TColors.pink +
                      str(pet.breed) + TColors.end + ').   ', end='')
                i += 1
        print('\n\n(0)' + TColors.red + 'Exit\n' + TColors.end)


class JointStorage(UnitStorage):
    storages = []

    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.defolt_storage = defolt_storage
        if type(defolt_storage) is SeparateStorage:
            self.storages.append(defolt_storage)

'''