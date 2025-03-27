"""
analysiert user promt nach bestimmten regeln.
am ende sollen vier keywords ausgegeben werden, mit samt einer beschreibung des characters,
bei der aber keine Klasse erwähnt wird.
diese wird dann über das jeweilige Keyword gesteuer
"""
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialisiere das Modell und den Tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


def classify_prompt(prompt):
    # Tokenisieren und Modell anwenden
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=30, num_return_sequences=1, no_repeat_ngram_size=2)

    # Generierten Text dekodieren
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result


# Beispiel-Prompt analysieren
user_prompt = "Ein dunkler Zauberer, der mit Feuermagie und Teleportationsmagie zaubert."
result = classify_prompt(user_prompt)
print(result)