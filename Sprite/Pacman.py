import pygame

class Pacman():
    def __init__(self, x, y, tile_size):
        self.__x = x
        self.__y = y
        self.__direction = "Up"
        self.__next_direction = "Up"
        self.__score = 0
        self.__tile_size = tile_size

    def draw(self, win):
        pygame.draw.circle(win, "yellow", (self.__x, self.__y), int(self.__tile_size//2) + 3)
    
    def display_score(self, screen):
        score_text = pygame.font.SysFont('didot.ttc', 20)
        score_box = score_text.render(f'SCORE: {self.__score}', True, (255,255,255))
        screen.blit(score_box, (20, self.__tile_size * 30 + 5))

    def accept_director_changer_visitor(self, visitor):
        visitor.visitPacman(self)

    def accept_movement_visitor(self, visitor):
        visitor.visitPacman(self)
    
    @property
    def next_direction(self):
        return self.__next_direction
    
    @next_direction.setter
    def next_direction(self, newdirection):
        self.__next_direction = newdirection

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, newdirection):
        self.__direction = newdirection

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, newscore):
        self.__score = newscore