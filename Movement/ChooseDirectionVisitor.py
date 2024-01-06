from Movement.AbstractMovementVisitor import AbstractMovementVisitor
from Sprite.Pacman import Pacman
from Sprite.Hunter import Hunter
from Movement.ChagneDirectionVisitor.CheckOpposite import check_oposite
from Movement.ChagneDirectionVisitor.DirectionChangePossibility import check_direction_change_possibility
 
class ChooseDirectionVisitor(AbstractMovementVisitor):
    def __init__(self, map, title_size, pacman):
        self.__map = map
        self.__title_size = title_size
        self.__pacman = pacman
    
    def visitPacman(self, pacman: Pacman):

        if check_oposite(pacman.direction, pacman.next_direction):
            pacman.direction = pacman.next_direction
            pacman.next_direction = "None"

        elif check_direction_change_possibility(pacman, self.__map, self.__title_size):
            pacman.direction = pacman.next_direction
            pacman.next_direction = "None"
    
    def visitHunter(self, hunter: Hunter):
        if (hunter.x-11) % self.__title_size == 0 and (hunter.y-11) % self.__title_size == 0:
            hunter.strategy.choose_direction(hunter, self.__pacman, self.__title_size, self.__map)