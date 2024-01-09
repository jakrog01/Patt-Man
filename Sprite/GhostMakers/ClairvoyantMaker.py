from Sprite.GhostMakers.AbstractGhostMaker import AbstractGhostMaker
from Sprite.Clairvoyant import Clairvoyant
import pygame

class ClairvoyantMaker(AbstractGhostMaker):
    def __init__(self):
        self.__picture = pygame.transform.scale(pygame.image.load(f"Sprite\Graphics\Clairvoyant.png"), (32,32))

    def make(self, args: list):
        return Clairvoyant(args[0],args[1], args[2],args[3], args[4], self.__picture)