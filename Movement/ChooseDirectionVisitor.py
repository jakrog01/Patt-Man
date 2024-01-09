from Movement.AbstractMovementVisitor import AbstractMovementVisitor
from Sprite.Pacman import Pacman
from Sprite.Hunter import Hunter
from Sprite.Traper import Traper
from Sprite.Ignoramus import Ignoramus

from Sprite.Clairvoyant import Clairvoyant
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
    
    def visit_hunter(self, hunter: Hunter):
        if (hunter.x-11) % self.__title_size == 0 and (hunter.y-11) % self.__title_size == 0:
            hunter.strategy.choose_direction(hunter, self.__pacman, self.__title_size, self.__map, -1, -1)

    def visit_clairvoyant(self, clairvoyant: Clairvoyant):
        if (clairvoyant.x-11) % self.__title_size == 0 and (clairvoyant.y-11) % self.__title_size == 0:
            clairvoyant.strategy.choose_direction(clairvoyant, self.__pacman, self.__title_size, self.__map, len(self.__map[0]),-1)

    def visit_traper(self, traper: Traper):
        if (traper.x-11) % self.__title_size == 0 and (traper.y-11) % self.__title_size == 0:
            traper.strategy.choose_direction(traper, self.__pacman, self.__title_size, self.__map, -1, len(self.__map))

    def visit_ignoramus(self, ignoramus: Ignoramus):
        if (ignoramus.x-11) % self.__title_size == 0 and (ignoramus.y-11) % self.__title_size == 0:
            ignoramus.strategy.choose_direction(ignoramus, self.__pacman, self.__title_size, self.__map, len(self.__map[0]), len(self.__map))