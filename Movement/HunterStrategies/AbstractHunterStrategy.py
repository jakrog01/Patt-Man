from abc import ABC, abstractmethod

class AbstractHunterStrategy():
    @abstractmethod
    def choose_direction():
        pass