#%% packages
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
load_dotenv(find_dotenv(usecwd=True))
from openai import OpenAI
#TODO: add package import
# %%
# Retrieve API key from environment variable
api_key=os.getenv("OPENAI_API_KEY")

# %%
# Model overview: https://console.groq.com/docs/models
MODEL_NAME = 'gpt-4o-mini'
#TODO: add the model
model = ChatOpenAI(model=MODEL_NAME,
                   temperature=0.7,
                   api_key=api_key)
# %% Run the model
res = model.invoke("What is a Generative AI?")
# %% find out what is in the result
res.model_dump()
# %% only print content
print(res.content)
# %%
client = OpenAI(api_key=api_key)
models = client.models.list()

print("--- OpenAI Models ---")
for model in models:
    print(f"Model ID: {model.id} | Owned By: {model.owned_by}")
# %%
