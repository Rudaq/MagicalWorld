from transformers import pipeline

gpt2_generator = pipeline('text-generation', model='gpt2')

text = gpt2_generator("Welcome Orindell, the good elf", do_sample=True, temperature=0.7, top_k=50, num_return_sequence=10)

for sentence in text:
    print(sentence["generated_text"]+"\n")
    print("\n")
