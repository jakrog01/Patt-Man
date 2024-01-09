from Sprite.GhostMakers.AbstractGhostMaker import AbstractGhostMaker
from Sprite.AbstractGhost import AbstractGhost

class GhostFactory():
    def __init__(self):
        self.__dict = {}

    def add(self, key: str, Function: AbstractGhostMaker):
        self.__dict[key] = Function
    
    def remove(self,key:str):
        if key in self.__dict:
            self.__dict.pop(key)
        else:
            raise ValueError

    def produce(self, key:str, list: list) -> AbstractGhost:
        try:
            return self.__dict[key].make(list)
        except:
            raise ValueError