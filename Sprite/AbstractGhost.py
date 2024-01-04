from abc import ABC, abstractmethod

class AbstractGhost(ABC):

    def __init__(self, x ,y):
        self.__x = x
        self.__y = y