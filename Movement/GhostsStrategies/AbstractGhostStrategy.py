from abc import ABC, abstractmethod

class AbstractGhostStrategy():
    @abstractmethod
    def choose_direction():
        pass