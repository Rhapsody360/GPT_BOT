from transformers import AutoTokenizer, pipeline
import torch

model = "google/gemma-2b-it"
hf_access_token = "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"

tokenizer = AutoTokenizer.from_pretrained(model,token = hf_access_token)
pipeline = pipeline(
    "text-generation",
    model=model,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda" if(torch.cuda.is_available()) else "cpu",
    token = hf_access_token
)

messages = [
    {"role": "user", "content": "write a poem on machine learning with a pirate accent"},
]
prompt = pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipeline(
    prompt,
    max_new_tokens=1000,
    do_sample=True,
    temperature=0.2,
    top_k=50,
    top_p=0.95
)
print(outputs[0]["generated_text"][len(prompt):])


# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it",token=hf_access_token)
# model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it")

# input_text = "Write me a poem about Machine Learning."
# input_ids = tokenizer(input_text, return_tensors="pt")

# outputs = model.generate(**input_ids)
# print(tokenizer.decode(outputs[0]))
