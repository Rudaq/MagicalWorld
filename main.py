from transformers import pipeline

# Generating character description after given input text and ensuring it ends with the end of a sentence.


# Method to format the generated text. Clipping text after the last sentence - last dot.
def end_sentence_on_the_dot(text):
    splitted = text.split(" ")
    reversed_text = list(reversed(splitted))
    reversed_second = list(reversed(splitted))
    word_end = ""
    for token in reversed_second:
        if "." in token:
            isolated_words = token.split(".")
            reversed_text.remove(token)
            word_end = isolated_words[0] + '.'
            break
        # elif "," in token or ";" in token:
        #     word = []
        #     reversed_text.remove(token)
        #     token = token[:-1]
        #     word.append(token)
        #     word.append(".")
        #     word_end = ''.join(word)
        #     break
        else:
            reversed_text.remove(token)

    print(reversed_text)

    reversed_again = list(reversed(reversed_text))
    reversed_again.append(word_end)
    joined = ' '.join(reversed_again)
    return joined


# Method to generate the text about the character using saved model and input sequence
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
