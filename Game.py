import pygame
from Board.Board import Board
from Board.Maps.FUWMap import FUWMap, start_points
from Sprite.Pacman import Pacman
from Sprite.Hunter import Hunter
from Sprite.Traper import Traper

from Movement.ChooseDirectionVisitor import ChooseDirectionVisitor
from Movement.MovementVisitor import MovementVisitor
from Movement.PacmanMovementDirectionSetter.PacmanMovementSetter import PacmanMovementDirectionSetter

pygame.init()
WIDTH = 630
HEIGHT = 670
TILE_SIZE= WIDTH / len(FUWMap) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

map = Board(FUWMap, TILE_SIZE)
player = Pacman(0, 0, TILE_SIZE)
ghosts = [Hunter(0,0, TILE_SIZE, FUWMap), Traper(0,0, TILE_SIZE, FUWMap)]

Board.place_in_starting_positions(player, ghosts, TILE_SIZE, start_points)

movement_visitor = MovementVisitor(FUWMap, TILE_SIZE)
choose_direction_visitor = ChooseDirectionVisitor(FUWMap, TILE_SIZE, player)
direction_setter = PacmanMovementDirectionSetter(player)

run = True

change_strategy_time = 2000
last_strategy_change_time = pygame.time.get_ticks()

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

    player.accept_director_changer_visitor(choose_direction_visitor)
    player.accept_movement_visitor(movement_visitor)

    map.draw_map(screen)
    player.display_score(screen)
    player.display_lives(screen)

    for ghost in ghosts:
        ghost.accept_director_changer_visitor(choose_direction_visitor)
        ghost.accept_movement_visitor(movement_visitor)
        ghost.draw(screen)

    player.draw(screen)
    
    pygame.display.update()
    dt = clock.tick(90)

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - last_strategy_change_time
    if elapsed_time >= change_strategy_time:
        for ghost in ghosts:
            ghost.change_strategy()

        last_strategy_change_time = current_time
        if change_strategy_time == 2000 or change_strategy_time == 5000:
            change_strategy_time = 25000
        else:
            change_strategy_time = 5000

    if Board.check_collisions(player, ghosts, TILE_SIZE):
        player.lives = player.lives-1
        if player.lives == 0:
            run = False
        else:
            Board.place_in_starting_positions(player, ghosts, TILE_SIZE, start_points)
            start_freeze = pygame.time.get_ticks()
            freeze = True
            while freeze:
                time = pygame.time.get_ticks()
                if time - start_freeze > 2000:
                    freeze = False
    
    condition = False
    for line in FUWMap:
        if 9 in line:
            condition = True
    run = condition

pygame.quit()