from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset, Dataset
import pandas as pd

# Încarcă datele
df = pd.read_csv("intents_dataset.csv")
label2id = {label: i for i, label in enumerate(df['label'].unique())}
id2label = {i: label for label, i in label2id.items()}
df['label_id'] = df['label'].map(label2id)

dataset = Dataset.from_pandas(df)

# Tokenizer + model
model_name = "readerbench/RoBERT-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(label2id))

# Tokenizare
def tokenize(example):
    return tokenizer(example["text"], padding="max_length", truncation=True)

dataset = dataset.train_test_split(test_size=0.2)
tokenized = dataset.map(tokenize)

# Argumente pentru fine-tuning
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    num_train_epochs=5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    save_total_limit=1,
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

# Start training
trainer.train()

# Salvează modelul fine-tunat
model.save_pretrained("./models/model")
tokenizer.save_pretrained("./models/")
