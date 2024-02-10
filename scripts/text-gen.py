from transformers import pipeline

text_gen = pipeline("text-generation", model='distilgpt2')

res = text_gen(
    "I really like some cool and new ice-cream flavours",
    max_length = 30,
    num_return_sequences=2,
)

print(res)