from transformers import T5ForConditionalGeneration

def get_t5model():
    return T5ForConditionalGeneration.from_pretrained("t5-small")

def get_t5finetune_model(checkpoint):
    return T5ForConditionalGeneration.from_pretrained(checkpoint)