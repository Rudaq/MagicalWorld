import pygame
# Generating dialog text for NPC side and formatting it


def draw_text(text, x, w, size, color, screen):
    font = pygame.font.SysFont('Verdana', size)
    img = font.render(text, True, color)
    screen.blit(img, (x, w))


# Placeholder
def generate_text():
    # text = "Hello!"
    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
    return text


def wrap_text(text):
    text_splitted = text.split(" ")
    text_list = []
    length_sum = 3

    joined_string = ""

    for word in text_splitted:
        if length_sum + len(word) <= 220:
            length_sum += len(word) + 1
            joined_string += word + " "
        else:
            text_list.append(joined_string)
            joined_string = word + " "
            length_sum = len(word) + 1

    text_list.append(joined_string)
    if len(text_list) > 2:
        return text_list[:2]
    else:
        return text_list
