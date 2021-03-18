import pygame
pygame.init()


class SoundLoader:
    way = 'sounds/'
    sound_format = '.wav'

    @classmethod
    def get_sound(cls, name):
        return pygame.mixer.Sound(cls.way + name + cls.sound_format)


class MainSounds:
    nuh = pygame.mixer.Sound('sounds/nuh.wav')
    rip_bell = SoundLoader.get_sound("rip_bell")


class AnimalSound:
    chewing = SoundLoader.get_sound('chewing')
    drink = SoundLoader.get_sound('drink')


class CatSounds:
    chewing = pygame.mixer.Sound('sounds/purr.wav')
    scream = None


class DogSounds:
    chewing = pygame.mixer.Sound('sounds/woof.wav')


class HumanSounds(AnimalSound):
    cha_ching = pygame.mixer.Sound('sounds/cha_ching.wav')
    nuh = pygame.mixer.Sound('sounds/nuh.wav')
    foot_step = pygame.mixer.Sound('sounds/footstep.wav')


class RefrigeratorSounds:
    open = pygame.mixer.Sound('sounds/refrigerator_open.wav')
    close = pygame.mixer.Sound('sounds/refrigerator_close.wav')


class DoorSounds:
    open = pygame.mixer.Sound('sounds/door_open.wav')


class AutomaticDoorSounds:
    open = pygame.mixer.Sound('sounds/automatic_door_open.wav')


class ShopSounds:
    pik = pygame.mixer.Sound('sounds/cashbox.wav')


class SectorsSounds:
    choose = pygame.mixer.Sound('sounds/toc_click.wav')
    select = pygame.mixer.Sound('sounds/selection_click.wav')


class PetSounds(AnimalSound):
    def __init__(self, chewing, scream, play):
        self.chewing = SoundLoader.get_sound(chewing)
        self.scream = SoundLoader.get_sound(scream)
        self.play = SoundLoader.get_sound(play)


class MoneySounds:
    dropping = SoundLoader.get_sound("money")


class SoundExemplars:
    dog_sounds = PetSounds('chewing', 'scream_dog', 'woof')
    cat_sounds = PetSounds('chewing', 'scream_cat', 'purr')


class CoffeeMachineSounds:
    get_coffee = SoundLoader.get_sound('get_coffee')


class TableFootballSounds:
    play_table_football = SoundLoader.get_sound('play_table_football')


class BitchSounds(AnimalSound):
    pleasure = SoundLoader.get_sound('woman_pleasure')