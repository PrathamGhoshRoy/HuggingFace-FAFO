from transformers import pipeline

sentiment_classifier = pipeline("sentiment-analysis", verbose=False)

res = sentiment_classifier("I've been having a really good day, but some bad things happened, but that's okay.")

print(res)

print(type(res))