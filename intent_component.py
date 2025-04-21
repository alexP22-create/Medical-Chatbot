from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import re
import json

# Constants
tokenizer_path = "./intent_model/intent_model"
model_path = "./intent_model/intent_model"
mapping_path = model_path + "/id2label.json"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Load label mapping
with open(mapping_path, "r") as f:
    id2label = json.load(f)

def classify_intent(question):
    inputs = tokenizer(question, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=1).item()
    return id2label[str(predicted_class_id)]


def extract_slots(text):
    slots = {}

    date_match = re.search(r"\b(\d{1,2}\.\d{1,2}\.\d{4})\b", text)
    if date_match:
        slots["data"] = date_match.group(1)

    name_match = re.search(r"pacientul(?:ui)? ([A-Z][a-z]+ [A-Z][a-z]+)", text)
    if name_match:
        slots["nume_pacient"] = name_match.group(1)

    return slots
