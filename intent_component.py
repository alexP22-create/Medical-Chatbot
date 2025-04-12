from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import re

tokenizer = AutoTokenizer.from_pretrained("./intent_model")
model = AutoModelForSequenceClassification.from_pretrained("./intent_model")

intents = [
    "get_diagnosis",
    "get_history",
    "get_hospitalizations",
    "get_treatments",
    "get_lab_results",
    "summarize_patient",
    "unknown"
]

def classify_intent(question):
    inputs = tokenizer(question, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return intents[predicted_class]

def extract_slots(text):
    slots = {}

    date_match = re.search(r"\b(\d{1,2}\.\d{1,2}\.\d{4})\b", text)
    if date_match:
        slots["data"] = date_match.group(1)

    name_match = re.search(r"pacientul(?:ui)? ([A-Z][a-z]+ [A-Z][a-z]+)", text)
    if name_match:
        slots["nume_pacient"] = name_match.group(1)

    return slots
