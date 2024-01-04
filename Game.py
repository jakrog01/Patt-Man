import pygame
from Board.Board import Board
from Board.Maps.FUWMap import FUWMap
from Sprite.Pacman import Pacman
from Movement.ChooseDirectionVisitor import ChooseDirectionVisitor
from Movement.MovementVisitor import MovementVisitor
from Movement.PacmanMovementSetter.PacmanMovementSetter import PacmanMovementDirectionSetter

pygame.init()

WIDTH = 630
HEIGHT = 670
TILE_SIZE= WIDTH / len(FUWMap) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

map = Board(FUWMap, TILE_SIZE)
player = Pacman(32, 116, TILE_SIZE)
run = True

movement_visitor = MovementVisitor(FUWMap, TILE_SIZE)
choose_direction_visitor = ChooseDirectionVisitor(FUWMap, TILE_SIZE)
direction_setter = PacmanMovementDirectionSetter(player)

while run:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                direction_setter.set_direction("w")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                direction_setter.set_direction("s")
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                direction_setter.set_direction("a")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                direction_setter.set_direction("d")
    
    screen.fill(pygame.Color("black"))

    map.draw_map(screen)
    player.display_score(screen)

    player.draw(screen)

    movement_visitor.visitPacman(player)
    pygame.display.update()
    dt = clock.tick(42)

pygame.quit()