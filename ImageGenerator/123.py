#importing libraries 
import torch 
from transformers import GPT2Tokenizer, GPT2LMHeadModel 

#loading tokenizer and model 
tokenizer = GPT2Tokenizer.from_pretrained('gpt2') 
model = GPT2LMHeadModel.from_pretrained('gpt2') 

#generating image description 
text = "This is a stunning AI image of a" 
indexed_tokens = tokenizer.encode(text) 
tokens_tensor = torch.tensor([indexed_tokens]) 

#generating image using GPT-2 model 
with torch.no_grad(): 

    #predicting next word in the sequence  
    outputs = model(tokens_tensor)  

    #getting the predicted word index  
    predictions = outputs[0]  

    #converting the index to actual word  
    predicted_word = tokenizer.decode(predictions[0].argmax().item())  

    #appending the predicted word to the text  
    text += " "+predicted_word+"."  

    print("Generated Image Description:", text)