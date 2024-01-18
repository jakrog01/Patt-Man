from Sprite.GhostMakers.AbstractGhostMaker import AbstractGhostMaker
from Sprite.Hunter import Hunter
import pygame
import os

class HunterMaker(AbstractGhostMaker):
    def __init__(self):
        self.__picture = pygame.transform.scale(pygame.image.load( os.path.join("Sprite", "Graphics", "Hunter.png")), (32,32))

    def make(self, args: list) -> Hunter:
        return Hunter(args[0],args[1], args[2],args[3], args[4], self.__picture)