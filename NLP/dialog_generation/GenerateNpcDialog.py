import random
from datetime import datetime
from pathlib import Path

import pygame
# Generating dialog text for NPC side and formatting it
from transformers import DistilBertTokenizerFast, pipeline, Conversation

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)

# conv_model_name="facebook/blenderbot-400M-distill"
conv_model = "microsoft/DialoGPT-medium"
conv_output = pipeline('conversational', model=conv_model)

# model_name_qa = "deepset/roberta-base-squad2"
model_name_qa = "deepset/tinyroberta-squad2"
qa_output = pipeline('question-answering', model=model_name_qa, tokenizer=model_name_qa)

model_name_sent = "cardiffnlp/twitter-roberta-base-sentiment"
sentiment_analysis = pipeline("sentiment-analysis", model=model_name_sent)


def check_if_question(sentence):
    question_starters = ["what", "who", "can", "why", "could", "would", "will", "did", "do", "does", "shall", "where",
                         "when", "are", "were", "is", "was", "have", "had", "how"]

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


def asking_for_quest(sentence, npc, hero):
    answers = ['Here you go', 'Go do the task!', 'It looks like you got a new task to do! Here you are',
               'Here you are!']
    if 'quest' in sentence or 'task' in sentence \
            or (hero.active_quest is not None and hero.active_quest.name == 'immortality_flower' and 'read' in sentence) \
            or (hero.active_quest is not None and hero.active_quest.name == 'smiths_tools' and 'tools' in sentence):
        # if statement for sentiment analysis
        sentence_cropped = sentence[3:]
        if sentiment_analysis(sentence_cropped)[0]['label'] == "LABEL_2" or (
                sentiment_analysis(sentence_cropped)[0]['label'] == "LABEL_1" and
                sentiment_analysis(sentence_cropped)[0]['score'] > 0.80):
            text = 'Check your scroll. If I have a quest for you, it\'ll be there'
            if npc.give_quest(hero):
                hero.new_task = True
                hero.restore_new_task = datetime.now()
            return True, text
        else:
            text = "I won't give you the quest. You're impolite."
            return True, text

    return False, ''


def produce_response(hero, npc):
    if hero.my_text == '>> ':
        if hero.side == npc.side:
            max = len(npc.nice_greetings)
            greeting_no = random.randint(0, max - 1)
            final_result = npc.nice_greetings[greeting_no]
        else:
            max = len(npc.rude_greetings)
            greeting_no = random.randint(0, max - 1)
            final_result = npc.rude_greetings[greeting_no]

        return final_result
    else:
        sentence = hero.my_text
        question = check_if_question(sentence)

        quest_request, final_result = asking_for_quest(sentence, npc, hero)
        # quest_request = False
        if not quest_request:
            if question and npc.context != '':
                sentence = replace_in_text(sentence, 'you', npc.race)
                sentence = replace_in_text(sentence, 'I', 'you')

                QA_input = {
                    'question': sentence,
                    'context': npc.context
                }
                result = qa_output(QA_input)

                print(result['answer'])
                final_result = result['answer']

                print("RACE: ", npc.race)
                final_result = replace_in_text(final_result, npc.race + 's', 'We')
                final_result = replace_in_text(final_result, npc.race, 'I')
                final_result = replace_in_text(final_result, npc.race + ' is ', 'I am ')
                final_result = replace_in_text(final_result, 'npc.name', npc.name)
                final_result = replace_in_text(final_result, 'his', 'my')
                final_result = replace_in_text(final_result, 'him', 'me')
                final_result = replace_in_text(final_result, 'them', 'us')
                final_result = final_result[0].upper() + final_result[1:]
                return final_result
            else:
                player_sentence = Conversation(sentence)
                final_text = conv_output(player_sentence)
                print(final_text)
                return (str(final_text).split('>>'))[-1][:-1]
        else:
            return final_result


# Method to draw text on the screen on the given height, width, size and in a specified color.
def draw_text(text, x, w, size, color, screen):
    font = pygame.font.SysFont('Verdana', size)
    img = font.render(text, True, color)
    screen.blit(img, (x, w))


# Placeholder for the future function generating text from npc side (chatbox model)
def generate_text(hero, npc):
    response = produce_response(hero, npc)
    print("Generating text")
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
