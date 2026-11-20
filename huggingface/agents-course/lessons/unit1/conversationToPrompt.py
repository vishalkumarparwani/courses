messages = [
    {"role": "system", "content": "You are an AI assistant with access to various tools."},
    {"role": "user", "content": "Hi !"},
    {"role": "assistant", "content": "Hi human, what can help you with ?"},
]


from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolM2-1.7B-Instruct")
rendered_prompt = tokenizer.apply_chat_template(messages, tokeize=False, add_generation_prpmpt=True)