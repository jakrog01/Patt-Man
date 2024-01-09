from Sprite.GhostMakers.AbstractGhostMaker import AbstractGhostMaker
from Sprite.Ignoramus import Ignoramus
import pygame

class IgnoramusMaker(AbstractGhostMaker):
    def __init__(self):
        self.__picture = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Ignoramus.png"), (32,32))

    def make(self, args: list):
        return Ignoramus(args[0],args[1], args[2],args[3], args[4], self.__picture)