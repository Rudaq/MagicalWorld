import pygame

from NLP.dialog_generation.GenerateNpcDialog import wrap_text, draw_text
from game.fight_support import set_fight_parameters
from game.settings import BLACK, DIALOG_START, WIDTH_GAME, WHITE, GUI_IMAGES

# Function to limit the length of text input in the dialog and its formatting (moves text to the next line after 220
# characters and cutting it all together after 440) - hero text (this and the one for npc can be converted into one)
def check_text_length(text, screen, text_height_position, color):
    text_list = []
    if len(text) <= 220:
        text_list.append(text)
    else:
        text_list = wrap_text(text, 220, True)

    for i in range(len(text_list)):
        draw_text(text_list[i], 50, text_height_position, 12, color, screen)
        text_height_position += 20


# Function that checks if the text is in available position to be displayed
def check_transparency(text):
    if text.position == DIALOG_START + 25 or text.position == DIALOG_START + 100:
        text.transparent = True
    else:
        text.transparent = False


# Move text to make place for another
def update_positions_and_transparency(text_history):
    for text in text_history:
        text.position -= 150
        if text.position == DIALOG_START + 25 or text.position == DIALOG_START + 100:
            text.transparent = True
        else:
            text.transparent = False


# Function to move dialog up to see previous messages
def move_dialog_up(text_history):
    i = 0

    for text in text_history:
        check_transparency(text)
        if i == 0 and text.position == DIALOG_START + 25:
            break
        text.position += 75
        i += 1


# Function to move dialog down to see next messages
def move_dialog_down(text_history):
    reversed_text = text_history[::-1]
    for i in range(len(reversed_text)):
        check_transparency(reversed_text[i])
        if i == 0 and reversed_text[i].position == DIALOG_START + 100 and reversed_text[
            i + 1].position == DIALOG_START + 25:
            print("HERE")
            break
        reversed_text[i].position -= 75


def hero_in_dialog(surf, screen, arrow_up, arrow_down, hero):
    surf.fill(BLACK)
    surf.set_alpha(192)  # 0 - 255
    screen.blit(surf, (0, DIALOG_START))

    arrows = pygame.sprite.Group()
    arrow_up.rect.x = WIDTH_GAME - 50
    arrow_up.rect.y = DIALOG_START + 25
    arrow_down.rect.x = WIDTH_GAME - 50
    arrow_down.rect.y = DIALOG_START + 100

    arrows.add(arrow_up)
    arrows.add(arrow_down)

    for text in hero.text_history:
        check_transparency(text)
        if text.transparent:
            check_text_length(text.text, screen, text.position, text.color)

    arrows.update()
    arrows.draw(screen)
    pygame.draw.polygon(screen, BLACK, [(WIDTH_GAME - 45, 140), (WIDTH_GAME - 38, 130), (WIDTH_GAME - 30, 140)],
                        2)
    pygame.draw.polygon(screen, BLACK, [(WIDTH_GAME - 45, 210), (WIDTH_GAME - 38, 220), (WIDTH_GAME - 30, 210)],
                        2)

    border = pygame.Rect(0, DIALOG_START, WIDTH_GAME, 150)
    pygame.draw.rect(screen, WHITE, border, 2, 3)


def talk(hero, chosen_npc, talk_button, fight_button):

    if not chosen_npc.is_talking:
        chosen_npc.is_talking = True
        hero.in_dialog = True
        hero.hero_turn = False

        talk_button.change_image(GUI_IMAGES['clicked_talk_button'], 0.8)
        fight_button.change_image(GUI_IMAGES['fight_button'], 0.8)

        hero.my_text = ">> "
        print("START TALKING!!")

        # if yes - stop the dialog
    else:
        chosen_npc.is_talking = False
        hero.in_dialog = False
        hero.hero_turn = False
        hero.my_text = ">> "
        hero.text_history = []
        chosen_npc.text_history = []
        chosen_npc.text = ">> "
        print("STOP TALKING!!")
        talk_button.change_image(GUI_IMAGES['talk_button'], 0.8)
