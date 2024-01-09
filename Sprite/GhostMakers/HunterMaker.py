from Sprite.GhostMakers.AbstractGhostMaker import AbstractGhostMaker
from Sprite.Hunter import Hunter
import pygame

class HunterMaker(AbstractGhostMaker):
    def __init__(self):
        self.__picture = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Hunter.png"), (32,32))

    def make(self, args: list):
        return Hunter(args[0],args[1], args[2],args[3], args[4], self.__picture)