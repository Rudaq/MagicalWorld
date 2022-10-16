import random
from pathlib import Path

import pygame
# Generating dialog text for NPC side and formatting it
from transformers import DistilBertTokenizerFast, pipeline, Conversation

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)

# conv_model_name="facebook/blenderbot-400M-distill"
conv_output = pipeline('conversational')
# sent_output = pipeline('sentiment-analysis', model="C:\\Inżynierka\\MagicalWorld\\NLP\\sentiment_analysis\\sent", tokenizer=tokenizer)

model_name_qa = "deepset/roberta-base-squad2"
qa_output = pipeline('question-answering', model=model_name_qa, tokenizer=model_name_qa)


def check_if_question(sentence):
    question_starters = ["what", "who", "can", "why", "could", "would", "will", "did", "do", "does", "shall", "where", "when", "are", "were", "is", "was", "have", "had", "how"]

    is_question = False
    splitted = sentence.split(' ', 1)[1]
    start = splitted.split(' ', 1)[0]
    start = start.lower()
    print("Start: ", start)
    if sentence.endswith('?') or "give" in sentence.lower():
        is_question = True
    elif start in question_starters:
        is_question = True

    return is_question


def replace_in_text(sentence, replaced, new_word):
    if replaced.lower() in sentence.lower():
        print("That's right")
        print(sentence.replace(replaced, new_word))
        return sentence.replace(replaced, new_word)
    return sentence


def produce_response(hero, npc):
    final_result = ''
    if hero.my_text == '>> ':
        if hero.side == npc.side:
            max = len(npc.nice_greetings)
            greeting_no = random.randint(0, max-1)
            final_result = npc.nice_greetings[greeting_no]
        else:
            max = len(npc.rude_greetings)
            greeting_no = random.randint(0, max-1)
            final_result = npc.rude_greetings[greeting_no]

        return final_result
    else:
        sentence = hero.my_text
        question = check_if_question(sentence)

        if question:
            sentence = replace_in_text(sentence, 'I', 'hero.race')
            sentence = replace_in_text(sentence, 'you', npc.race)
            # final_text = sent_output(sentence)
            # if final_text[0]["label"] == 'LABEL_1':
            # context = Path("C:\\Inżynierka\\MagicalWorld\\NLP\\dialog_generation\\DarkWizardContext.txt").read_text()

            QA_input = {
                'question': sentence,
                'context':  npc.context
            }
            result = qa_output(QA_input)

            print(result['answer'])
            final_result = result['answer']
            # else:
            #     final_result = "You're impolite, I won't help you."
            #     print("Negative")
            print("RACE: ", npc.race)
            final_result = replace_in_text(final_result, npc.race+'s', 'We')
            final_result = replace_in_text(final_result, npc.race, 'I')
            final_result = replace_in_text(final_result, 'hero.race', 'you')
            final_result = replace_in_text(final_result, 'them', 'us')
            final_result = final_result[0].upper() + final_result[1:]
            return final_result
        else:
            player_sentence = Conversation(sentence)
            final_text = conv_output(player_sentence)
            print(final_text)
            return (str(final_text).split('>>'))[-1][:-1]

# Method to draw text on the screen on the given height, width, size and in a specified color.
def draw_text(text, x, w, size, color, screen):
    font = pygame.font.SysFont('Verdana', size)
    img = font.render(text, True, color)
    screen.blit(img, (x, w))


# Placeholder for the future function generating text from npc side (chatbox model)
def generate_text(hero, npc):
    # text = "Hello!"
    response = produce_response(hero, npc)
    print("Generating text")
    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
    return response


# Function to limit the length of text input in the dialog and its formatting (moves text to the next line after 220
# characters and cutting it all together after 440)
def wrap_text(text, length, stop):
    text_splitted = text.split(" ")
    text_list = []
    length_sum = 3

    joined_string = ""

    for word in text_splitted:
        if length_sum + len(word) <= length:
            length_sum += len(word) + 1
            joined_string += word + " "
        else:
            text_list.append(joined_string)
            joined_string = word + " "
            length_sum = len(word) + 1

    text_list.append(joined_string)
    if stop:
        if len(text_list) > 2:
            return text_list[:2]
        else:
            return text_list
    else:
        return text_list
