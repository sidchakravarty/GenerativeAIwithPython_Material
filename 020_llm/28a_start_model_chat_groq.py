#%% packages
import os
from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd = True))
# %%
# %%
api_key = api_key=os.getenv("GROQ_API_KEY")
# %%
# Fetches models available on Groq's LPU inference engine
client = Groq(api_key=api_key)
response = client.models.list()

print("--- Groq Models ---")
for model in response.data:
    # Groq provides additional metadata like 'context_window'
    print(f"ID: {model.id:30} | Developer: {model.owned_by}")

# %%
# Model overview: https://console.groq.com/docs/models

MODEL_NAME = "llama-3.3-70b-versatile"
model = ChatGroq(model=MODEL_NAME, 
                 temperature=0.7, 
                 api_key=api_key)
# %% Run the model
res = model.invoke("What is the capital of France?")
# %% find out what is in the result
res.model_dump()
# %% only print content
res.content
# %%
