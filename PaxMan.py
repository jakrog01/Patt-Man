import pygame
import random
from Board.Board import Board
from Board.Maps.FUWMap import FUWMap, start_points, ghost_respawn_point
from Sprite.Player import Player
from Sprite.Traper import Traper

from Sprite.GhostFactory import GhostFactory
from Sprite.GhostMakers.HunterMaker import HunterMaker
from Sprite.GhostMakers.IgnoramusMaker import IgnoramusMaker
from Sprite.GhostMakers.ClairvoyantMaker import ClairvoyantMaker
from Sprite.GhostMakers.TraperMaker import TraperMaker
from Sprite.Graphics.SpecialGraphicsLoaderVisitor import SpecialGraphicLoaderVisitor

from Movement.GhostsStrategies.GhostHouseStrategy import GhostHouseStrategy
from Movement.GhostsStrategies.GhostDispersionStrategy import GhostDispersionStrategy
from Movement.GhostsStrategies.GhostLeaveHouseStrategy import GhostLeaveHouseStrategy
from Movement.ChooseDirectionVisitor import ChooseDirectionVisitor
from Movement.MovementVisitor import MovementVisitor
from Movement.PlayerMovementDirectionSetter.PlayerMovementSetter import PlayerMovementDirectionSetter


pygame.init()

pygame.display.set_caption('PaxMan')
Icon = pygame.image.load(f'Sprite\\Graphics\\Player\\2.png')
pygame.display.set_icon(Icon)

used_map = FUWMap
WIDTH = 630
HEIGHT = 670
TILE_SIZE= WIDTH / len(used_map) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

map = Board(used_map, TILE_SIZE)
player = Player(0, 0, TILE_SIZE)
graphic_loader = SpecialGraphicLoaderVisitor()

ghost_factory = GhostFactory()
ghost_factory.add("HUNTER", HunterMaker())
ghost_factory.add("CLAIRVOYANT", ClairvoyantMaker())
ghost_factory.add("TRAPER", TraperMaker())
ghost_factory.add("IGNORAMUS", IgnoramusMaker())
ghosts_to_make = ["HUNTER", "CLAIRVOYANT", "TRAPER", "IGNORAMUS"]
ghosts = []

for index, key in enumerate(ghosts_to_make):
    ghosts.append(ghost_factory.produce(key, [start_points[index+1][0], start_points[index+1][1], ghost_respawn_point, TILE_SIZE, used_map]))
for ghost in ghosts:
    if isinstance(ghost, Traper):
        ghost.set_hunter(ghosts[0])    
    ghost.accept_graphic_loader_visitor(graphic_loader)
player.accept_graphic_loader_visitor(graphic_loader)

Board.place_in_starting_positions(player, ghosts, TILE_SIZE, start_points)

movement_visitor = MovementVisitor(used_map, TILE_SIZE, ghosts)
choose_direction_visitor = ChooseDirectionVisitor(used_map, TILE_SIZE, player)
direction_setter = PlayerMovementDirectionSetter(player)

run = True
dead = False
exit = True
change_strategy_time = 2000
cherry_spawned = False
last_strategy_change_time = pygame.time.get_ticks()

cherry_time = random.randint(30000,40000)
cherry_duration_time = random.randint(15000,25000)

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            exit = False

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
        ghosts[1].enter_predator_mode()
        ghosts[1].strategy = GhostLeaveHouseStrategy()
        ghosts[1].state = "Escape"

    elif player.score > 750 and isinstance(ghosts[2].strategy, GhostHouseStrategy):
        ghosts[2].enter_predator_mode()
        ghosts[2].strategy = GhostLeaveHouseStrategy()
        ghosts[2].state = "Escape"
    
    elif player.score > 1500 and isinstance(ghosts[3].strategy, GhostHouseStrategy):
        ghosts[3].enter_predator_mode()
        ghosts[3].strategy = GhostLeaveHouseStrategy()
        ghosts[3].state = "Escape"

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
                    ghost.enter_predator_mode()
            change_strategy_time = 25000

        else:
            for ghost in ghosts:
                if ghost.state == "Predator":
                    ghost.strategy = GhostDispersionStrategy()
            change_strategy_time = 5000
    
    if current_time >= cherry_time and not cherry_spawned:
        used_map[start_points[0][0] - 1][start_points[0][1] - 1] = 10
        start_cherry = pygame.time.get_ticks()
        cherry_spawned = True
    
    elif current_time - cherry_time > cherry_duration_time:
        used_map[start_points[0][0]-1][start_points[0][1]-1] = 0

    if player.state == "Predator" and player.counter == 0:
        start_predator_time = pygame.time.get_ticks()

    if player.counter > 0:
        current_time = pygame.time.get_ticks()
        elapsed_predator_time = current_time - start_predator_time

        if elapsed_predator_time >= 8000:
            player.enter_prey_mode()
            for ghost in ghosts:
                    if ghost.state == "Prey":
                        ghost.enter_predator_mode()
    
    if Board.check_collisions(player, ghosts, TILE_SIZE):
        player.lives = player.lives-1
        dead = True
        used_map[start_points[0][0]-1][start_points[0][1]-1] = 0
        
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
    
    if run != False:
        condition = False

        for line in used_map:
            if 9 in line:
                condition = True
        run = condition

if exit:
    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        
        screen.fill(pygame.Color("black"))

        if dead:
            text = "LOST"
        else:
            text = "WON"
        
        end_text = pygame.font.Font('Sprite/Graphics/Grand9K Pixel.ttf', 80)
        end_box = end_text.render(f'YOU {text}', True, (255, 0, 0))
        end_text_rect = end_box.get_rect()
        end_text_rect.center = (WIDTH // 2, HEIGHT // 2 - 55)
        screen.blit(end_box, end_text_rect.topleft)

        score_text = pygame.font.Font('Sprite/Graphics/Grand9K Pixel.ttf', 85)
        score_box = score_text.render(f'SCORE: {player.score + player.lives * 400}', True, (255, 255, 0))
        score_text_rect = score_box.get_rect()
        score_text_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)
        screen.blit(score_box, score_text_rect.topleft)

        pygame.display.update()
        dt = clock.tick(90)


pygame.quit()