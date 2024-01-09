import pygame

class Pacman():
    def __init__(self, x, y, tile_size):
        self.__x = x
        self.__y = y
        self.__direction = "Right"
        self.__next_direction = "Right"
        self.__score = 0
        self.__tile_size = tile_size
        self.__lives = 2

        self.__state = "Prey"
        self.__counter = 0
        self.__kill_streak = 0

        self.__stepper = 0

    def enter_predator_mode(self):
        self.__state = "Predator"
        self.__kill_streak = 0

    def enter_prey_mode(self):
        self.__counter = 0
        self.__state = "Prey"

    def draw(self, win):
        graphic = int(self.__stepper // 10)
        rot = self.__rotation[self.direction]

        rotated_image = pygame.transform.rotate(self.__pictures[graphic], rot)
        rotated_rect = rotated_image.get_rect(center=(self.__x, self.__y))
        win.blit(rotated_image, rotated_rect.topleft)

        self.__stepper += 1
        if self.__stepper > 39:
            self.__stepper = 0


    def load_graphics(self, one, two, three, four):
        self.__pictures = {0: one, 1: two, 2: three, 3: four}
        self.__rotation = {"Right": 0, "Up": 90, "Left": 180, "Down": 270}

    def display_score(self, screen):
        score_text =pygame.font.Font('Sprite/Graphics/Grand9K Pixel.ttf', 15)
        score_box = score_text.render(f'SCORE: {self.__score}', True, (255,255,255))
        screen.blit(score_box, (20, self.__tile_size * 30 + 5))
    
    def display_lives(self, screen):
        lives_text = pygame.font.Font('Sprite/Graphics/Grand9K Pixel.ttf', 15)
        lives_box = lives_text.render(f'LIVES: {self.__lives}', True, (255,255,255))
        screen.blit(lives_box, (550, self.__tile_size * 30 + 5))

    def accept_director_changer_visitor(self, visitor):
        visitor.visitPacman(self)

    def accept_movement_visitor(self, visitor):
        visitor.visitPacman(self)

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, new_state):
        self.__state = new_state

    @property
    def kill_streak(self):
        return self.__kill_streak
    
    @kill_streak.setter
    def kill_streak(self, new_kill_streak):
        self.__kill_streak = new_kill_streak

    @property
    def counter(self):
        return self.__counter     
    
    @counter.setter
    def counter(self, new_counter):
        self.__counter = new_counter     

    @property
    def next_direction(self):
        return self.__next_direction
    
    @next_direction.setter
    def next_direction(self, newdirection):
        self.__next_direction = newdirection
    
    @property
    def lives(self):
        return self.__lives
    
    @lives.setter
    def lives(self, value):
        self.__lives = value
    
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