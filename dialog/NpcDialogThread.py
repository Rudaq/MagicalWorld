import threading
from dialog.GenerateNpcDialog import generate_text, draw_text, wrap_text
from main import generate_text_about_character

YELLOW = (255, 234, 0)


# Thread function to generate npc side of the dialog without delaying and stopping the game.


# Thread supporting the npc side of the dialog
class NpcDialogThread(threading.Thread):
    def __init__(self, hero, screen, npc):
        super().__init__()
        self.hero = hero
        self.screen = screen
        self.npc = npc

    # Main function of the thread - calls for the function generating text when it's npc's turn for talking
    def run(self):
        while True:
            if self.hero.in_dialog:
                if not self.hero.hero_turn:
                    self.npc.text = ">> " + generate_text()
                    self.hero.hero_turn = True
                    self.hero.my_text = ">> "
            else:
                break

    # Method to set npc that takes part in the dialog
    def set_npc(self, npc):
        self.npc = npc
