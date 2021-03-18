import pygame


class HumanSprites:
    # Player
    bitmap = pygame.image.load("images/human/bitmap.png")
    head = pygame.image.load("images/human/head.png")
    body = pygame.image.load("images/human/body.png")
    top = pygame.image.load("images/human/top.png")
    legs = pygame.image.load("images/human/legs.png")
    left_leg_up = pygame.image.load("images/human/l_leg_up.png")
    right_leg_up = pygame.image.load("images/human/r_leg_up.png")
    walk_legs = [left_leg_up, right_leg_up, left_leg_up, right_leg_up, left_leg_up, right_leg_up]


class WomanSprites:
    bitmap = pygame.image.load("images/human/woman.png")


class CashierSprites:
    bitmap = pygame.image.load("images/human/cashier.png")


class CatSprites:
    bitmap = pygame.image.load("images/cat/bitmap.png")


class DogSprites:
    bitmap = pygame.image.load("images/dog/bitmap.png")


class RipSprite:
    bitmap = pygame.image.load("images/rip.png")


