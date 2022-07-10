from transformers import GPT2Model, GPT2Config, GPT2Tokenizer, GPT2LMHeadModel, TextDataset, \
    DataCollatorForLanguageModeling, pipeline, StoppingCriteriaList, MaxLengthCriteria, ConstraintListState
import torch
from sklearn.model_selection import train_test_split
from transformers import Trainer, TrainingArguments, AutoModelWithLMHead
import re

# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("gpt2")
#
# text_list = []
#
# with open("stories2.csv", "r") as my_input_file:
#     for line in my_input_file:
#         line = line.split(" ")
#         text_list.append(" ".join(line))
#
#
# train, test = train_test_split(text_list, test_size=0.2)
#
#
# def build_text_files(data, dest_path):
#     f = open(dest_path, 'w')
#     end_data = ''
#     for texts in data:
#         summary = str(texts).strip()
#         summary = re.sub(r"\s", " ", summary)
#         end_data += summary + "\n"
#     f.write(end_data)
#
#
# build_text_files(train, 'train_dataset.txt')
# build_text_files(test, 'test_dataset.txt')
#
# train_path = 'train_dataset.txt'
# test_path = 'test_dataset.txt'
#
#
# def load_data(train_path, test_path, tokenizer):
#     train_dataset = TextDataset(
#         tokenizer=tokenizer,
#         file_path=train_path,
#         block_size=12)
#
#     test_dataset = TextDataset(
#         tokenizer=tokenizer,
#         file_path=test_path,
#         block_size=12)
#
#     data_collator = DataCollatorForLanguageModeling(
#         tokenizer=tokenizer, mlm=False,
#     )
#
#     return train_dataset, test_dataset, data_collator
#
# train_dataset, test_dataset, data_collator = load_data(train_path, test_path, tokenizer)
#
# # model = AutoModelWithLMHead.from_pretrained("anonymous-german-nlp/german-gpt2")
#
#
# training_args = TrainingArguments(
#     output_dir="./my_gpt2",
#     overwrite_output_dir=True,
#     num_train_epochs=12,
#     per_device_train_batch_size=32,
#     per_device_eval_batch_size=64,
#     eval_steps=400,
#     save_steps=800,
#     warmup_steps=500,
#     prediction_loss_only=True,
#     )
#
#
# trainer = Trainer(
#     model=model,
#     args=training_args,
#     data_collator=data_collator,
#     train_dataset=train_dataset,
#     eval_dataset=test_dataset,
# )
#
# trainer.train()
# trainer.save_model()

sequence = "You are Orindell. A good elf"
# output = pipeline('text-generation', model='./my_gpt2', tokenizer='gpt2')
# final_text = output(sequence)[0]['generated_text']

def end_sentence_on_the_dot(text):
    splitted = text.split(" ")
    reversed_text = list(reversed(splitted))
    reversed_second = list(reversed(splitted))
    word_end = ""
    for token in reversed_second:
        if "." in token:
            break
        elif "," in token or ";" in token:
            word = []
            reversed_text.remove(token)
            token = token[:-1]
            word.append(token)
            word.append(".")
            word_end = ''.join(word)
            break
        else:
            reversed_text.remove(token)

    reversed_again = list(reversed(reversed_text))
    reversed_again.append(word_end)
    joined = ' '.join(reversed_again)
    return joined


def generate_text_about_character(sequence):
    output = pipeline('text-generation', model='./my_gpt2', tokenizer='gpt2')
    final_text = output(sequence)[0]['generated_text']
    final_text = end_sentence_on_the_dot(final_text)
    print("\n", final_text)
    return final_text

#
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("./my_gpt2")
#
# input_ids = tokenizer(sequence, return_tensors="pt").input_ids
#
# outputs = model.generate(input_ids)
# text = tokenizer.batch_decode(outputs, skip_special_tokens=False)
#
# final_text = text[0]
# print(final_text)
# final_text = end_sentence_on_the_dot(final_text)
# print(final_text)
