
# from transformers import AutoModelForCausalLM, AutoTokenizer

# model_path = "Rhaps360/opt125m-ins-ft"

# tokenizer = AutoTokenizer.from_pretrained(model_path)
# model = AutoModelForCausalLM.from_pretrained(
#     model_path,
#     device_map="cpu",
#     torch_dtype='auto'
# ).eval()

# # Prompt content: "hi"
# messages = [
#     {"role": "user", "content": "i am depressed"}
# ]

# input_ids = tokenizer.apply_chat_template(conversation=messages, tokenize=True, add_generation_prompt=True, return_tensors='pt',max_new_tokens=70)
# output_ids = model.generate(input_ids.to('cpu'))
# response = tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True,max_new_tokens=70)

# # Model response: "Hello! How can I assist you today?"
# print(response)







from transformers import AutoTokenizer, pipeline
import torch

model = "Rhaps360/gemma-dep-ins-ft"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = pipeline(
    "text-generation",
    model=model,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda" if(torch.cuda.is_available()) else "cpu",
    )


def get_response(input):
    messages = [
        {"role": "user", "content": "### Context: "+input+" ### Response: "}
    ]
    prompt = pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = pipeline(
        prompt,
        max_new_tokens=300,
        do_sample=True,
        temperature=0.2,
        top_k=50,
        top_p=0.95
    )
    print(outputs[0]["generated_text"][len(prompt):])
    return (outputs[0]["generated_text"][len(prompt):])
