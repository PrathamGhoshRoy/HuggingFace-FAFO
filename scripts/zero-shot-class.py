from transformers import pipeline

zero_shot_classifier = pipeline("zero-shot-classification")

res = zero_shot_classifier(
    "How many people like ice-cream?",
    candidate_labels=["food", "beverage", "soup"]
)

print(res)