import pygame
from Board.Board import Board
from Board.Maps.FUWMap import FUWMap, start_points, ghost_respawn_point
from Sprite.Pacman import Pacman
from Sprite.Traper import Traper
from Sprite.GhostFactory import GhostFactory
from Sprite.GhostMakers.HunterMaker import HunterMaker
from Sprite.GhostMakers.ClairvoyantMaker import ClairvoyantMaker
from Sprite.GhostMakers.TraperMaker import TraperMaker
from Movement.GhostsStrategies.GhostHouseStrategy import GhostHouseStrategy
from Movement.GhostsStrategies.GhostDispersionStrategy import GhostDispersionStrategy
from Movement.ChooseDirectionVisitor import ChooseDirectionVisitor
from Movement.MovementVisitor import MovementVisitor
from Sprite.GhostMakers.SpecialGraphicsLoaderVisitor import SpecialGraphicLoaderVisitor
from Movement.PacmanMovementDirectionSetter.PacmanMovementSetter import PacmanMovementDirectionSetter

pygame.init()
WIDTH = 630
HEIGHT = 670
TILE_SIZE= WIDTH / len(FUWMap) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

map = Board(FUWMap, TILE_SIZE)
player = Pacman(0, 0, TILE_SIZE)

graphic_loader = SpecialGraphicLoaderVisitor()

ghost_factory = GhostFactory()
ghost_factory.add("HUNTER", HunterMaker())
ghost_factory.add("CLAIRVOYANT", ClairvoyantMaker())
ghost_factory.add("TRAPER", TraperMaker())
ghosts_to_make = ["HUNTER", "CLAIRVOYANT", "TRAPER"]

ghosts = []
for index, key in enumerate(ghosts_to_make):
    ghosts.append(ghost_factory.produce(key, [start_points[index+1][0], start_points[index+1][1], ghost_respawn_point, TILE_SIZE, FUWMap]))

for ghost in ghosts:
    if isinstance(ghost, Traper):
        ghost.set_hunter(ghosts[0])    
    ghost.accept_graphic_loader_visitor(graphic_loader)

Board.place_in_starting_positions(player, ghosts, TILE_SIZE, start_points)

movement_visitor = MovementVisitor(FUWMap, TILE_SIZE, ghosts)
choose_direction_visitor = ChooseDirectionVisitor(FUWMap, TILE_SIZE, player)
direction_setter = PacmanMovementDirectionSetter(player)

run = True
dead = False

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

    if player.score > 150 and isinstance(ghosts[1].strategy, GhostHouseStrategy):
        ghosts[1].state = "Predator"
        ghosts[1].strategy = GhostDispersionStrategy()

    elif player.score > 650 and isinstance(ghosts[2].strategy, GhostHouseStrategy):
        ghosts[2].state = "Predator"
        ghosts[2].strategy = GhostDispersionStrategy()

    for ghost in ghosts:
        ghost.accept_director_changer_visitor(choose_direction_visitor)
        ghost.accept_movement_visitor(movement_visitor)
        ghost.draw(screen)

    player.draw(screen)
    
    pygame.display.update()
    dt = clock.tick(90)

    if dead == True:
        start_freeze = pygame.time.get_ticks()
        freeze = True
        while freeze:
            time = pygame.time.get_ticks()
            if time - start_freeze > 2000:
                freeze = False
                dead = False


    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - last_strategy_change_time

    if elapsed_time >= change_strategy_time:
        last_strategy_change_time = current_time

        if change_strategy_time == 2000 or change_strategy_time == 5000:
            for ghost in ghosts:
                if ghost.state == "Predator":
                    ghost.set_normal_strategy()
            change_strategy_time = 25000

        else:
            for ghost in ghosts:
                if ghost.state == "Predator":
                    ghost.strategy = GhostDispersionStrategy()

            change_strategy_time = 5000


    if player.state == "Predator" and player.counter == 0:
        start_predator_time = pygame.time.get_ticks()

    if player.counter > 0:
        current_time = pygame.time.get_ticks()
        elapsed_predator_time = current_time - start_predator_time
        
        if elapsed_predator_time >= 8000:
            player.enter_prey_mode()
            for ghost in ghosts:
                    if ghost.state != "Home" and ghost.state != "Dead":
                        ghost.enter_predator_mode()
    

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
                if time - start_freeze > 500:
                    freeze = False
                    dead = True
    
    if run != False:
        condition = False

        for line in FUWMap:
            if 9 in line:
                condition = True
        run = condition

pygame.quit()