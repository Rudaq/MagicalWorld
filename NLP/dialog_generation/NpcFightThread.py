import threading

import pygame

from NLP.dialog_generation.DialogLine import DialogLine
from NLP.dialog_generation.GenerateNpcDialog import generate_text
from game.dialog_support import generate_random_answer, stop_talk
from game.fight_support import stop_fight, remove_npc

DIALOG_START = 100

YELLOW = (255, 234, 0)
WHITE = (255, 255, 255)


# Thread function to generate npc side of the dialog without delaying and stopping the game.


# Thread supporting the npc side of the dialog
class NpcFightThread(threading.Thread):
    def __init__(self, hero, screen, npcs, all_sprites_group):
        super().__init__()
        self.hero = hero
        self.screen = screen
        self.npcs = npcs
        self.all_sprites = all_sprites_group

    # Main function of the thread - calls for the function generating text when it's npc's turn for talking
    def run(self):
        clock = pygame.time.Clock()
        while True:

            if self.hero.chosen_npc is not None:
                if self.hero.chosen_npc.in_fight_mode:
                    self.hero.chosen_npc.move_in_fight(self.hero, self.all_sprites)
                    self.hero.chosen_npc.attack_type = None
                    self.hero.chosen_npc.fight_npc(self.screen, self.hero, self.npcs)
                    self.all_sprites.update()

            # Random movement of npcs if not in dialog
            # for npc in self.npcs:
            #     if not npc.is_talking and not npc.in_fight_mode:
            #         npc.move(self.all_sprites)

                # if npc.in_fight_mode:
                #     npc.move_in_fight(self.hero, self.all_sprites)
                #     npc.attack_type = None
                #     npc.fight_npc(self.screen, self.hero, self.npcs)

            # self.all_sprites.update()
            clock.tick(30)
