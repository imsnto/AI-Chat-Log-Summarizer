import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from src.settings import settings

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
checkpoint = settings.checkpoint_path
model = T5ForConditionalGeneration.from_pretrained(checkpoint).to(device)
tokenizer = (T5Tokenizer.from_pretrained(checkpoint))

def get_conversation_topic(conversation):
    try:
        encoding = tokenizer(
            conversation,
            max_length=512,
            padding='max_length',
            truncation=True,
            return_tensors="pt"
        ).to(device)

        model.eval()
        with torch.no_grad():
            output = model.generate(
                input_ids = encoding['input_ids'],
                attention_mask = encoding['attention_mask'],
                max_length=128
            )
        return tokenizer.decode(output[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error : {str(e)}"
