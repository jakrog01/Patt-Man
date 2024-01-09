from Sprite.GhostMakers.AbstractGhostMaker import AbstractGhostMaker
from Sprite.Traper import Traper
import pygame

class TraperMaker(AbstractGhostMaker):
    def __init__(self):
        self.__picture = pygame.transform.scale(pygame.image.load(f"Sprite\\Graphics\\Traper.png"), (32,32))

    def make(self, args: list):
        return Traper(args[0],args[1], args[2],args[3], args[4], self.__picture)