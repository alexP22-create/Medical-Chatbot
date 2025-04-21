from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset, Dataset
import pandas as pd
import json

# Load dataset
df = pd.read_csv("intents_dataset.csv")

# Create label mappings
label2id = {label: i for i, label in enumerate(sorted(df['label'].unique()))}
id2label = {i: label for label, i in label2id.items()}
df['label_id'] = df['label'].map(label2id)

# Convert to HuggingFace dataset
dataset = Dataset.from_pandas(df)
dataset = dataset.remove_columns(["__index_level_0__"]) if "__index_level_0__" in dataset.column_names else dataset
dataset = dataset.train_test_split(test_size=0.2)

# Load tokenizer & model
model_name = "readerbench/RoBERT-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=len(label2id),
    id2label=id2label,
    label2id=label2id
)

# Tokenization function
def tokenize(example):
    return tokenizer(example["text"], padding="max_length", truncation=True)

# Tokenize the dataset
tokenized = dataset.map(tokenize, batched=True)
tokenized = tokenized.rename_column("label_id", "labels")
tokenized.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    save_total_limit=1,
    evaluation_strategy="epoch",  # this works across all recent versions
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
    load_best_model_at_end=True
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["test"],
    tokenizer=tokenizer
)

# Train the model
trainer.train()

# Save everything
model.save_pretrained("./intent_model")
tokenizer.save_pretrained("./intent_model")
with open("./intent_model/id2label.json", "w", encoding="utf-8") as f:
    json.dump(id2label, f, ensure_ascii=False, indent=2)
