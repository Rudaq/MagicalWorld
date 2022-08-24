from game.game_support import create_npc, import_csv_layout, import_folder

import sys
import os
from datetime import datetime
from pygame.locals import *
from NLP.dialog_generation.ButtonClass import ButtonClass
from NLP.dialog_generation.NpcDialogThread import NpcDialogThread
from game.Button import Button
from game.dialog_support import hero_in_dialog, update_positions_and_transparency, move_dialog_up, move_dialog_down
from game.game_support import hero_in_dialog_or_talk, hero_only_in_fight
from game.fight_support import set_fight_parameters
from game.game_support import create_npc
from game.hud_component import update_hud
from game.quest.Quest import Quest
from game.quest_support import show_quest_to_hero
from settings import *
import pygame
from settings import GUI_IMAGES, MAP_IMAGES
from _csv import reader
import os
from pathlib import Path

'''
Main game loop
'''

TILESIZE = 32

current = os.path.dirname(os.path.realpath(__file__))
print("Current Directory", current)
path = Path(__file__).resolve().parent.parent
print(path)


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, inflation, surface=pygame.Surface((32, 32))):
        super(Tile, self).__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.inflation = inflation
        # inflate - take the rect and change the size
        self.groups = groups
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(inflation[0], inflation[1])


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super(CameraGroup, self).__init__()
        self.display_surf = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surf.get_size()[0] // 2
        self.half_h = self.display_surf.get_size()[1] // 2

        # ground
        self.ground_surf = pygame.image.load(os.path.join(path, 'resources/graphics/tilemap/floor.png')).convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, hero):
        if hero.rect.centerx <= 750:
            self.offset.x = 0
        else:
            self.offset.x = hero.rect.centerx - self.half_w
        if hero.rect.centery <= 400:
            self.offset.y = 0
        else:
            self.offset.y = hero.rect.centery - self.half_h

        # ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surf.blit(self.ground_surf, ground_offset)

        # active elements
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surf.blit(sprite.image, offset_position)


def create_map(all_sprites_group, collision_sprites):
    layouts = {
        'boundary_hero': import_csv_layout('resources/map/tilesets/v3_constraints.csv'),
        'object': import_csv_layout('resources/map/tilesets/v3_objects.csv'),
    }
    graphics = {
        'objects': import_folder('../resources/graphics/objects')
    }

    bound = pygame.image.load(os.path.join(path, 'resources/graphics/tilemap/player_blocker.png'))

    for style, layout in layouts.items():
        for row_index, row in enumerate(layout):
            for col_index, tile in enumerate(row):
                if tile != '-1':
                    x = col_index * 16
                    y = row_index * 16
                    if style == 'boundary_hero':
                        Tile((x, y), (all_sprites_group, collision_sprites), 'invisible', (-5, -4), bound)

                    if style == 'object':
                        surf = graphics['objects'][int(tile)]
                        Tile((x, y), (all_sprites_group, collision_sprites), 'object', (-10, -16), surf)


# Main game function
def game(hero):
    # pygame initialization
    pygame.init()
    pygame.display.set_caption("Battle of the Realm")
    screen = pygame.display.set_mode((WIDTH_GAME, HEIGHT_GAME))
    clock = pygame.time.Clock()

    npcs = []
    all_sprites_group = CameraGroup()
    # all_sprites_group = pygame.sprite.Group()
    collision_sprites = pygame.sprite.Group()

    # Test quest
    quest = Quest(
        "Go to the place where you found the stone, pour raven blood over it, burn the sage in the sacred fire, release mermaid’s voice and say the incantation to summon the god.",
        50, [], [])
    hero.active_quest = quest

    # Adding created characters to group with all sprites
    hero.collision_sprites = collision_sprites
    hero.groups = all_sprites_group
    all_sprites_group.add(hero)

    dx = 0
    dy = 0
    direct = "U"
    moving = False
    pressed = False
    prev = False
    npc_dialog_thread = None
    npc_dialog_thread = NpcDialogThread(hero, screen, npcs)
    npc_dialog_thread.start()
    show_quest = False
    restore_life = False
    restore_mana = False
    restore_life_time_passed = None
    restore_mana_time_passed = None
    option = 1
    npc_clicked = False
    chosen_npc = None
    counter = 0

    s = pygame.Surface((WIDTH_GAME, 150), pygame.SRCALPHA)
    arrow_up = ButtonClass(25, 25)
    arrow_down = ButtonClass(25, 25)
    scroll_button = ButtonClass(30, 40)
    fight_button = Button(100, 50, GUI_IMAGES['fight_button'], 0.8)
    talk_button = Button(100, 50, GUI_IMAGES['talk_button'], 0.8)

    # Creating npcs
    for npc_entity in NPCs:
        create_npc(npc_entity, [npcs], [all_sprites_group], collision_sprites)

    create_map(all_sprites_group, collision_sprites)

    # Main game loop
    while True:
        screen.fill(GREEN)

        # all_sprites_group.custom_draw(hero)
        # all_sprites_group.update()

        all_sprites_group.update()
        hero.update()
        all_sprites_group.draw(screen)

        # Getting the list of all pressed keys
        keys_pressed = pygame.key.get_pressed()

        # Event support - quiting, movement
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT \
                        or event.key == pygame.K_d or event.key == pygame.K_DOWN or event.key == pygame.K_s \
                        or event.key == pygame.K_UP or event.key == pygame.K_w:
                    moving = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    direct = "U"
                    dx = 0
                    dy = -5
                    moving = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direct = "D"
                    dx = 0
                    dy = 5
                    moving = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direct = "R"
                    dx = 5
                    dy = 0
                    moving = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direct = "L"
                    dx = -5
                    dy = 0
                    moving = True
                elif event.key == pygame.K_1 and hero.in_fight:
                    option = 1
                    set_fight_parameters(hero)
                elif event.key == pygame.K_2 and hero.in_fight:
                    option = 2
                    set_fight_parameters(hero)
                elif event.key == pygame.K_3 and hero.in_fight:
                    option = 3
                    set_fight_parameters(hero)

                # Event support for dialog
                if hero.in_dialog:
                    moving = False
                    # Checking if hero is now talking - possibility of keyboard interaction
                    # letters, digits, signs and space accepted (lists at the top)
                    if hero.hero_turn:
                        if pygame.key.name(event.key) in LETTERS:
                            if keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]:
                                hero.my_text += pygame.key.name(event.key).upper()
                            else:
                                hero.my_text += pygame.key.name(event.key)
                            hero.text_history[len(hero.text_history) - 1].text = hero.my_text

                        elif pygame.key.name(event.key) in DIGITS:
                            if pygame.key.name(event.key) == '1' and (keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]):
                                hero.my_text += '!'
                            else:
                                hero.my_text += pygame.key.name(event.key)
                            hero.text_history[len(hero.text_history) - 1].text = hero.my_text
                        elif pygame.key.name(event.key) == 'space':
                            hero.my_text += ' '
                            hero.text_history[len(hero.text_history) - 1].text = hero.my_text
                        elif pygame.key.name(event.key) in SIGNS:
                            if pygame.key.name(event.key) == '/' and (keys_pressed[K_LSHIFT] or keys_pressed[K_RSHIFT]):
                                hero.my_text += '?'
                            else:
                                hero.my_text += pygame.key.name(event.key)
                            hero.text_history[len(hero.text_history) - 1].text = hero.my_text
                        # Deleting the last written letter
                        elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            hero.my_text = hero.my_text[:-1]
                            hero.text_history[len(hero.text_history) - 1].text = hero.my_text
                        # Detecting enter, finishing the input, turn is changed to npc
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            hero.hero_turn = False
                            update_positions_and_transparency(hero.text_history)

        # Moving hero
        if moving:
            hero.move(direct, dx, dy)

        # Random movement of npcs if not in dialog
        for npc in npcs:
            if not npc.is_talking and not npc.is_fighting:
                npc.move()

        # Getting the state of mouse buttons - pressed or not
        left, middle, right = pygame.mouse.get_pressed()
        # Position of the mouse
        x, y = pygame.mouse.get_pos()
        mouse_point = (x, y)

        # Checking if the value of left in the last iteration was different
        # Ensuring that one click only performs the action once
        if left and prev != left:
            pressed = True
        else:
            pressed = False

        # Checking if mouse pressed
        if pressed:
            for npc in npcs:
                # Checking mouse point collision with npc
                if npc.rect.collidepoint(mouse_point):
                    counter += 1
                    if counter % 2 == 1:
                        chosen_npc = npc
                        npc_clicked = True
                        chosen_npc.add_npc_to_hud = True
                        update_hud(screen, hero, scroll_button, restore_life, restore_mana,
                                   restore_mana_time_passed,
                                   restore_life_time_passed, chosen_npc)
                        all_sprites_group.update()

                    else:
                        npc_clicked = False
                        chosen_npc.add_npc_to_hud = False
                        if chosen_npc.is_talking:
                            chosen_npc.is_talking = False
                            hero.in_dialog = False
                            hero.hero_turn = False
                            hero.my_text = ">> "
                            hero.text_history = []
                            chosen_npc.text_history = []
                            chosen_npc.text = ">> "
                            print("STOP TALKING!!")

                        if chosen_npc.is_fighting:
                            chosen_npc.is_fighting = False
                            hero.in_fight = False
                            print("STOP FIGHT")

                        update_hud(screen, hero, scroll_button, restore_life, restore_mana,
                                   restore_mana_time_passed,
                                   restore_life_time_passed, chosen_npc)
                        all_sprites_group.update()

            if arrow_up.rect.collidepoint(mouse_point):
                move_dialog_up(hero.text_history)
            elif arrow_down.rect.collidepoint(mouse_point):
                move_dialog_down(hero.text_history)
            elif scroll_button.rect.collidepoint(mouse_point):
                show_quest = not show_quest

        # Set previous state of left mouse button
        prev = left

        if chosen_npc is not None:
            if chosen_npc.add_npc_to_hud:
                update_hud(screen, hero, scroll_button, restore_life, restore_mana,
                           restore_mana_time_passed,
                           restore_life_time_passed, chosen_npc)
                all_sprites_group.update()

        if hero.in_attack:
            hero.fight(screen, option, npcs)
            all_sprites_group.update()
            print(hero.rect.x, hero.rect.y)

        # in npc is clicked, the buttons to fight or talk are displayed
        if npc_clicked:
            # check if npc can be in dialog or only cn fight
            if chosen_npc.can_talk:
                # NPC can fight and talk
                if not chosen_npc.is_talking and not chosen_npc.is_fighting:
                    # checking if talk or fight button are clicked
                    hero_in_dialog_or_talk(s, screen, fight_button, talk_button, chosen_npc, hero)
                    all_sprites_group.update()
            else:
                # NPC can only fight
                if not chosen_npc.is_talking and not chosen_npc.is_fighting:
                    hero_only_in_fight(s, screen, fight_button, chosen_npc, hero)
                    all_sprites_group.update()

        if hero.in_dialog:
            hero_in_dialog(s, screen, arrow_up, arrow_down, hero)
            all_sprites_group.update()

        update_hud(screen, hero, scroll_button, restore_life, restore_mana, restore_mana_time_passed,
                   restore_life_time_passed, chosen_npc)

        if show_quest:
            show_quest_to_hero(screen, hero)

        if hero.mana == 0 and not restore_mana:
            restore_mana = True
            # print("TEST")
            restore_mana_time_passed = datetime.now()
        elif hero.mana > 0:
            restore_mana = False

        if hero.life == 0 and not restore_life:
            restore_life = True
            restore_life_time_passed = datetime.now()
        elif hero.mana > 0:
            restore_life = False

        all_sprites_group.update()
        pygame.display.update()
        clock.tick(60)
