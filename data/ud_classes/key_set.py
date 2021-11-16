import pygame

class Actions:
    right = False
    left = False
    down = False
    up = False

    def __init__(self, keys):
        self.right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        self.left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        self.down = keys[pygame.K_UP] or keys[pygame.K_w]
        self.up = keys[pygame.K_DOWN] or keys[pygame.K_s]
        