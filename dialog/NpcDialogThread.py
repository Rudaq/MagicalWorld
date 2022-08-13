import threading
from copy import copy

from dialog.DialogLine import DialogLine
from dialog.GenerateNpcDialog import generate_text, draw_text, wrap_text
from main import generate_text_about_character

DIALOG_START = 100

YELLOW = (255, 234, 0)
WHITE = (255, 255, 255)


# Thread function to generate npc side of the dialog without delaying and stopping the game.


# Thread supporting the npc side of the dialog
class NpcDialogThread(threading.Thread):
    def __init__(self, hero, screen, npcs):
        super().__init__()
        self.hero = hero
        self.screen = screen
        self.npcs = npcs

    # Main function of the thread - calls for the function generating text when it's npc's turn for talking
    def run(self):
        while True:
            if self.hero.in_dialog:
                if not self.hero.hero_turn:
                    for npc in self.npcs:
                        if npc.is_talking:
                            npc.text = ">> " + generate_text()
                            # npc.text_history.append(npc.text)
                            if len(self.hero.text_history) > 1:
                                reversed_text = self.hero.text_history[::-1]
                                pos = reversed_text[0].position
                            else:
                                pos = 50
                            npc_dialog_line = DialogLine(npc.text, pos + 75, YELLOW)
                            npc_dialog_line.transparent = True
                            self.hero.text_history.append(npc_dialog_line)
                            self.hero.hero_turn = True
                            self.hero.my_text = ">> "
                            hero_dialog_line = DialogLine(self.hero.my_text, pos + 150, WHITE)
                            hero_dialog_line.transparent = True
                            self.hero.text_history.append(hero_dialog_line)
                            break

