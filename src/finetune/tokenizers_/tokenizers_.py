from transformers import T5Tokenizer

def get_t5tokenizer():
    return T5Tokenizer.from_pretrained('t5-small', legacy=False)

def get_t5finetune_tokenizer(checkpoint):
    return T5Tokenizer.from_pretrained(checkpoint, legacy=False)